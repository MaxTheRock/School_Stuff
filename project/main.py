a, b, c = 0, 3, 3

while a < 2:
  print(f"Before inner loop: a < 2={a < 2}, b > 0={b > 0}, a={a}, b={b}, c={c}")
  a = a + 1
  while b > 0:
    b = b - 1
    c = c - a + b
    print(f"Inside inner loop: a < 2={a < 2}, b > 0={b > 0}, a={a}, b={b}, c={c}")

print(f"After loops: a < 2={a < 2}, b > 0={b > 0}, a={a}, b={b}, c={c}")
