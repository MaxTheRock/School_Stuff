import random
from colorama import Fore

loop = int(input("How many tries do you want to use: "))
total = []

while loop!=0:
  num = random.randint(0,1)
  if num == 1:
    print(Fore.GREEN + f"{num}", end="")
  else:
    print(Fore.RED + f"{num}", end="")
  total.append(num)
  loop = loop-1
print()
print("Total numbers: ",len(total))