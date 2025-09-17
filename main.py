age = 0
while age < 17 or age > 75:
  name = input("What is your name: ")
  print("hello ", name)
  age = int(input("What is your age: "))

  if age < 17 or age > 75:
    print("You do not fall within our age range")
    print("Restart...")
  else:
    print("Welcome to the driving licence program")