# ticket.py
import datetime
from final_employee_panel import train

class TicketManager:   
    def issue_ticket(self, user, tr, count):
        # Check if the train ID exists in the train system
        if tr.id in train.trains:
            train.trains[tr.id]["filled"] += count
        else:
            # If train ID doesn't exist in the main system, just record the ticket
            print(f"Warning: Train ID {tr.id} not found in main system. Ticket recorded anyway.")
        
        filename = f"{user.username}_ticket.txt"
        with open(filename, "a") as f:
            f.write(f"Buyer: {user.name}\n")
            f.write(f"Train: {tr.name}\n")
            f.write(f"[Origin]: {tr.origin}\n")
            f.write(f"Destination: {tr.destination}\n")
            f.write(f"Tickets: {count}\n")
            f.write(f"Total Price: {tr.price * count}\n")
            f.write(f"Time: {datetime.datetime.now()}\n")
            f.write("-" * 30 + "\n")
        print("Ticket issued successfully. Saved to file.")
        input("Press Enter to continue... ") 
        