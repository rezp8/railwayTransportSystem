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

class CardManager:
    def __init__(self, user):
        self.user = user
    
    def add_card(self):
        """Add a new card to user's saved cards"""
        clear_screen()
        print("=== Add New Card ===")
        print("(Type 'back' at any time to return to previous menu)")
        print()
        
        try:
            card_number = input("Card Number (16 digits, or 'back' to cancel): ").strip()
            if card_number.lower() == 'back':
                return False
            
            exp_month_input = input("Expiry Month (1-12, or 'back' to cancel): ").strip()
            if exp_month_input.lower() == 'back':
                return False
            exp_month = int(exp_month_input)
            
            exp_year_input = input("Expiry Year (1403-1408, or 'back' to cancel): ").strip()
            if exp_year_input.lower() == 'back':
                return False
            exp_year = int(exp_year_input)
            
            cvv2 = input("CVV2 (3 digits, or 'back' to cancel): ").strip()
            if cvv2.lower() == 'back':
                return False
            
            card_name = input("Card name (optional, e.g., 'My Visa Card', or 'back' to cancel): ").strip()
            if card_name.lower() == 'back':
                return False
            
            # Validate card data
            if len(card_number) != 16 or not card_number.isnumeric():
                print("❌ Invalid card number. Must be 16 digits.")
                input("Press Enter to continue...")
                return False
            
            if not (1 <= exp_month <= 12):
                print("❌ Invalid expiry month. Must be 1-12.")
                input("Press Enter to continue...")
                return False
            
            if exp_year < 1403 or exp_year > 1408:
                print("❌ Invalid expiry year. Must be 1403-1408.")
                input("Press Enter to continue...")
                return False
            
            if len(cvv2) != 3 or not cvv2.isnumeric():
                print("❌ Invalid CVV2. Must be 3 digits.")
                input("Press Enter to continue...")
                return False
            
            # Check if card already exists
            if any(card.card_number == card_number for card in self.user.cards):
                print("❌ This card is already saved.")
                input("Press Enter to continue...")
                return False
            
            # Create and add card
            new_card = Card(card_number, exp_month, exp_year, cvv2, card_name)
            self.user.cards.append(new_card)
            print(f"✅ Card '{new_card.card_name}' added successfully!")
            input("Press Enter to continue...")
            return True
            
        except ValueError:
            print("❌ Invalid input. Please enter valid numbers.")
            input("Press Enter to continue...")
            return False
    
    def show_cards(self):
        """Display all saved cards with balance information"""
        clear_screen()
        print("=== My Saved Cards ===")
        
        if not self.user.cards:
            print("No cards saved yet.")
            print("Add a card to make future purchases easier!")
        else:
            for i, card in enumerate(self.user.cards, 1):
                print(f"{i}. {card.get_display_info_with_balance()}")
        
        print("\nOptions:")
        print("1. View card details")
        print("2. Back to card management")
        choice = input("Choose option: ").strip()
        
        if choice == "1":
            self.view_card_details()
        # Otherwise, just return to card management
    
    def view_card_details(self):
        """View detailed information about a specific card"""
        if not self.user.cards:
            print("No cards to view.")
            input("Press Enter to continue...")
            return
        
        while True:
            clear_screen()
            print("=== Select Card to View Details ===")
            for i, card in enumerate(self.user.cards, 1):
                print(f"{i}. {card.get_display_info_with_balance()}")
            print(f"{len(self.user.cards) + 1}. Back to card list")
            
            try:
                choice = int(input("Select card number: "))
                if 1 <= choice <= len(self.user.cards):
                    card = self.user.cards[choice - 1]
                    self.show_card_transactions(card)
                    return
                elif choice == len(self.user.cards) + 1:
                    return
                else:
                    print("Invalid selection.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input.")
                input("Press Enter to continue...")
    
    def show_card_transactions(self, card):
        """Show transaction history for a specific card"""
        clear_screen()
        print(f"=== {card.card_name} - Transaction History ===")
        print(f"Card: {card.get_masked_number()}")
        print(f"Current Balance: {card.balance:,} Toman")
        print(f"Expiry: {card.exp_month:02d}/{card.exp_year}")
        print("-" * 50)
        
        if not card.transactions:
            print("No transactions found.")
        else:
            print("Recent Transactions:")
            print("-" * 50)
            for transaction in card.get_recent_transactions(10):
                amount_str = f"+{transaction['amount']:,}" if transaction['type'] in ['charge', 'refund'] else f"-{transaction['amount']:,}"
                print(f"{transaction['date']} | {amount_str} Toman | {transaction['type'].title()}")
                if transaction['description']:
                    print(f"  Description: {transaction['description']}")
                print()
        
        input("Press Enter to continue...")
    
    def select_card(self):
        """Let user select a card from saved cards"""
        if not self.user.cards:
            print("No saved cards. Please add a card first.")
            input("Press Enter to continue...")
            return None
        
        while True:
            clear_screen()
            print("=== Select Card ===")
            for i, card in enumerate(self.user.cards, 1):
                print(f"{i}. {card.get_display_info_with_balance()}")
            print(f"{len(self.user.cards) + 1}. Add new card")
            print(f"{len(self.user.cards) + 2}. Cancel")
            
            try:
                choice = int(input("Select card number: "))
                if 1 <= choice <= len(self.user.cards):
                    return self.user.cards[choice - 1]
                elif choice == len(self.user.cards) + 1:
                    if self.add_card():
                        continue  # Show selection menu again
                    else:
                        continue
                elif choice == len(self.user.cards) + 2:
                    return None
                else:
                    print("Invalid selection.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input.")
                input("Press Enter to continue...")
    
    def remove_card(self):
        """Remove a card from saved cards"""
        if not self.user.cards:
            print("No cards to remove.")
            input("Press Enter to continue...")
            return
        
        while True:
            clear_screen()
            print("=== Remove Card ===")
            for i, card in enumerate(self.user.cards, 1):
                print(f"{i}. {card.get_display_info()}")
            print(f"{len(self.user.cards) + 1}. Cancel")
            
            try:
                choice = int(input("Select card to remove: "))
                if 1 <= choice <= len(self.user.cards):
                    card_to_remove = self.user.cards[choice - 1]
                    confirm = input(f"Are you sure you want to remove '{card_to_remove.card_name}'? (y/n): ").strip().lower()
                    if confirm == 'y':
                        self.user.cards.remove(card_to_remove)
                        print("✅ Card removed successfully!")
                    input("Press Enter to continue...")
                    return
                elif choice == len(self.user.cards) + 1:
                    return
                else:
                    print("Invalid selection.")
                    input("Press Enter to continue...")
            except ValueError:
                print("Invalid input.")
                input("Press Enter to continue...")