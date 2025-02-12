import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def start_game(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
        self.show_hands()

    def show_hands(self):
        print(Fore.CYAN + f"Player's Hand: {Fore.GREEN}{self.player_hand} {Fore.CYAN}(Value: {Fore.GREEN}{self.player_hand.value()}{Fore.CYAN})")
        time.sleep(1)
        print(Fore.CYAN + f"Dealer's Hand: {Fore.GREEN}{self.dealer_hand.cards[0]}, Hidden Card")
        time.sleep(1)

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal())
        print(Fore.CYAN + f"Player's Hand: {Fore.GREEN}{self.player_hand} {Fore.CYAN}(Value: {Fore.GREEN}{self.player_hand.value()}{Fore.CYAN})")
        time.sleep(1)
        if self.player_hand.value() > 21:
            print(Fore.RED + "Player busts! Dealer wins.")
            time.sleep(1)

    def dealer_play(self):
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal())
        print(Fore.CYAN + f"Dealer's Hand: {Fore.GREEN}{self.dealer_hand} {Fore.CYAN}(Value: {Fore.GREEN}{self.dealer_hand.value()}{Fore.CYAN})")
        time.sleep(1)
        if self.dealer_hand.value() > 21:
            print(Fore.GREEN + "Dealer busts! Player wins.")
        elif self.dealer_hand.value() > self.player_hand.value():
            print(Fore.RED + "Dealer wins.")
        elif self.dealer_hand.value() < self.player_hand.value():
            print(Fore.GREEN + "Player wins.")
        else:
            print(Fore.YELLOW + "It's a tie!")
        time.sleep(1)

def run():
    game = BlackjackGame()
    game.start_game()
    while game.player_hand.value() < 21:
        action = input(Fore.CYAN + "Do you want to hit or stand? ").strip().lower()
        if action == 'hit':
            game.player_hit()
        elif action == 'stand':
            break
    game.dealer_play()

if __name__ == "__main__":
    run()