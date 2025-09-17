def validate_password():
  while True:
    password = input("Enter a password (9-12 characters): ")
    if 9 <= len(password) <= 12:
      print("Password accepted!")
      break
    else:
      print("Invalid password. It must be between 9 and 12 characters long.")

if __name__ == "__main__":
  validate_password()