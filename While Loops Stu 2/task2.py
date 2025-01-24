stored_pass = "Calder"

attempts = 0

while attempts < 4:
  password = input("Enter password: ")

  if password == stored_pass:
    print("Correct Password!")
    break
  
  elif attempts < 3:
    attempts += 1
    print(f"Incorrect, {4 - attempts}")
  
  else:
    print("!!!! Locked out !!!!")