import re
from utils import validate_email, validate_password, validate_registration_data, clear_screen

class Card:
    def __init__(self, card_number, exp_month, exp_year, cvv2, card_name=""):
        self.card_number = card_number
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.cvv2 = cvv2
        self.card_name = card_name or f"Card ending in {card_number[-4:]}"
        self.balance = 0  # Track card balance
        self.transactions = []  # Track transaction history
    
    def get_masked_number(self):
        """Return masked card number for display (e.g., **** **** **** 1234)"""
        return f"**** **** **** {self.card_number[-4:]}"
    
    def get_display_info(self):
        """Return formatted card info for display"""
        return f"{self.card_name} - {self.get_masked_number()} (Exp: {self.exp_month:02d}/{self.exp_year})"
    
    def get_display_info_with_balance(self):
        """Return formatted card info with balance"""
        return f"{self.card_name} - {self.get_masked_number()} (Exp: {self.exp_month:02d}/{self.exp_year}) - Balance: {self.balance:,} Toman"
    
    def add_transaction(self, amount, transaction_type, description=""):
        """Add a transaction to the card's history"""
        import datetime
        transaction = {
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'amount': amount,
            'type': transaction_type,  # 'charge', 'payment', 'refund'
            'description': description
        }
        self.transactions.append(transaction)
        
        # Update balance based on transaction type
        if transaction_type == 'charge':
            self.balance += amount
        elif transaction_type == 'payment':
            self.balance -= amount
        elif transaction_type == 'refund':
            self.balance += amount
    
    def get_recent_transactions(self, limit=5):
        """Get recent transactions for display"""
        return self.transactions[-limit:] if self.transactions else []

class User:
    def __init__(self, username, email, name, password):
        self.username = username
        self.email = email
        self.name = name
        self.password = password
        self.wallet = 0
        self.cards = []

class UserManager:
    users = [
        # Temporary test user for system testing
        User("testuser", "test@example.com", "Test User", "password123@")
    ]

    def register(self):
        while True:
            clear_screen()
            print("=== Register ===")
            print("(Type 'back' at any time to return to previous menu)")
            print()
            
            username = input("Enter username (or 'back' to cancel): ").strip()
            if username.lower() == 'back':
                return False
            
            email = input("Enter email (or 'back' to cancel): ").strip()
            if email.lower() == 'back':
                return False
            
            name = input("Enter name (or 'back' to cancel): ").strip()
            if name.lower() == 'back':
                return False
            
            password = input("Enter password (or 'back' to cancel): ").strip()
            if password.lower() == 'back':
                return False

            # Validate all data at once
            errors = validate_registration_data(username, email, name, password, self.users)
            
            if errors:
                print("\n❌ Registration failed. Please fix the following issues:")
                for i, error in enumerate(errors, 1):
                    print(f"   {i}. {error}")
                print("\nOptions:")
                print("1. Try again")
                print("2. Go back to main menu")
                choice = input("Choose option: ").strip()
                
                if choice == "2":
                    return False
                continue

            # If no errors, create user
            new_user = User(username, email, name, password)
            self.users.append(new_user)
            print("\n✅ Registration successful!")
            input("Press Enter to continue...")
            return True

    def login(self):
        while True:
            clear_screen()
            print("=== Login ===")
            print("(Type 'back' at any time to return to previous menu)")
            print()
            
            username = input("Username (or 'back' to cancel): ").strip()
            if username.lower() == 'back':
                return None
            
            password = input("Password (or 'back' to cancel): ").strip()
            if password.lower() == 'back':
                return None

            user = next((u for u in self.users if u.username == username and u.password == password), None)
            if user:
                print("Login successful!")
                input("Press Enter to continue...")
                return user
            else:
                print("Invalid credentials.")
                print("\nOptions:")
                print("1. Try again")
                print("2. Go back to main menu")
                choice = input("Choose option: ").strip()
                if choice == "2":
                    return None

    def edit_user_info(self, user):
        clear_screen()
        print("=== Edit User Info ===")
        print("(Type 'back' at any time to return to previous menu)")
        print()
        print(f"Current Name: {user.name}")
        print(f"Current Email: {user.email}")
        print("Note: Username cannot be changed.")
        print()

        name = input("New name (leave blank to keep current, or 'back' to cancel): ").strip()
        if name.lower() == 'back':
            return
        
        email = input("New email (leave blank to keep current, or 'back' to cancel): ").strip()
        if email.lower() == 'back':
            return

        if name:
            user.name = name
        if email:
            if validate_email(email):
                user.email = email
            else:
                print("Invalid email format.")
                input("Press Enter to continue...")
                return

        print("Information updated.")
        input("Press Enter to continue...")

