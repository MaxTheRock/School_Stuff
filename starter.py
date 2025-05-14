total = 0

fo = int(input("> "))
so = int(input("> "))
fs = int(input("> "))
ss = int(input("> "))

for index in range (fo,so):
  total = total + 1
  print("First")
  for number in range (fs,ss):
    total = total + 1
    print("Second")

print(total)