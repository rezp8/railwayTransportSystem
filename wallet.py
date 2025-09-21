# wallet.py
from BANK import API
from user import CardManager

class WalletManager:
    def add_funds_prompt(self, user):
        print("=== Add Funds ===")
        print("(Type 'back' at any time to return to previous menu)")
        print()
        
        # Ask user if they want to use saved card or enter new one
        if user.cards:
            print("1. Use saved card")
            print("2. Enter new card")
            print("3. Back to previous menu")
            choice = input("Choose option: ").strip()
            
            if choice == "3" or choice.lower() == "back":
                return
            elif choice == "1":
                card_manager = CardManager(user)
                selected_card = card_manager.select_card()
                if not selected_card:
                    return
                
                # Use selected card
                card = selected_card.card_number
                exp_month = selected_card.exp_month
                exp_year = selected_card.exp_year
                cvv2 = selected_card.cvv2
                
                # Still need password for payment
                password = input("Password (6 digits, or 'back' to cancel): ").strip()
                if password.lower() == 'back':
                    return
            elif choice == "2":
                # Enter new card details
                card, exp_month, exp_year, cvv2, password = self._get_new_card_details()
                if not card:
                    return
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                return
        else:
            # No saved cards, enter new card
            print("No saved cards found.")
            print("1. Enter new card")
            print("2. Back to previous menu")
            choice = input("Choose option: ").strip()
            
            if choice == "2" or choice.lower() == "back":
                return
            elif choice == "1":
                card, exp_month, exp_year, cvv2, password = self._get_new_card_details()
                if not card:
                    return
            else:
                print("Invalid choice.")
                input("Press Enter to continue...")
                return
        
        try:
            amount = float(input("Amount to add: "))
            api = API()
            payment_id = api.pay(card, exp_month, exp_year, password, cvv2, amount)
            user.wallet += amount
            
            # If it's a new card, ask if user wants to save it
            if not any(c.card_number == card for c in user.cards):
                save_card = input("Save this card for future use? (y/n): ").strip().lower()
                if save_card == 'y':
                    card_name = input("Card name (optional): ").strip()
                    from user import Card
                    new_card = Card(card, exp_month, exp_year, cvv2, card_name)
                    # Add transaction to the new card
                    new_card.add_transaction(amount, 'charge', f'Wallet top-up - Payment ID: {payment_id}')
                    user.cards.append(new_card)
                    print("✅ Card saved successfully!")
            else:
                # Find the existing card and add transaction
                existing_card = next(c for c in user.cards if c.card_number == card)
                existing_card.add_transaction(amount, 'charge', f'Wallet top-up - Payment ID: {payment_id}')
            
            print(f"Payment successful! Payment ID: {payment_id}")
            print(f"New balance: {user.wallet}")
        except Exception as e:
            print("Payment failed:", str(e))
        input("Press Enter to continue...")
    
    def _get_new_card_details(self):
        """Get new card details from user"""
        try:
            card = input("Card Number (16 digits, or 'back' to cancel): ").strip()
            if card.lower() == 'back':
                return None, None, None, None, None
            
            exp_month_input = input("Expiry Month (1-12, or 'back' to cancel): ").strip()
            if exp_month_input.lower() == 'back':
                return None, None, None, None, None
            exp_month = int(exp_month_input)
            
            exp_year_input = input("Expiry Year (1403-1408, or 'back' to cancel): ").strip()
            if exp_year_input.lower() == 'back':
                return None, None, None, None, None
            exp_year = int(exp_year_input)
            
            password = input("Password (6 digits, or 'back' to cancel): ").strip()
            if password.lower() == 'back':
                return None, None, None, None, None
            
            cvv2 = input("CVV2 (3 digits, or 'back' to cancel): ").strip()
            if cvv2.lower() == 'back':
                return None, None, None, None, None
            
            return card, exp_month, exp_year, cvv2, password
        except ValueError:
            print("Invalid input.")
            input("Press Enter to continue...")
            return None, None, None, None, None

    def has_sufficient_balance(self, user, amount):
        return user.wallet >= amount

    def deduct_balance(self, user, amount):
        user.wallet -= amount
    
    def record_ticket_purchase(self, user, amount, train_name, ticket_count):
        """Record a ticket purchase transaction"""
        # This could be enhanced to track which card was used for the purchase
        # For now, we'll just record it as a general transaction
        pass