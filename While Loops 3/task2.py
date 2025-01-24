loop_amount = int(input("How many GCSE's do you have: "))

total = 0

while loop_amount > 0:
  input("Enter subject: ")
  grade = int(input("Enter grade: "))

  total = total + grade
  loop_amount -= 1

print(f"Your score {total}")

if total > 40:
  print("You can go to six form!")
else:
  print("Sorry not enough points")