# ticket.py
import datetime

class TicketManager:
    def issue_ticket(self, user, train, count):
        train.capacity -= count
        filename = f"{user.username}_ticket.txt"
        with open(filename, "a") as f:
            f.write(f"Buyer: {user.name}\n")
            f.write(f"Train: {train.name}\n")
            f.write(f"Destination: {train.destination}\n")
            f.write(f"Tickets: {count}\n")
            f.write(f"Total Price: {train.price * count}\n")
            f.write(f"Time: {datetime.datetime.now()}\n")
            f.write("-" * 30 + "\n")
        print("Ticket issued successfully. Saved to file.")
        input("Press Enter to continue...")