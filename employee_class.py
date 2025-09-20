from train import Train
class Employee:
    trains = []
    def __init__(self, name, lastname, email, username, password): 
        self.name = name
        self.lastname = lastname
        self.email = email 
        self.username = username
        self.password = password
    

    def safe_input(prompt):
        while True:
            value = input(prompt).strip()
            if value.lower() == "back":
                return "back"
            if value != "":
                return value
            else:
                print("input must be unempty.please try again")

    @staticmethod
    def add_train():
        name = Employee.safe_input("Train name: ")
        if name == "back": return

        line = Employee.safe_input("Train line: ")
        if line == "back": return

        avg_speed = Employee.safe_input("Average speed: ")
        if avg_speed == "back": return

        stop_times = {}
        count_str = Employee.safe_input("Number of stations: ")
        if count_str == "back": return
        if not count_str.isdigit():
            print(" Invalid number of stations.")
            return
        count = int(count_str)

        for i in range(count):
            station = Employee.safe_input(f"Station {i+1} name: ")
            if station == "back": return

            while True:
                duration = Employee.safe_input(f"Stop time at {station}: ")
                if duration == "back": return
                if duration.isdigit():
                    stop_times[station] = int(duration)
                    break
                else:
                    print("Invalid number, please enter digits only.")

        quality = Employee.safe_input("Quality grade: ")
        if quality == "back": return

        cost = Employee.safe_input("Ticket cost: ")
        if cost == "back": return

        seats = Employee.safe_input("Available seats: ")
        if seats == "back": return

        id = Employee.safe_input("Train ID: ")
        if id == "back": return

        for tr in Employee.trains:
            if tr.id == id:
                print("Train ID must be unique!")
                return

        new_train = Train(name, line, avg_speed, stop_times, quality, cost, seats, id)
        Employee.trains.append(new_train)
        print("Train added successfully!")

    @staticmethod
    def edit_train():
        id = Employee.safe_input("Enter the train ID to edit or type 'back' to return: ")
        if id == "back": return

        for tr in Employee.trains:
            if tr.id == id:
                choice = Employee.safe_input(
                    "What do you want to change?\n"
                    "1. Name\n2. Line\n3. Avg speed\n4. Stop times\n"
                    "5. Quality\n6. Cost\n7. Seats\n: "
                )
                if choice == "back": return




                match choice:
                    case "1" | "name":
                        tr.name = Employee.safe_input("Enter new name: ")
                    case "2" | "line":
                        tr.line = Employee.safe_input("Enter new line: ")
                    case "3" | "avg_speed":
                        tr.avg_speed = Employee.safe_input("Enter new average speed: ")
                    case "4" | "stop_times":
                        stop_times = {}
                        count_str = Employee.safe_input("Number of stations: ")
                        if not count_str.isdigit():
                            print(" Invalid number of stations.")
                            return
                        count = int(count_str)

                        for i in range(count):
                            station = Employee.safe_input(f"Station {i+1} name: ")
                            if station == "back": return

                            while True:
                                duration = Employee.safe_input(f"Stop time at {station}: ")
                                if duration == "back": return
                                if duration.isdigit():
                                    stop_times[station] = int(duration)
                                    break
                                else:
                                    print(" Invalid number, please enter digits only.")

                        tr.stop_times = stop_times
                    case "5" | "quality":
                        tr.quality = Employee.safe_input("Enter new quality: ")
                    case "6" | "cost":
                        tr.cost = Employee.safe_input("Enter new cost: ")
                    case "7" | "seats":
                        tr.seats = Employee.safe_input("Enter new seats: ")
                    case _:
                        print(" Invalid option.")
                print("Train updated successfully!")
                return
        print("Train not found!")
    @staticmethod
    def delete_train():
        id = Employee.safe_input("Enter the train ID to delete or type 'back' to return: ")
        if id == "back":
            return

        for tr in Employee.trains:
            if tr.id == id:
                Employee.trains.remove(tr)
                print(f" Train with ID '{id}' deleted successfully!")
                return

        print("Train not found.")
    @staticmethod
    def trains_info():
        if not Employee.trains:
            print("No trains available.")
            return

        print("\n List of Trains:")
        for tr in Employee.trains:
            print(f"ID: {tr.id}")
            print(f"Name: {tr.name}")
            print(f"Line: {tr.line}")
            print(f"Average Speed: {tr.avg_speed}")
            print(f"Quality: {tr.quality}")
            print(f"Cost: {tr.cost}")
            print(f"Seats: {tr.seats}")
            print("Stop Times:")
            for station, duration in tr.stop_times.items():
                print(f" {station}: {duration} min\n")


                 
               
                   
             