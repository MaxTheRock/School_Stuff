from numba import jit

@jit(nopython=True)
def main():
  for i in range (2000001):
    print(i)


if __name__ == "__main__":
  main()