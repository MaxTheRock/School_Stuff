import math

def calculate_area(radius):
	return math.pi * radius ** 2

def main():
	while True:
		try:
			radius = int(input("Enter the radius of the circle (1-30): "))
			if 1 <= radius <= 30:
				print(f"The area of the circle with radius {radius} is {calculate_area(radius):.2f}")
				break
			else:
				print("Please enter a whole number between 1 and 30.")
		except ValueError:
			print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
	main()

