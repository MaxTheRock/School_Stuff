import random
import time

balance = 100

def clear():
  print("\033c")

def typing_print(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.05)

def loading():
  print("Loading...")
  time.sleep(1)

def racing(bet, horse_pick, balance):
  clear()
  print("Racing...")
  winner = random.randint(1, 4)
  time.sleep(1)
  print(f"The winner is Horse {winner}!\n")
  if winner == horse_pick:
    balance += bet * 2
    print(f"Congratulations! You have won £{bet * 2}.\n")
  else:
    print(f"Sorry, you have lost £{bet}.\n")
  print(f"Your balance is now £{balance}.\n")
  while True:
    try:
      play_again = input("Do you want to play again? (yes/no): ")
      if play_again == "yes":
        game()
      elif play_again == "no":
        clear()
        typing_print("Thank you for playing!\n")
        break
      else:
        print("Please enter 'yes' or 'no'.")
    except ValueError:
      pass

def game():
  clear()
  typing_print(f"Pick your horse!\n")
  print()
  print("Horse 1")
  time.sleep(0.5)
  print("Horse 2")
  time.sleep(0.5)
  print("Horse 3")
  time.sleep(0.5)
  print("Horse 4")
  time.sleep(0.5)
  while True:
    global balance
    try:
      horse_pick = int(input("Enter the number of the horse you want to bet on: "))
      if horse_pick in range(1, 5):
        break
      else:
        print("Please enter a number between 1 and 4.")
    except ValueError:
      print("Please enter a number.")
  while True:
    try:
      bet = int(input("Enter the amount you want to bet: "))
      if bet < balance:
        balance -= bet
        break
      else:
        print("You do not have enough money.")
    except ValueError:
      print("Please enter a number.")
  print(f"You have bet £{bet} on Horse {horse_pick}.\n")
  
  racing(bet, horse_pick, balance)



def run():
  loading()
  clear()
  typing_print("Welcome to the Horse Betting Game!\n")
  time.sleep(0.5)
  typing_print("You have £100 to start with.\n")
  print()
  game()


if __name__ == '__main__':
  run()