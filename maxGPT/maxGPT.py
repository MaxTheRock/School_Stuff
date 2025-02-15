import random
import time
from colorama import Fore
import maxGPT_data

def clear_screen():
  print("\033[H\033[J", end="")

print("Loading...")
clear_screen()

clear_screen()

while True:
  print()
  message = input("Enter a message: ")
  message = message.lower()
  
  if message in maxGPT_data.greeting_input: 
    print(Fore.CYAN + random.choice(maxGPT_data.greeting_output) + Fore.RESET)

  elif message in maxGPT_data.time_input:
    print(Fore.CYAN + f"The current time is {maxGPT_data.time_output}" + Fore.RESET)
  
  elif message in maxGPT_data.farewell_input:
    print(Fore.CYAN + random.choice(maxGPT_data.farewell_output) + Fore.RESET)
    break

  elif message in maxGPT_data.confirm_input:
    print(Fore.CYAN + random.choice(maxGPT_data.confirm_output) + Fore.RESET)

  elif message in maxGPT_data.joke_input:
    print(Fore.CYAN + random.choice(maxGPT_data.joke_output) + Fore.RESET)

  elif message in maxGPT_data.food_input:
    print(Fore.CYAN + random.choice(maxGPT_data.food_output) + Fore.RESET)

  elif message.isdigit():
    print(Fore.CYAN + "Thats a great number!" + Fore.RESET)

  elif message in maxGPT_data.spanish_input:
    print(Fore.CYAN + random.choice(maxGPT_data.spanish_output) + Fore.RESET)
  
  elif message in maxGPT_data.letRan_input:
    print(Fore.CYAN + random.choice(maxGPT_data.letRan_output) + Fore.RESET)
  
  elif message in maxGPT_data.clear_input:
    clear_screen()
  
  elif message in maxGPT_data.dumb_input:
    print(Fore.CYAN + random.choice(maxGPT_data.dumb_output) + Fore.RESET)
  
  elif message in maxGPT_data.howAreYou_input:
    print(Fore.CYAN + random.choice(maxGPT_data.howAreYou_output) + Fore.RESET)
  

  elif message != "":
    with open("messages.txt", "a") as file:
      file.write(f"{message}\n")