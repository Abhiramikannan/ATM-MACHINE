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
    amount = float(input("Enter amount to deposit: ₹"))
    users[card_number]['balance'] += amount
    users[card_number]['transactions'].append(f"Deposited ₹{amount:,.2f}")
    print(f"Successfully deposited ₹{amount:,.2f}. New balance: ₹{users[card_number]['balance']:,.2f}")

def withdraw(card_number):
    """Withdraw money from the user's account."""
    amount = float(input("Enter amount to withdraw: ₹"))
    
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

def main():
    """Main function to drive the ATM simulation."""
    card_number = login()
    
    if card_number is None:
        return
    
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")
        
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
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        time.sleep(2)

if __name__ == "__main__":
    main()
