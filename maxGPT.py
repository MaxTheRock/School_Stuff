import random
import time
from colorama import Fore

greetings = ["Hello, what are you up to?", "Hey, how are you doing?", "Hi, how can I help you?"]
farewells = ["Goodbye, have a great day!", "See you later!", "Bye, take care!"]

def clear_screen():
  print("\033[H\033[J", end="")

def greeting():
  print(Fore.CYAN + random.choice(greetings) + Fore.RESET)

def tell_time():
  current_time = time.strftime("%H:%M:%S")
  print(Fore.CYAN + f"The current time is {current_time}" + Fore.RESET)

def farewell():
  print(Fore.CYAN + random.choice(farewells) + Fore.RESET)

while True:
  message = input("Enter a message: ")
  message = message.lower()
  if message == "hello" or message == "hi" or message == "hey" or message == "sup": 
    greeting()

  if message == "time" or message == "current time" or message == "what time is it" or message == "tell me the time" or message == "what is the time":
    tell_time()
  
  if message == "bye" or message == "goodbye" or message == "see you later" or message == "take care" or message == "cya":
    farewell()
    break