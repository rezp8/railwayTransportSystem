# self.trains[self.id] = {
#                         "Name": self.name, 
#                         "Line": self.moving_line.title(), 
#                         "Average speed": self.avg_speed,
#                         "Stop duration per station": self.stop_per_station, 
#                         "Quality": self.quality, 
#                         "Ticket price": self.ticket_price,
#                         "Capacity": self.capacity,
#                         "empty capacity": int(self.capacity)
# }
class Train:
    def __init__(self, name, destination, capacity, price, id):
        self.name = name
        self.destination = destination
        self.capacity = capacity
        self.price = price
        self.id = id

 #train.py --> new version by group 3 

class TrainManager:

    def show_trains(self):
        from final_employee_panel import train
        trains=[] 
        for i in train.trains:
            trains.append(Train(
                train.trains[i]["Name"],
                train.line.lines[train.trains[i]["Line"]]["destination"], 
                int(train.trains[i]["Capacity"])-train.trains[i]["filled"], 
                int(train.trains[i]["Ticket price"]),
                i
            ))
        print("\n=== Available Trains ===")
        for i, t in enumerate(trains):
            status = "Capacity Full" if t.capacity <= 0 else f"{t.capacity} seats left"
            print(f"{i+1}. {t.name} -> {t.destination} | Price: {t.price} | {status}")

    def select_train(self): 
        from final_employee_panel import train
        trains=[] 
        for i in train.trains:
            trains.append(Train(
                train.trains[i]["Name"],
                train.line.lines[train.trains[i]["Line"]]["destination"], 
                int(train.trains[i]["Capacity"])-train.trains[i]["filled"],  
                int(train.trains[i]["Ticket price"]),
                i
            ))
        try:
            if len(trains)==0:
                print("There are no available trains")
                input("Press Enter to continue...")
                return None
            choice = input("Select train number (or 'back' to cancel): ").strip()
            if choice.lower() == 'back':
                return None
            
            idx = int(choice) - 1
            train = trains[idx]
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