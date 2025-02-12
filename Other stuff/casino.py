from simple_term_menu import TerminalMenu
from colorama import Fore, init
import blackjack

init(autoreset=True)

def clear_screen():
    print("\033[H\033[J", end="")

def play_slots():
    clear_screen()
    print(Fore.CYAN + "Playing slots")
    # Add your slots game logic here

def play_random():
    clear_screen()
    print(Fore.CYAN + "Playing random guess")
    # Add your random guess game logic here

def play_select():
    options = [
        Fore.GREEN + "Slots [AVAILABLE]" + Fore.RESET,
        Fore.GREEN + "Random Guess [AVAILABLE]" + Fore.RESET,
        Fore.GREEN + "Blackjack [AVAILABLE]" + Fore.RESET,
        Fore.RED + "Back" + Fore.RESET
    ]
    terminal_menu = TerminalMenu(options, title=Fore.CYAN + "What would you like to play?" + Fore.RESET, menu_cursor=Fore.RED + "> " + Fore.RESET, menu_cursor_style=("fg_red", "bold"))
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        play_slots()
    elif menu_entry_index == 1:
        play_random()
    elif menu_entry_index == 2:
        blackjack.run()
    elif menu_entry_index == 3:
        return

def options_menu():
    clear_screen()
    print(Fore.CYAN + "Options menu")
    # Add your options logic here

def credits_menu():
    clear_screen()
    print(Fore.CYAN + "Credits menu")
    # Add your credits logic here

def main_menu():
    options = [
        Fore.GREEN + "Play" + Fore.RESET,
        Fore.YELLOW + "Options" + Fore.RESET,
        Fore.BLUE + "Credits" + Fore.RESET,
        Fore.RED + "Quit" + Fore.RESET
    ]
    terminal_menu = TerminalMenu(options, title=Fore.CYAN + "Main Menu" + Fore.RESET, menu_cursor=Fore.RED + "> " + Fore.RESET, menu_cursor_style=("fg_red", "bold"))
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        play_select()
    elif menu_entry_index == 1:
        options_menu()
    elif menu_entry_index == 2:
        credits_menu()
    elif menu_entry_index == 3:
        return

if __name__ == "__main__":
    main_menu()