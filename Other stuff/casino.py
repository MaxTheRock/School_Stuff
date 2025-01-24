import random
import time
from colorama import Fore
import slots

def clear_screen():
  print("\033c")

def menu_screen():
  clear_screen()
  print(Fore.CYAN + "**-- Welcome to Max's Casino --**")
  print()
  print("1. ",Fore.RED + "Play" + Fore.CYAN)
  print("2. ",Fore.WHITE + "Options" + Fore.CYAN)
  print("3. ",Fore.RED + "Credits" + Fore.CYAN)
  print("4. ",Fore.WHITE + "Quit" + Fore.CYAN)

  while True:
    try:
      option = int(input("Enter choice >> "))
      if option <= 4:
        break
      else:
        print(Fore.RED + "Enter [1,2,3,4]" + Fore.RESET)
    except ValueError:
      print(Fore.RED + "Enter [1,2,3,4]" + Fore.RESET)
  
  if option == 1:
    play_select()
  elif option == 2:
    options()
  elif option == 3:
    credits_()
  else:
    quit()

def play_select():
  clear_screen()
  print(Fore.CYAN + "What would you like to play")
  print()
  print("1. ",Fore.GREEN + "Slots [AVAILABLE]" + Fore.CYAN)
  print("2. ",Fore.RED + "Random Guess [UNAVALIABLE]" + Fore.CYAN)
  print("3. ",Fore.RED + "Blackjack [UNAVAILABLE]" + Fore.CYAN)
  print("4. ",Fore.WHITE + "Back" + Fore.CYAN)

  while True:
    try:
      option = int(input("Enter choice >> "))
      if option <= 4:
        break
      else:
        print(Fore.RED + "Enter [1,2,3,4]" + Fore.RESET)
    except ValueError:
      print(Fore.RED + "Enter [1,2,3,4]" + Fore.RESET)
  
  if option == 1:
    play_slots()
  elif option == 2:
    play_random()
  elif option == 3:
    play_blackjack()
  else:
    menu_screen()

def options():
  clear_screen()

  pass

def credits_():
  clear_screen()
  pass

def play_slots():
  slots.run()
  pass

def play_random():
  pass

def play_blackjack():
  pass

menu_screen()