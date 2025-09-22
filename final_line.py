
class Line:
    def __init__(self, train):
        self.lines = {}
        self.train = train

    def creating(self):
        while True:
            try:

                while True:
                    self.name = safe_input("Line name:(Enter '0' to go back to employee panel ) ").strip()
                    if self.name == "0":
                        return
                    else:
                        break

                while True:
                    self.origin = safe_input("Origin: ")
                    if self.origin == "0":
                        return
                    else:
                        break

                while True:
                    try:
                        self.destination = safe_input("Destination: ")
                        if self.destination.lower() == self.origin.lower():
                            raise ValueError(
                                "'Destination' cannot be the same as 'Origin'")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        while True:
                            user_input3 = input(
                                "Enter '0' to go back to Employee Panel or '1' to try again: ")
                            if user_input3 == "1":
                                break
                            elif user_input3 == "0":
                                return
                            else:
                                print("Invalid option.")
                while True:
                    try:
                        self.stations_number = safe_input(
                            "Number of stations: ").strip()
                        if not self.stations_number.isdecimal():
                            raise ValueError(
                                "Number of stations must be a whole number equal or greater than zero.")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        while True:
                            user_input4 = input(
                                "Enter '0' to go back to Employee Panel or '1' to try again: ")
                            if user_input4 == "1":
                                break
                            elif user_input4 == "0":
                                return
                            else:
                                print("Invalid option.")

                if int(self.stations_number) == 0:
                    self.station_names = None
                else:
                    while True:
                        try:

                            self.station_names = input(
                                f"Please enter names of stations and use space to separate them\n***For names with more than one part please use '_': ").strip().title().split()
                            if len(self.station_names) != int(self.stations_number):
                                raise ValueError(
                                    f"Expected {int(self.stations_number)} station names but recieved {len(self.station_names)}")
                            elif len(set(self.station_names)) < len(self.station_names):
                                raise ValueError(
                                    "Name of stations cannot be repetetive")
                            for station in self.station_names:
                                if station == self.origin.title() or station == self.destination.title():
                                    raise ValueError(
                                        "Station name cannot be the same as 'Origin' or 'Destination'.")
                            else:
                                break
                        except ValueError as e:
                            print(e)
                            while True:
                                user_input5 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input5 == "1":
                                    break
                                elif user_input5 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                if self.name.title() not in self.lines:
                    self.lines[self.name.title()] = {"Origin": self.origin.title(), "Destination": self.destination.title(),
                                                     "Number of stations": self.stations_number, "Stations": self.station_names}
                    print(
                        f"\n***** '{self.name}' has been successfully added *****\n")
                    while True:
                        user_input6 = input(
                            "Enter '0' to go back to Employee Panel or '1' to add another line: ").strip()
                        if user_input6 == "1":
                            break
                        elif user_input6 == "0":
                            return
                        else:
                            print("Invalid option.")

                else:
                    raise ValueError(
                        f"A line named '{self.name.strip()}' already exists. Line names cannot be repetetive.")
            except ValueError as e:
                print(e)
                while True:
                    user_input7 = input(
                        "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                    if user_input7 == "1":
                        break
                    elif user_input7 == "0":
                        return
                    else:
                        print("Invalid option.")

    def editing(self):
        while True:
            try:
                if len(self.lines) == 0:
                    print("No line found to edit.")
                    break
                user_input = input(
                    "Enter the name of the line you would like to edit: ").strip().title()
                if user_input in self.lines:
                    print(f"{user_input} : {self.lines[user_input]}")
                    while True:
                        try:
                            user_input2 = input(
                                "What feature would you like to edit?(Origin, Destination, Number of stations, Stations): ").strip().lower()
                            reference = ["origin", "destination",
                                         "number of stations", "stations"]
                            if user_input2 in reference:
                                while True:
                                    try:
                                        user_input3 = input(
                                            f"Enter the new value for '{user_input2}': ").strip()
                                        if user_input3 != "":
                                            self.lines[user_input][user_input2] = user_input3
                                            print(
                                                f"\n*****{user_input2} of '{self.name}' has been successfully changed.*****\n")
                                            user_input0 = input(
                                                "Press 'Enter' to edit another feature or enter 'exit' to return to Employee Panel:\n>>>").strip().lower()
                                            if user_input0 == "exit":
                                                break
                                        else:
                                            raise ValueError(
                                                f"'{user_input2}' cannot be empty")
                                    except ValueError as e:
                                        print(e)
                                    user_input4 = input(
                                        "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
                                    if user_input4 == "exit":
                                        break
                            else:
                                raise ValueError(
                                    f"There is no feature named '{user_input2}'")
                        except ValueError as e:
                            print(e)
                        user_input5 = input(
                            "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
                        if user_input5 == "exit":
                            break
                else:
                    raise ValueError(
                        f"Line named '{user_input}' doesn't exist.")
            except ValueError as e:
                print(e)
            user_input6 = input(
                "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
            if user_input6 == "exit":
                break

    def removing(self):
        while True:
            try:
                if len(self.lines) == 0:
                    print("No line found to remove.")
                    break
                user_input = input(
                    "Enter the name of the line you would like to remove: ").strip().title()
                if user_input in self.lines:
                    self.lines.pop(user_input)
                    self.train.remove_trains_by_line(user_input)
                    print(
                        f"\n***** '{user_input}' and trains associated with it have been successfully removed *****\n")
                    while True:
                        user_input1 = input(
                            "Enter '0' to go back to Employee Panel or '1' to remove another line: ").strip()
                        if user_input1 == "1":
                            break
                        elif user_input1 == "0":
                            return
                        else:
                            print("Invalid option.")

                else:
                    raise ValueError(
                        f"There is no line named '{user_input}'")
            except ValueError as e:
                print(e)
                while True:
                    user_input2 = input(
                        "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                    if user_input2 == "1":
                        break
                    elif user_input2 == "0":
                        return
                    else:
                        print("Invalid option.")

    def viewing(self):
        if len(self.lines) == 0:
            print(f"\nNo line has been added yet")
        else:
            for key, value in self.lines.items():
                print(f"{key} : {value}")
        print("------------------------")
        while True:
            user_input0 = input(
                "Enter 0 to go back to Employee Panel: ").strip()
            if user_input0 == "0":
                break
            else:
                print("Invalid option.")
def safe_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Input must be non-empty. Please try again.")

