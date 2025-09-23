# main.py
from user import UserManager, CardManager
from train import TrainManager
from ticket import TicketManager
from wallet import WalletManager
from utils import print_sep


def regular_user_flow():
    user_manager = UserManager()
    train_manager = TrainManager()
    ticket_manager = TicketManager()
    wallet_manager = WalletManager()

    while True:
        # clear_screen()
        print_sep("Regular User Panel")
        # print("=== Regular User Panel ===")
        print("1. Register")
        print("2. Login")
        print("3. Back to Start Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            success = user_manager.register()
            if not success:
                continue  # User chose to go back
        elif choice == "2":
            user = user_manager.login()
            if user:
                purchase_flow(user, user_manager, train_manager, ticket_manager, wallet_manager)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

def purchase_flow(user, user_manager, train_manager, ticket_manager, wallet_manager):
    card_manager = CardManager(user)
    
    while True:
        # clear_screen()
        print_sep("Purchase Panel")
        # print("=== Purchase Panel ===")
        print("1. Buy Ticket")
        print("2. Edit User Information")
        print("3. Manage Cards")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            train_manager.show_trains()
            train = train_manager.select_train()
            if train:
                # Check if user has sufficient balance first
                if wallet_manager.has_sufficient_balance(user, train.price):
                    count_input = input("How many tickets? (or 'back' to cancel): ").strip()
                    if count_input.lower() == 'back':
                        continue
                    
                    try:
                        count = int(count_input)
                        total_cost = train.price * count
                        if wallet_manager.has_sufficient_balance(user, total_cost):
                            # Ask user to select a card for the purchase
                            selected_card = None
                            if user.cards:
                                print("\nSelect a card for this purchase:")
                                for i, card in enumerate(user.cards):
                                    print(f"{i+1}. {card.get_display_info_with_balance()}")
                                print(f"{len(user.cards)+1}. Use wallet balance only")
                                
                                card_choice = input("Choose card (or 'back' to cancel): ").strip()
                                if card_choice.lower() == 'back':
                                    continue
                                
                                try:
                                    card_idx = int(card_choice) - 1
                                    if 0 <= card_idx < len(user.cards):
                                        selected_card = user.cards[card_idx]
                                    elif card_idx == len(user.cards):
                                        selected_card = None  # Use wallet only
                                    else:
                                        print("Invalid selection.")
                                        input("Press Enter to continue...")
                                        continue
                                except ValueError:
                                    print("Invalid selection.")
                                    input("Press Enter to continue...")
                                    continue
                            
                            wallet_manager.deduct_balance(user, total_cost)
                            
                            # Update card balance if a card was selected
                            if selected_card:
                                selected_card.add_transaction(total_cost, 'payment', f'Ticket purchase: {train.name} x{count}')
                            
                            ticket_manager.issue_ticket(user, train, count)
                            wallet_manager.record_ticket_purchase(user, total_cost, train.name, count)
                        else:
                            print("Insufficient balance for this purchase.")
                            print(f"Required: {total_cost}, Available: {user.wallet}")
                            add_funds = input("Would you like to add funds? (y/n): ").strip().lower()
                            if add_funds == 'y':
                                wallet_manager.add_funds_prompt(user)
                            input("Press Enter to continue...")
                    except ValueError:
                        print("Invalid number.")
                        input("Press Enter to continue...")
                else:
                    print(f"Insufficient balance. Required: {train.price}, Available: {user.wallet}")
                    add_funds = input("Would you like to add funds? (y/n): ").strip().lower()
                    if add_funds == 'y':
                        wallet_manager.add_funds_prompt(user)
                    input("Press Enter to continue...")
        elif choice == "2":
            user_manager.edit_user_info(user)
        elif choice == "3":
            card_management_flow(card_manager)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

def card_management_flow(card_manager):
    """Handle card management operations"""
    while True:
        # clear_screen()
        print_sep("Card Management")
        # print("=== Card Management ===")
        print("1. View Saved Cards")
        print("2. Add New Card")
        print("3. Remove Card")
        print("4. View Card Details & Transactions")
        print("5. Back to Purchase Panel")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            card_manager.show_cards()
        elif choice == "2":
            card_manager.add_card()
        elif choice == "3":
            card_manager.remove_card()
        elif choice == "4":
            card_manager.view_card_details()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

# if __name__ == "__main__":
#     start_panel()