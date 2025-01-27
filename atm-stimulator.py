import time
from termcolor import colored
import pygame

# Initialize pygame mixer for sound effects
pygame.mixer.init()

# Predefined users with fixed card numbers, PINs, and balances
users = {
    "1234567890123456": {"pin": "1234", "balance": 5000, "transactions": []},
    "9876543210987654": {"pin": "4321", "balance": 10000, "transactions": []},
    "1122334455667788": {"pin": "1111", "balance": 15000, "transactions": []},
    "9988776655443322": {"pin": "8765", "balance": 20000, "transactions": []},
    "5678901234567890": {"pin": "6789", "balance": 25000, "transactions": []}
}

def print_welcome_message():
    """Print a welcoming message with color"""
    print(colored("Welcome to the ATM Machine", 'green', attrs=['bold']))

def play_success_sound():
    """Play a success sound when a transaction is successful"""
    try:
        success_sound = pygame.mixer.Sound("success.wav")  # Add your own sound file here
        success_sound.play()
    except FileNotFoundError:
        print("Sound file 'success.wav' not found. Skipping sound.")

def login():
    """Simulate login with card number and PIN."""
    print_welcome_message()
    
    # Display predefined card numbers for the user to input
    print("\nAvailable Card Numbers: ")
    for card in users:
        print(colored(card, 'cyan'))

    card_number = input("\nEnter your 16-digit card number: ")

    # Check if the card number entered is valid (16 digits)
    if len(card_number) != 16 or not card_number.isdigit():
        print(colored("Invalid card number. Please enter a 16-digit card number.", 'red'))
        return None

    if card_number not in users:
        print(colored("Card not recognized.", 'red'))
        return None
    
    pin = input("Enter your PIN: ")
    
    if users[card_number]['pin'] != pin:
        print(colored("Incorrect PIN.", 'red'))
        return None
    
    print(colored("Login successful.", 'green'))
    return card_number

def show_balance(card_number):
    """Display the user's balance with formatted output."""
    print(f"Your current balance is {colored(f'₹{users[card_number]['balance']:,.2f}', 'yellow')}")

def deposit(card_number):
    """Deposit money into the user's account."""
    amount = float(input("Enter amount to deposit: ₹"))
    users[card_number]['balance'] += amount
    users[card_number]['transactions'].append(f"Deposited ₹{amount:,.2f}")
    play_success_sound()  # Play success sound
    print(colored(f"Successfully deposited ₹{amount:,.2f}. New balance: ₹{users[card_number]['balance']:,.2f}", 'green'))

def withdraw(card_number):
    """Withdraw money from the user's account."""
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if users[card_number]['balance'] >= amount:
        users[card_number]['balance'] -= amount
        users[card_number]['transactions'].append(f"Withdrew ₹{amount:,.2f}")
        play_success_sound()  # Play success sound
        print(colored(f"Successfully withdrew ₹{amount:,.2f}. New balance: ₹{users[card_number]['balance']:,.2f}", 'green'))
    else:
        print(colored("Insufficient funds!", 'red'))

def mini_statement(card_number):
    """Display the user's mini statement."""
    print("Mini Statement:")
    if users[card_number]['transactions']:
        for transaction in users[card_number]['transactions']:
            print(colored(transaction, 'blue'))
    else:
        print(colored("No transactions yet.", 'yellow'))

def change_pin(card_number):
    """Allow the user to change their PIN."""
    print("You can change your PIN now.")
    
    # Prompt the user for the old PIN
    old_pin = input("Enter your old PIN: ")
    
    if users[card_number]['pin'] != old_pin:
        print(colored("Incorrect old PIN. PIN change failed.", 'red'))
        return
    
    # Prompt for new PIN
    new_pin = input("Enter your new PIN (4 digits): ")
    
    # Validate the new PIN
    if len(new_pin) != 4 or not new_pin.isdigit():
        print(colored("Invalid PIN. Please enter a 4-digit PIN.", 'red'))
        return
    
    # Update the PIN
    users[card_number]['pin'] = new_pin
    print(colored("Your PIN has been successfully changed.", 'green'))

def show_transaction_history(card_number, n=5):
    """Display the last 'n' transactions of the user's account."""
    print(f"\nLast {n} Transactions:")
    transactions = users[card_number]['transactions'][-n:]  # Get the last 'n' transactions
    if transactions:
        for transaction in transactions:
            print(colored(transaction, 'magenta'))
    else:
        print(colored("No transactions available.", 'yellow'))

def show_menu():
    """Display the ATM menu."""
    print("\nATM Menu:")  # Debugging line
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Mini Statement")
    print("5. Change Pin")
    print("6. Transaction History")
    print("7. Exit")

def main():
    """Main function to drive the ATM simulation."""
    card_number = login()
    
    if card_number is None:
        return
    
    while True:
        show_menu()
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_balance(card_number)
        elif choice == '2':
            deposit(card_number)
        elif choice == '3':
            withdraw(card_number)
        elif choice == '4':
            mini_statement(card_number)
        elif choice == '5':
            change_pin(card_number)
        elif choice == '6':
            show_transaction_history(card_number)
        elif choice == '7':
            print(colored("Thank you for using the ATM. Goodbye!", 'green'))
            break  # Exit the loop if the user selects '7'
        else:
            print(colored("Invalid option. Please try again.", 'red'))
        
        time.sleep(2)

# Start the program
if __name__ == "__main__":
    main()
#ort merge