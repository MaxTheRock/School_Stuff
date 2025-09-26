racetype = ""
while racetype!="A" and racetype!="B" and racetype!="C" and racetype!="D":
  print("")
  racetype = input("What was the race type A B C or D")
  racetype=racetype.upper()
  if racetype!="A" and racetype!="B" and racetype!="C" and racetype!="D":
    print("")
    print("You need to enter either A B C D")
    print("")

racetime=46.00
while racetime<0.0 or racetime>45.00:
  racetime=float(input("What is the race time?"))
  if racetime<0.0 or racetime>45.00:
    print("")
    print("You need to enter a number between 0.0 and 45.0")
    print("")
  else:
    x=2
  
