import random
import time
import math
from typing import List, Dict

rs = "🟥"
ys = "🟨"

SYMBOLS = [
    "🍇", "🍈", "🍉",
    "🍊", "🍋", "🍌",
    "🍍", "🥭", "🍎",
    "🍏", "🍐", "🍑",
    "🍒", "🍓", "🫐",
    "🥝", "🍅", "🥥",
    "💣", "💀", "❌",
]

# Color groups for checking matches
COLORS: Dict[str, List[str]] = {
    "red": ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"],
    "orange": ["🍊", "🍍", "🥭", "🍑"],
    "yellow": ["🍋", "🍌"],
    "green": ["🍈", "🍏", "🍐", "🥝"],
    "purple": ["🍇", "🫐", "💣"],
}

SPECIAL_SYMBOLS = ["💣", "💀", "❌"]
PIRATE_SYMBOLS = ["💀", "❌", "🥥"]

credits = int(input("Enter credits: "))


def colour_check(s1: str, s2: str, s3: str) -> bool:
    for color_group in COLORS.values():
        if s1 in color_group and s2 in color_group and s3 in color_group:
            return True
    return False


def clear() -> None:
    print("\033c", end="")


while credits > 0:
    clear()
    slot1, slot2, slot3 = [random.choice(SYMBOLS) for _ in range(3)]
    jackpot_type = f"{rs}                  {rs}"
    mult_type = f"{rs}                  {rs}"

    # Check for special combinations
    if slot1 == slot2 == slot3 == "💣":
        credits -= math.ceil(credits / 2)
        jackpot_type = f"{rs}   CREDIT BOMB    {rs}"
        mult_type = f"{rs}💣     ÷ 2     💣{rs}"
    elif slot1 == slot2 == slot3 == "💀":
        credits -= 667
        jackpot_type = f"{rs}   CREDIT SKULL   {rs}"
        mult_type = f"{rs}💀    - 667     💀{rs}"
    elif slot1 == slot2 == slot3 == "❌":
        credits -= 2000
        jackpot_type = f"{rs}     CREDIT X     {rs}"
        mult_type = f"{rs}❌   - 2000     ❌{rs}"
    elif all(s in SPECIAL_SYMBOLS for s in [slot1, slot2, slot3]):
        credits -= 50
        jackpot_type = f"{rs}      OH NO...    {rs}"
        mult_type = f"{rs}💣    - 50     💀{rs}"
    elif slot1 == slot2 == slot3:
        credits += 500
        jackpot_type = f"{rs}  CREDIT JACKPOT  {rs}"
        mult_type = f"{rs}🎰    + 500     🎰{rs}"
    elif colour_check(slot1, slot2, slot3):
        credits += 10
        jackpot_type = f"{rs}  COLOUR JACKPOT  {rs}"
        mult_type = f"{rs}🎰    + 10      🎰{rs}"
    elif all(s in PIRATE_SYMBOLS for s in [slot1, slot2, slot3]):
        credits += 250
        jackpot_type = f"{rs}  PIRATE JACKPOT  {rs}"
        mult_type = f"{rs}🦴    + 250     🦴{rs}"
    
    credits -= 1
    credit_str = str(credits)
    total_width = 18
    pad = total_width - len(credit_str)
    left = pad // 2
    right = pad - left
    spaces_left = " " * left
    spaces_right = " " * right
        
    print(f"{ys}{rs}{ys}{rs}{ys}{rs}{ys}{rs}{ys}{rs}{ys}")
    print(f"{jackpot_type}")
    print(f"{ys}     {slot1} {slot2} {slot3}     {ys}")
    print(f"{mult_type}")
    print(
            f"{ys}     Credits:     {ys}\n{rs}{spaces_left}{credit_str}{spaces_right}{rs}\n{ys}{rs}{ys}{rs}{ys}{rs}{ys}{rs}{ys}{rs}{ys}"
        )
    if jackpot_type != f"{rs}                  {rs}":
      time.sleep(3)
    else:
      time.sleep(0.3)
    
    ys,rs = rs,ys

print("No credits left :(")
while True: continue
