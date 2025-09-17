#!/usr/bin/env python3
"""
generate_starwars_crawl.py

Generates a Star Wars–style tilted crawl MP4 (static starfield + glowing yellow text).
Save as generate_starwars_crawl.py and run: python generate_starwars_crawl.py

Dependencies:
    pip install pillow numpy opencv-python
"""

import os
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import cv2

# ----------------- USER CONFIG -----------------
OUT_FILE = "star_wars_crawl_placeholder.mp4"
WIDTH, HEIGHT = 1920, 1080
DURATION = 90               # seconds
FPS = 30
FRAMES = int(DURATION * FPS)
BACKGROUND_STAR_COUNT = 800  # number of stars in starfield
STAR_BRIGHTNESS = 200        # 0..255
FONT_PATH = None             # set to a ttf path if you want (e.g., "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
FONT_SIZE = 64
TEXT_COLOR = (255, 232, 31)  # yellow (R,G,B)
GLOW_RADIUS = 12             # how strong the glow is (blur radius)
CROP_TEXT_WIDTH = WIDTH * 0.7
TILT_ANGLE_DEG = 60          # classic Star Wars tilt (~60°)
SPEED_FACTOR = 0.45          # lower -> slower scroll; adjust for readability
# ------------------------------------------------

# Placeholder text - exactly as requested
CREDITS_TEXT = """
[YOUR PRESENTATION TITLE]

Episode [X]: [SUBTITLE]

[INTRO TEXT LINE 1]

[INTRO TEXT LINE 2]

[INTRO TEXT LINE 3]

CREDITS

Director: [NAME]
Producer: [NAME]
Writer: [NAME]
Design: [NAME]
Special Thanks: [NAME]
"""

# Create output directory if needed
os.makedirs(".", exist_ok=True)

def make_starfield(w, h, count, brightness=255):
    """Create a static starfield (PIL Image)"""
    img = Image.new("RGB", (w, h), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    rng = np.random.default_rng()
    xs = rng.integers(0, w, size=count)
    ys = rng.integers(0, h, size=count)
    sizes = rng.integers(1, 3, size=count)
    for x, y, s in zip(xs, ys, sizes):
        color = (brightness, brightness, brightness)
        # draw small ellipse for star
        draw.ellipse((x, y, x + s, y + s), fill=color)
    return img

def load_font(size):
    if FONT_PATH and os.path.isfile(FONT_PATH):
        return ImageFont.truetype(FONT_PATH, size)
    # fallback to a default PIL font (may not scale perfectly)
    try:
        return ImageFont.truetype("DejaVuSans-Bold.ttf", size)
    except Exception:
        return ImageFont.load_default()

def render_long_text_image(text, width, font):
    """Render multiline text onto a tall image (PIL) centered and wrapped."""
    wrapper = textwrap.TextWrapper(width=40)  # coarse wrap; we will re-wrap with font metrics later
    lines = [ln for paragraph in text.strip().split("\n\n") for ln in (paragraph.splitlines() + [""])]
    # Better wrapping by measuring
    words = text.strip().split()
    # Build paragraphs
    para_texts = text.strip().split("\n\n")
    wrapped_lines = []
    for p in para_texts:
        p = p.strip()
        if not p:
            wrapped_lines.append("")
            continue
        # wrap by pixel width
        line = ""
        for word in p.split():
            test = (line + " " + word).strip()
            bbox = font.getbbox(test)  # Use getbbox instead of getsize
            w = bbox[2] - bbox[0]  # Calculate width from bounding box
            if w <= width:
                line = test
            else:
                wrapped_lines.append(line)
                line = word
        wrapped_lines.append(line)
        wrapped_lines.append("")  # paragraph gap
    # Estimate height
    line_h = int(font.getbbox("Ay")[3] * 1.45)  # Use getbbox for height
    img_h = max(HEIGHT * 3, int(line_h * max(30, len(wrapped_lines) + 10)))  # tall canvas
    img = Image.new("RGBA", (width, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    y = 40
    for ln in wrapped_lines:
        if ln == "":
            y += int(line_h * 0.5)
            continue
        bbox = font.getbbox(ln)
        w = bbox[2] - bbox[0]
        draw.text(((width - w) // 2, y), ln, font=font, fill=TEXT_COLOR + (255,))
        y += line_h
    return img

def add_glow(pil_img, radius):
    """Return PIL Image with glow (blurred copy under original)."""
    # Create glow by blurring alpha channel
    base = pil_img.convert("RGBA")
    alpha = base.split()[3]
    # Enlarge alpha to make glow softer
    glow = alpha.filter(ImageFilter.GaussianBlur(radius=radius))
    # create a colored glow image
    glow_img = Image.new("RGBA", base.size, TEXT_COLOR + (0,))
    glow_img.putalpha(glow)
    # Composite glow then original text
    combined = Image.alpha_composite(glow_img, base)
    return combined

def pil_to_cv2(img_pil):
    """Convert PIL Image to BGR numpy for OpenCV"""
    arr = np.array(img_pil.convert("RGB"))
    return cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

def perspective_warp(src_img_cv2, dst_size, tilt_angle_deg):
    """
    Create a perspective transform that simulates the tilt.
    src_img_cv2: source image (BGR)
    dst_size: (w,h)
    tilt_angle_deg: how much the top should appear smaller (larger -> more tilt)
    """
    h_dst = dst_size[1]
    w_dst = dst_size[0]

    h_src, w_src = src_img_cv2.shape[:2]

    # We will map a rectangle from the source to a trapezoid in the destination.
    # Top width relative to bottom
    top_scale = max(0.05, 1.0 - (tilt_angle_deg / 90.0))  # ~0.33 for 60deg
    top_w = int(w_dst * top_scale)
    bottom_w = int(w_dst * 0.85)

    # Target polygon (clockwise)
    dst_quad = np.float32([
        [(w_dst - top_w)//2, int(h_dst * 0.05)],                         # top-left
        [(w_dst + top_w)//2, int(h_dst * 0.05)],                         # top-right
        [(w_dst + bottom_w)//2, int(h_dst * 0.95)],                      # bottom-right
        [(w_dst - bottom_w)//2, int(h_dst * 0.95)],                      # bottom-left
    ])

    # Source polygon: a centered rectangle in the source image
    src_w = w_src
    src_h = h_src
    src_quad = np.float32([
        [0, 0],
        [src_w, 0],
        [src_w, src_h],
        [0, src_h]
    ])

    M = cv2.getPerspectiveTransform(src_quad, dst_quad)
    warped = cv2.warpPerspective(src_img_cv2, M, (w_dst, h_dst), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_TRANSPARENT)
    return warped

def main():
    print("Generating starfield...")
    starfield = make_starfield(WIDTH, HEIGHT, BACKGROUND_STAR_COUNT, STAR_BRIGHTNESS)

    print("Preparing font and text image (this may take a moment)...")
    font = load_font(FONT_SIZE)
    text_img = render_long_text_image(CREDITS_TEXT, int(CROP_TEXT_WIDTH), font)

    # Apply glow
    print("Adding glow to text...")
    text_with_glow = add_glow(text_img, GLOW_RADIUS)

    # Convert to cv2 BGR
    text_cv2 = pil_to_cv2(text_with_glow)  # note: size = (CROP_TEXT_WIDTH, tall_h)

    # We'll make a wide canvas to warp from (so the warped shape looks correct)
    print("Creating video writer...")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # mp4 output; change if you can use H264
    writer = cv2.VideoWriter(OUT_FILE, fourcc, FPS, (WIDTH, HEIGHT))

    # Pre-convert starfield to cv2
    star_cv2 = pil_to_cv2(starfield)

    tall_h = text_cv2.shape[0]
    # initial vertical offset: start lower than screen bottom
    start_y = HEIGHT + 100
    # end offset: when the top of text is well above frame
    end_y = -tall_h - 100

    # compute per-frame offsets with easing (smooth)
    positions = np.linspace(start_y, end_y, FRAMES)

    print(f"Rendering {FRAMES} frames (this can take a while)...")
    for i, y in enumerate(positions):
        # 1) create empty frame from starfield
        frame = star_cv2.copy()

        # 2) make a blank RGBA canvas to paste the text at the current y
        overlay_rgba = np.zeros((HEIGHT, WIDTH, 4), dtype=np.uint8)  # RGBA

        # compute x to center the text canvas horizontally
        x = (WIDTH - text_cv2.shape[1]) // 2
        y_int = int(y)

        # paste text_cv2 onto overlay_rgba at (x, y_int)
        # compute intersection region
        src_h, src_w = text_cv2.shape[:2]

        dst_x0 = max(0, x)
        dst_x1 = min(WIDTH, x + src_w)
        dst_y0 = max(0, y_int)
        dst_y1 = min(HEIGHT, y_int + src_h)

        src_x0 = max(0, -x)
        src_x1 = src_x0 + (dst_x1 - dst_x0)
        src_y0 = max(0, -y_int)
        src_y1 = src_y0 + (dst_y1 - dst_y0)

        if dst_x1 > dst_x0 and dst_y1 > dst_y0:
            overlay_rgba[dst_y0:dst_y1, dst_x0:dst_x1, :3] = text_cv2[src_y0:src_y1, src_x0:src_x1, :]
            # compute alpha from brightness of text (approx)
            alpha = cv2.cvtColor(text_cv2[src_y0:src_y1, src_x0:src_x1, :], cv2.COLOR_BGR2GRAY)
            alpha = (alpha.astype(np.float32) / 255.0 * 255).astype(np.uint8)
            overlay_rgba[dst_y0:dst_y1, dst_x0:dst_x1, 3] = alpha

        # 3) convert overlay to PIL, apply perspective warp (we warp the entire overlay canvas)
        overlay_pil = Image.fromarray(cv2.cvtColor(overlay_rgba, cv2.COLOR_BGRA2RGBA))
        overlay_cv2_full = cv2.cvtColor(np.array(overlay_pil), cv2.COLOR_RGBA2BGRA)

        # warp the overlay (perspective)
        warped = perspective_warp(overlay_cv2_full, (WIDTH, HEIGHT), TILT_ANGLE_DEG)

        # 4) composite warped (BGRA) over starfield (BGR)
        # Separate alpha
        if warped.shape[2] == 4:
            alpha = warped[:, :, 3].astype(np.float32) / 255.0
            for c in range(3):
                frame[:, :, c] = (warped[:, :, c].astype(np.float32) * alpha + frame[:, :, c].astype(np.float32) * (1 - alpha)).astype(np.uint8)
        else:
            # fallback - no alpha
            frame = cv2.addWeighted(warped[:, :, :3], 1.0, frame, 0.0, 0)

        # 5) write frame
        writer.write(frame)

        if (i + 1) % (FPS * 5) == 0:
            print(f"  - frame {i+1}/{FRAMES} ({(i+1)/FRAMES*100:.1f}%)")

    writer.release()
    print(f"Done. Output file: {OUT_FILE}")
    print("If the video looks too compressed or codec issues appear, you can re-encode with ffmpeg, e.g.:")
    print(f"  ffmpeg -i {OUT_FILE} -c:v libx264 -crf 18 -preset slow final_h264.mp4")

if __name__ == "__main__":
    main()