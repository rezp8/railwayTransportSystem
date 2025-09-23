# main.py
from user import UserManager, CardManager
from train import TrainManager
from ticket import TicketManager
from wallet import WalletManager
from utils import clear_screen

# def start_panel():
#     while True:
#         clear_screen()
#         print("=== Train Ticket System ===")
#         print("1. Full Admin")
#         print("2. Train Employee")
#         print("3. Regular User")
#         print("4. Exit")
#         choice = input("Choose an option: ").strip()

#         if choice == "3":
#             regular_user_flow()
#         elif choice == "4":
#             print("Exiting...")
#             break
#         else:
#             print("Only Regular User is supported in this version.")
#             input("Press Enter to continue...")

def regular_user_flow():
    user_manager = UserManager()
    train_manager = TrainManager()
    ticket_manager = TicketManager()
    wallet_manager = WalletManager()

    while True:
        clear_screen()
        print("=== Regular User Panel ===")
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
        clear_screen()
        print("=== Purchase Panel ===")
        print("1. Buy Ticket")
        print("2. Edit User Information")
        print("3. Manage Cards")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            train_manager.show_trains()
            train = train_manager.select_train()
            if train:
                # Store initial balance to check if payment was completed
                initial_balance = user.wallet
                wallet_manager.add_funds_prompt(user)
                
                # Check if user actually completed payment (balance increased)
                if user.wallet > initial_balance:
                    if wallet_manager.has_sufficient_balance(user, train.price):
                        count_input = input("How many tickets? (or 'back' to cancel): ").strip()
                        if count_input.lower() == 'back':
                            continue
                        
                        try:
                            count = int(count_input)
                            total_cost = train.price * count
                            if wallet_manager.has_sufficient_balance(user, total_cost):
                                wallet_manager.deduct_balance(user, total_cost)
                                ticket_manager.issue_ticket(user, train, count)
                                wallet_manager.record_ticket_purchase(user, total_cost, train.name, count)
                            else:
                                print("Low Balance.")
                                input("Press Enter to continue...")
                        except ValueError:
                            print("Invalid number.")
                            input("Press Enter to continue...")
                    else:
                        print("Insufficient balance for this train.")
                        input("Press Enter to continue...")
                # If balance didn't increase, user cancelled the payment process
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
        clear_screen()
        print("=== Card Management ===")
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