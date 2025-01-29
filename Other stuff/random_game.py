import random
import time
from colorama import Fore

money = 5
auto = True

def clear_screen():
  print("\033c")

def generate():
  global the_slot, choice_of_num
  clear_screen()
  the_slot = random.randint(1,100)
  if money > 10:
    colour_credits = Fore.GREEN
  elif money > 5:
    colour_credits = Fore.YELLOW
  else:
    colour_credits = Fore.RED
  print(Fore.CYAN + "**-- " + Fore.YELLOW + "Random " + Fore.CYAN + "--**" + colour_credits + f"       Credits: {money}")
  print()
  print("Your choice: ",choice_of_num)
  print("Computer choice: ",the_slot)

def cycle():
  cycle_time = 0.1
  for i in range (10):
    generate()
    time.sleep(cycle_time)
    cycle_time -= 0.005

def check_for_win(num_choice):
  global the_slot, money
  print()
  
  if the_slot == num_choice:
    print(Fore.GREEN + " 🎉 You win 🎉" + Fore.GREEN)
    money += 10
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
  global choice_of_num
  clear_screen()
  print("**-- Welcome to Random Game --**")
  time.sleep(1)
  while True:
    global auto
    choice_of_num = int(input("Enter a number between [1 - 100] >> "))
    cycle()
    check_for_win(choice_of_num)
    print()
    
    if auto == False:
      input(Fore.RESET + "Press " + Fore.LIGHTMAGENTA_EX +"[Enter]" + Fore.RESET + " to continue >> ")

    if money <= 0:
      print(Fore.RED + "No more credits left")
      choice = input(Fore.RED + "Press " + Fore.BLUE + "'t' " + Fore.RED + "to top up or press " + Fore.BLUE + "'q' " + Fore.RED + " to quit >> ")

      if choice == "t":
        top_up()
      else:
        quit()
