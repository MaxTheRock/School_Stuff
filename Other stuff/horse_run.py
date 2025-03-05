import random

horse_icon = "🐎"
horse_pos = 0

field = [" " * 20]

def horse_run():
  global horse_pos
  while horse_pos < len(field[0]) - 1:
    horse_pos += random.randint(1, 3)
    if horse_pos >= len(field[0]):
      horse_pos = len(field[0]) - 1
    print("\033c", end="")  # Clear the screen
    print(f"{' ' * horse_pos}{horse_icon}")

horse_run()