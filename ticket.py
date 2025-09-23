# ticket.py
import datetime
from final_employee_panel import train

class TicketManager:   
    def issue_ticket(self, user, tr, count):
        train.trains[tr.id]["filled"] += count
        filename = f"{user.username}_ticket.txt"
        with open(filename, "a") as f:
            f.write(f"Buyer: {user.name}\n")
            f.write(f"Train: {tr.name}\n")
            f.write(f"Destination: {tr.origin}\n")
            f.write(f"Destination: {tr.destination}\n")
            f.write(f"Tickets: {count}\n")
            f.write(f"Total Price: {tr.price * count}\n")
            f.write(f"Time: {datetime.datetime.now()}\n")
            f.write("-" * 30 + "\n")
        print("Ticket issued successfully. Saved to file.")
        input("Press Enter to continue... ") 
        