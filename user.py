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
