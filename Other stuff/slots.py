import random
import time
from colorama import Fore

money = 10

auto = True

slot = ["🍇", "🍉", "🍊", "🍋", "🍍", "🍒", "7️⃣ ","⭐"]

def clear_screen():
  print("\033c")

def generate_3():
  global the_slot
  clear_screen()
  slot1 = random.choice(slot)
  slot2 = random.choice(slot)
  slot3 = random.choice(slot)
  the_slot = [slot1, slot2, slot3]
  print(Fore.CYAN + "**-- " + Fore.YELLOW + "Slots " + Fore.CYAN + "--**")
  print("  ",*the_slot)

def cycle():
  cycle_time = 0.1
  for i in range (10):
    generate_3()
    time.sleep(cycle_time)
    cycle_time -= 0.005

def check_for_win():
  global the_slot, money
  print()
  
  if the_slot[0] == the_slot[1] and the_slot[1] == the_slot[2]:
    print(Fore.GREEN + " 🎉 You win 🎉" + Fore.GREEN)
    money += 10
    print(f"  Credits: {money}")
    time.sleep(5)
  else:
    money -= 1
    print(Fore.RED + " X Try again X" + Fore.RESET)
    print(f"  Credits: {money}")
    time.sleep(0.5)
  

def top_up():
  global money
  print(Fore.CYAN + "How much money do you want to enter?")
  print(Fore.YELLOW + "1 Pound = 1 Credit")
  top = int(input(" >> "))

  money = money + top

def run():
  clear_screen()
  print("**-- Welcome to Slots --**")
  time.sleep(1)
  while True:
    cycle()
    check_for_win()
    print()
    
    if auto == False:
      input(Fore.RESET + "Press " + Fore.LIGHTMAGENTA_EX +"[Enter]" + Fore.RESET + " to continue >> ")

    if money <= 0:
      print(Fore.RED + "No more credits left")
      choice = input(Fore.RESET + "Press " + Fore.BLUE + "'t' " + Fore.RED + "to top up or press " + Fore.BLUE + "'q' " + Fore.RED + " to quit >> ")

      if choice == "t":
        top_up()
      else:
        quit()
