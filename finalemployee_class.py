from line import Line
from train import Train

class Employee:
    lines = []
    trains = []

    def __init__(self, name, lastname, email, username, password): 
        self.name = name
        self.lastname = lastname
        self.email = email 
        self.username = username
        self.password = password

    @staticmethod
    def safe_input(prompt):
        while True:
            value = input(prompt).strip()
            if value != "":
                return value
            else:
                print("Input must be non-empty. Please try again.")

    @staticmethod
    def add_line():
        while True:
            line_name = Employee.safe_input("Enter line name (or type '0' to return): ")
            if line_name == "0":
                return
            if any(line.name == line_name for line in Employee.lines):
                print("This line name already exists, please try again.")
            else:
                break

        origin = Employee.safe_input("Origin (or type '0' to return): ")
        if origin == "0":
            return

        while True:
            destination = Employee.safe_input("Destination (or type '0' to return): ")
            if destination == "0":
                return
            if destination.lower() == origin.lower():
                print("Destination cannot be the same as origin.")
            else:
                break

        while True:
            station_count = Employee.safe_input("Number of stations (or type '0' to return): ")
            if station_count == "0":
                return
            if not station_count.isdecimal():
                print("Number of stations must be a non-negative integer.")
            else:
                station_count = int(station_count)
                break

        while True:
            stations = input(
                f"Enter {station_count} stations (space separated, '_' for multi-part names): "
            ).strip().title().split()

            if station_count != 0 and len(stations) == 0:
                print("Station list cannot be empty.")
            elif len(stations) != station_count:
                print(f"Expected {station_count} stations but got {len(stations)}.")
            elif len(set(stations)) < len(stations):
                print("Stations cannot have duplicate names.")
            elif origin.title() in stations or destination.title() in stations:
                print("Origin and Destination cannot be in stations list.")
            else:
                break

        new_line = Line(line_name, origin, destination, station_count, stations)
        Employee.lines.append(new_line)
        print("Line added successfully.")

    @staticmethod
    def edit_line():
        line_name = Employee.safe_input("Enter line name to edit (or type '0' to return): ")
        if line_name == "0":
            return

        found_line = None
        for line in Employee.lines:
            if line.name == line_name:
                found_line = line
                break

        if not found_line:
            print("Line not found.")
            return

        print(f"\nCurrent line info:")
        print(f"Name: {found_line.name}")
        print(f"Origin: {found_line.origin}")
        print(f"Destination: {found_line.destination}")
        print(f"Stations: {found_line.stations}")
        print(f"Station Count: {found_line.station_count}\n")

        choice = Employee.safe_input(
            "What do you want to update?\n"
            "1) Line name\n"
            "2) Origin\n"
            "3) Destination\n"
            "4) Stations list\n"
            "0) Return\n"
            "Enter choice: "
        )

        match choice:
            case "1":
                new_name = Employee.safe_input("Enter new line name: ")
                found_line.name = new_name
            case "2":
                new_origin = Employee.safe_input("Enter new origin: ")
                found_line.origin = new_origin
            case "3":
                new_dest = Employee.safe_input("Enter new destination: ")
                found_line.destination = new_dest
            case "4":
                new_stations = input("Enter new stations (space separated): ").strip().title().split()
                found_line.stations = new_stations
                found_line.station_count = len(new_stations)
            case "0":
                return
            case _:
                print("Invalid choice.")

        print("Line updated successfully.")
    @staticmethod
    def delete_line():
        line_name = Employee.safe_input("Enter line name to delete (or type '0' to return): ")
        if line_name == "0":
            return

        found_line = None
        for line in Employee.lines:
            if line.name == line_name:
                found_line = line
                break

        if not found_line:
            print("Line not found.")
            return
        Employee.lines.remove(found_line)
        print(f"Line '{line_name}' deleted successfully.")

    @staticmethod
    def line_info():
        if not Employee.lines:   # if no line is registered
            print("No lines have been registered yet.")
            return

        print("Registered lines information:")
        for line in Employee.lines:
            print("--------------------------")
            print(f"Line name: {line.name}")
            print(f"Origin: {line.origin}")
            print(f"Destination: {line.destination}")
            print(f"Station count: {line.station_count}")
            print(f"Stations: {', '.join(line.stations)}")

        # return option
        input("Press Enter to return to the employee menu")
        return




    @staticmethod
    def add_train():
        name = Employee.safe_input("Train name(or type 0 to return): ")
        if name == "0": return

        line = Employee.safe_input("Train line: ")

        avg_speed = Employee.safe_input("Average speed: ")
        if not avg_speed.isdigit():
            print("Invalid average speed.")
            return
        avg_speed = int(avg_speed)

        stop_times = {}
        count_str = Employee.safe_input("Number of stations: ")
    
        if not count_str.isdigit():
            print("Invalid number of stations.")
            return
        count = int(count_str)

        for i in range(count):
            station = Employee.safe_input(f"Station {i+1} name: ")
            if station == "0": return

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
        if not cost.isdigit():
            print("Invalid cost.")
            return
        cost = int(cost)

        seats = Employee.safe_input("Available seats: ")
        if not seats.isdigit():
            print("Invalid number of seats.")
            return
        seats = int(seats)

        id = Employee.safe_input("Train ID: ")
    

        for tr in Employee.trains:
            if tr.id == id:
                print("Train ID must be unique!")
                return

        new_train = Train(name, line, avg_speed, stop_times, quality, cost, seats, id)
        Employee.trains.append(new_train)
        print("Train added successfully.")


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
                    case "1":
                        tr.name = Employee.safe_input("Enter new name: ")
                    case "2":
                        tr.line = Employee.safe_input("Enter new line: ")
                    case "3":
                        speed = Employee.safe_input("Enter new average speed: ")
                        if speed.isdigit():
                            tr.avg_speed = int(speed)
                        else:
                            print("Invalid speed.")
                            return
                    case "4":
                        stop_times = {}
                        count_str = Employee.safe_input("Number of stations: ")
                        if not count_str.isdigit():
                            print("Invalid number of stations.")
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

                        tr.stop_times = stop_times
                    case "5":
                        tr.quality = Employee.safe_input("Enter new quality: ")
                    case "6":
                        cost = Employee.safe_input("Enter new cost: ")
                        if cost.isdigit():
                            tr.cost = int(cost)
                        else:
                            print("Invalid cost.")
                            return
                    case "7":
                        seats = Employee.safe_input("Enter new seats: ")
                        if seats.isdigit():
                            tr.seats = int(seats)
                        else:
                            print("Invalid number of seats.")
                            return
                    case _:
                        print("Invalid option.")
                        return
                print("Train updated successfully.")
                return

        print("Train not found.")


    @staticmethod
    def delete_train():
        id = Employee.safe_input("Enter the train ID to delete or type 'back' to return: ")
        if id == "back": return

        for tr in Employee.trains:
            if tr.id == id:
                Employee.trains.remove(tr)
                print(f"Train with ID '{id}' deleted successfully.")
                return

        print("Train not found.")


    @staticmethod
    def train_info():
        if not Employee.trains:
            print("No trains available.")
            return

        print("\nList of Trains:")
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
                print(f"  {station}: {duration} min")
            print("------------------------")
