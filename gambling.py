import random
import time
import math

symbols = [
  "🍇", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍", "🥭", "🍎", "🍏", "🍐", "🍑", "🍒", "🍓", "🫐", "🥝", "🍅", "🥥",
  "💣", "💀", "❌"
]

credits = int(input("Enter credits: "))

def colour_check(s1, s2, s3):
  r_s = ["🍉", "🍎", "🍒", "🍓", "🍅", "❌"]
  o_s = ["🍊", "🍍", "🥭", "🍑"]
  y_s = ["🍋", "🍌", "🌽"]
  g_s = ["🍈", "🍏", "🍐", "🥝"]
  p_s = ["🍇", "🫐", "💣"]

  if (s1 in r_s) and (s2 in r_s) and (s3 in r_s):
    return True
  elif (s1 in o_s) and (s2 in o_s) and (s3 in o_s):
    return True
  elif (s1 in y_s) and (s2 in y_s) and (s3 in y_s):
    return True
  elif (s1 in g_s) and (s2 in g_s) and (s3 in g_s):
    return True
  elif (s1 in p_s) and (s2 in p_s) and (s3 in p_s):
    return True
  else:
    return False

def clear():
  print("\033c", end="")

while credits != 0:
  clear()
  slot1 = random.choice(symbols)
  slot2 = random.choice(symbols)
  slot3 = random.choice(symbols)
  
  print("🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨")
  print(f"🟥     {slot1} {slot2} {slot3}     🟥")
  print("🟨                  🟨")
  print("🟥                  🟥")
  
  
  if (slot1 == "💣") and (slot2== "💣") and (slot3=="💣"):
    credits = credits - (math.ceil(credits/2))
    print("")
    print("🔥  CREDIT BOMB   🔥")
    print("💣      ÷ 2      💣")
    time.sleep(3)
  elif (slot1 == "💀") and (slot2== "💀") and (slot3=="💀"):
    credits = credits - 667
    print("")
    print("🔥  CREDIT SKULL  🔥")
    print("💀     - 667      💀")
    time.sleep(3)
  elif (slot1 == "❌") and (slot2== "❌") and (slot3=="❌"):
    credits = credits - 5000
    print("")
    print("🔥  CREDIT SKULL  🔥")
    print("❌    - 5000      ❌")
    time.sleep(3)
  elif (slot1 in ["💣", "💀", "❌"]) and (slot2 in ["💣", "💀", "❌"]) and (slot3 in ["💣", "💀", "❌"]):
    credits = credits - 50
    print("")
    print("❌     OH NO...   ❌")
    print("💣     - 50       💀")
    time.sleep(3)
  elif (slot1 == slot2) and (slot2 == slot3):
    credits = credits + 500
    print("")
    print("🎰 CREDIT JACKPOT 🎰")
    print("🎰     + 500      🎰")
    time.sleep(3)
  elif colour_check(slot1,slot2,slot3):
    clear()
    print("🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥")
    print(f"      {slot1} {slot2} {slot3}")
    print("🎰 COLOUR JACKPOT 🎰")
    print("🎰     + 10       🎰")
    print("      Credits: ")
    print(f"      {credits}")
    time.sleep(2)
    credits = credits + 10
    clear()
    print("")
    print(f"      {slot1} {slot2} {slot3}")
    print("🎰 COLOUR JACKPOT 🎰")
    print("🎰     + 10       🎰")
    print("      Credits: ")
    print(f"      {credits}")
    
    time.sleep(1)
  elif ((slot1 == "💀") or (slot1 == "❌") or (slot1 == "🥥")) and ((slot2 == "💀") or (slot2 == "❌") or (slot2 == "🥥")) and ((slot3 == "💀") or (slot3 == "❌") or (slot3 == "🥥")):
    credits = credits + 250
    print("🎰 PIRATE JACKPOT 🎰")
    print("🦴     + 250      🦴")
    time.sleep(3)
  else:
    credits -= 1
    space = 8 - len(str(credits))
    spaces = ""
    for _ in range(space):
      spaces += " "
    
    print("🟨     Credits:     🟨")
    print(f"🟥     {credits}{spaces}     🟥")
    print("🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨")
  time.sleep(0.5)

print("No credits left :(")
time.sleep(99)
