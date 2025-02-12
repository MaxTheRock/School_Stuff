from random import randint

class Roulette:
    def __init__(self):
        # Initialize the game state
        self.balance = 100
        self.stake = 0

    def place_bet(self):
        while True:
            try:
                self.stake = float(input("Enter your bet amount: "))
                if 0 < self.stake <= self.balance:
                    self.balance -= self.stake
                    return True
                else:
                    print("Invalid bet amount. Please enter a positive value less than or equal to your balance.")
            except ValueError:
                print("Invalid input. Please enter a valid bet amount.")

    def spin_wheel(self):
        # Simulate spinning the roulette wheel
        return randint(0, 36)

    def place_red_bet(self):
        if self.place_bet():
            result = self.spin_wheel()
            print(f"Result: {result}")
            if result % 2 == 0 and result != 0:  # even number
                winnings = self.stake * 2
                self.balance += winnings
                print(f"You win! Your balance is now ${self.balance:.2f}.")
            else:
                print("You lose!")

    def place_black_bet(self):
        if self.place_bet():
            result = self.spin_wheel()
            print(f"Result: {result}")
            if result % 2 != 0:  # odd number
                winnings = self.stake * 2
                self.balance += winnings
                print(f"You win! Your balance is now ${self.balance:.2f}.")
            else:
                print("You lose!")

    def place_even_bet(self):
        if self.place_bet():
            result = self.spin_wheel()
            print(f"Result: {result}")
            if result % 2 == 0 and result != 0:  # even number
                winnings = self.stake * 2
                self.balance += winnings
                print(f"You win! Your balance is now ${self.balance:.2f}.")
            else:
                print("You lose!")

    def place_odd_bet(self):
        if self.place_bet():
            result = self.spin_wheel()
            print(f"Result: {result}")
            if result % 2 != 0:  # odd number
                winnings = self.stake * 2
                self.balance += winnings
                print(f"You win! Your balance is now ${self.balance:.2f}.")
            else:
                print("You lose!")

    def run(self):
        while self.balance > 0:
            print(f"\nYour current balance: ${self.balance:.2f}")
            bet_type = input("Choose your bet type (red/black/even/odd): ").strip().lower()
            if bet_type == "red":
                self.place_red_bet()
            elif bet_type == "black":
                self.place_black_bet()
            elif bet_type == "even":
                self.place_even_bet()
            elif bet_type == "odd":
                self.place_odd_bet()
            else:
                print("Invalid bet type. Please choose red, black, even, or odd.")

        print("You have lost all your money! Game over.")

if __name__ == "__main__":
    game = Roulette()
    game.run()