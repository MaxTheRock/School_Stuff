a = 0
b = 4
c = 2 

while a < 3:
  a = a + 1 
  print("A: ",a)
  while b > 0:
    b = b - 1 
    print("B: ",b)
    c = c - a + b
    print("C: ",c)


print(a, b, c) 