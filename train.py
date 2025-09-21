# class Train:
#     def __init__(self, name, line, avg_speed, stop_times, quality, cost, seats, id):
#         self.name = name
#         self.line = line
#         self.avg_speed = avg_speed
#         self.stop_times = stop_times
#         self.quality = quality
#         self.cost = cost
#         self.seats = seats
#         self.id = id
 # train.py --> new version by group 3
class Train:
    def __init__(self, name, destination, capacity, price):
        self.name = name
        self.destination = destination
        self.capacity = capacity
        self.price = price

class TrainManager:
    [
        Train("Express 101", "Tehran", 50, 100000),
        Train("Shatab 202", "Mashhad", 30, 150000),
        Train("Raja 303", "Isfahan", 20, 120000),
    ]

    def show_trains(self):
        print("\n=== Available Trains ===")
        for i, t in enumerate(self.trains):
            status = "Capacity Full" if t.capacity <= 0 else f"{t.capacity} seats left"
            print(f"{i+1}. {t.name} -> {t.destination} | Price: {t.price} | {status}")

    def select_train(self):
        try:
            choice = input("Select train number (or 'back' to cancel): ").strip()
            if choice.lower() == 'back':
                return None
            
            idx = int(choice) - 1
            train = self.trains[idx]
            if train.capacity > 0:
                return train
            else:
                print("This train is full.")
                input("Press Enter to continue...")
                return None
        except (IndexError, ValueError):
            print("Invalid selection.")
            input("Press Enter to continue...")
            return None   