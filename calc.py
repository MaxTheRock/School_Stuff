
while True:
  num_1 = input("Enter first number: ")
  num_2 = input("Enter second number: ")

  num_1 = float(num_1)
  num_2 = float(num_2)

  operation = input("Enter operation (+, -, *, /): ")

  if operation == "+":
    answer = num_1 + num_2
  elif operation == "-":
    answer = num_1 - num_2
  elif operation == "*":
    answer = num_1 * num_2
  elif operation == "/":
    answer = num_1 / num_2

  print(float(answer))

  print(int(answer))
  
  while True:
    choice = input("Do you want to continue? (y/n): ")
    if choice == "n":
      quit()
    elif choice == "y":
      break
    else:
      print("Invalid choice")
      