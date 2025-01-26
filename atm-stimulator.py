import time

# Predefined users with fixed card numbers, PINs, and balances
users = {
    "1234567890123456": {"pin": "1234", "balance": 5000, "transactions": []},
    "9876543210987654": {"pin": "4321", "balance": 10000, "transactions": []},
    "1122334455667788": {"pin": "1111", "balance": 15000, "transactions": []},
    "9988776655443322": {"pin": "8765", "balance": 20000, "transactions": []},
    "5678901234567890": {"pin": "6789", "balance": 25000, "transactions": []}
}

def login():
    """Simulate login with card number and PIN."""
    print("Welcome to the ATM Machine")
    
    # Display predefined card numbers for the user to input
    print("\nAvailable Card Numbers: ")
    for card in users:
        print(card)

    card_number = input("\nEnter your 16-digit card number: ")

    # Check if the card number entered is valid (16 digits)
    if len(card_number) != 16 or not card_number.isdigit():
        print("Invalid card number. Please enter a 16-digit card number.")
        return None

    if card_number not in users:
        print("Card not recognized.")
        return None
    
    pin = input("Enter your PIN: ")
    
    if users[card_number]['pin'] != pin:
        print("Incorrect PIN.")
        return None
    
    print("Login successful.")
    return card_number

def show_balance(card_number):
    """Display the user's balance."""
    print(f"Your current balance is ₹{users[card_number]['balance']:,.2f}")

def deposit(card_number):
    """Deposit money into the user's account."""
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return

    users[card_number]['balance'] += amount
    users[card_number]['transactions'].append(f"Deposited ₹{amount:,.2f}")
    print(f"Successfully deposited ₹{amount:,.2f}. New balance: ₹{users[card_number]['balance']:,.2f}")

def withdraw(card_number):
    """Withdraw money from the user's account."""
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return
    
    if users[card_number]['balance'] >= amount:
        users[card_number]['balance'] -= amount
        users[card_number]['transactions'].append(f"Withdrew ₹{amount:,.2f}")
        print(f"Successfully withdrew ₹{amount:,.2f}. New balance: ₹{users[card_number]['balance']:,.2f}")
    else:
        print("Insufficient funds!")

def mini_statement(card_number):
    """Display the user's mini statement."""
    print("Mini Statement:")
    if users[card_number]['transactions']:
        for transaction in users[card_number]['transactions']:
            print(transaction)
    else:
        print("No transactions yet.")

def change_pin(card_number):
    """Allow the user to change their PIN."""
    print("You can change your PIN now.")
    
    # Prompt the user for the old PIN
    old_pin = input("Enter your old PIN: ")
    
    if users[card_number]['pin'] != old_pin:
        print("Incorrect old PIN. PIN change failed.")
        return
    
    # Prompt for new PIN
    new_pin = input("Enter your new PIN (4 digits): ")
    
    # Validate the new PIN
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("Invalid PIN. Please enter a 4-digit PIN.")
        return
    
    # Update the PIN
    users[card_number]['pin'] = new_pin
    print("Your PIN has been successfully changed.")

# Function to show the last 'n' transactions of the user
def show_transaction_history(card_number, n=5):
    """Display the last n transactions of the user's account."""
    print(f"\nLast {n} Transactions:")
    transactions = users[card_number]['transactions'][-n:]  # Get the last 'n' transactions
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions available.")

def main():
    """Main function to drive the ATM simulation."""
    print("ATM program started.")  # Debugging line
    card_number = login()
    
    if card_number is None:
        return
    
    while True:
        print("\nATM Menu:")  # Debugging line
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change Pin")
        print("6. Transaction History")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        print(f"User chose option: {choice}")  # Debugging line
        
        if choice == '1':
            show_balance(card_number)
        elif choice == '2':
            deposit(card_number)
        elif choice == '3':
            withdraw(card_number)
        elif choice == '4':
            mini_statement(card_number)
        elif choice == '5':
            change_pin(card_number)  # Call the change_pin function
        elif choice == '6':
            show_transaction_history(card_number)  # Show transaction history
        elif choice == '7':
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the loop if the user selects '7'
        else:
            print("Invalid option. Please try again.")
        
        time.sleep(2)

if __name__ == "__main__":
    main()
