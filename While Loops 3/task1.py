count = 0
sum = 0
x = 1

while x==1:
  number = int(input("What number do you want? ")) # Asks for a number
  count=count+1 # Adds 1 to the count
  sum=sum+number # Adds number to the sum

  y = 1
  while y==1:
    question = input("Do you want another go?") # Asks for another go
    question=question.lower()
    if question=="yes" or question=="y": # Loops again
      x=1
      y=2
    elif question=="no" or question=="n":
      x=2
      y=2
      print("Amount of numbers entered: ",count)
      print("The sum of all the numbers are: ", sum)
    else:
      print("You have not entered a yes or a no")
      x=2
      y=1