class Line:
    def __init__(self, train):
        self.lines = {}
        self.train = train

    def creating(self):
        while True:
            try:
                while True:
                    try:
                        self.name = input("Line name: ").strip()
                        if self.name == "":
                            raise ValueError("Line name cannot be empty")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input11 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input11 == "exit":
                            return

                while True:
                    try:
                        self.origin = input("Origin: ").strip()
                        if self.origin == "":
                            raise ValueError("Origin cannot be empty")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input12 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input12 == "exit":
                            return
                while True:
                    try:
                        self.destination = input("Destination: ").strip()
                        if self.destination == "":
                            raise ValueError("Destination cannot be empty")
                        elif self.destination.lower() == self.origin.lower():
                            raise ValueError(
                                "'Destination' cannot be the same as 'Origin'")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input13 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input13 == "exit":
                            return
                while True:
                    try:
                        self.stations_number = input(
                            "Number of stations: ").strip()
                        if self.stations_number == "":
                            raise ValueError(
                                "Number of stations cannot be empty")
                        elif not self.stations_number.isdecimal():
                            raise ValueError(
                                "Number of stations must be a whole number equal or greater than zero.")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input14 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input14 == "exit":
                            return

                if int(self.stations_number) == 0:
                    self.station_names = None
                else:
                    while True:
                        try:

                            self.station_names = input(
                                f"Please enter names of stations and use space to separate them\n***For names with more than one part please use '_': ").strip().title().split()

                            if int(self.stations_number) != 0 and len(self.station_names) == 0:
                                raise ValueError(
                                    f"Expected {int(self.stations_number)} but recieved {len(self.station_names)}")
                            elif len(self.station_names) != int(self.stations_number):
                                raise ValueError(
                                    f"Expected {int(self.stations_number)} but recieved {len(self.station_names)}")
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
                            user_input15 = input(
                                "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                            if user_input15 == "exit":
                                return

                if self.name.title() not in self.lines:
                    self.lines[self.name.title()] = {"Origin": self.origin.title(), "Destination": self.destination.title(),
                                                     "Number of stations": self.stations_number, "Stations": self.station_names}
                    print(
                        f"\n***** '{self.name}' has been successfully added *****\n")
                    user_input0 = input(
                        "Press 'Enter' to add another line or enter 'exit' to return to Employee Panel:\n>>>").strip().lower()
                    if user_input0 == "exit":
                        return

                else:
                    raise ValueError(
                        f"A line named '{self.name.strip().title()}' already exists.")
            except ValueError as e:
                print(e)
                user_input = input(
                    "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                if user_input == "exit":
                    break

    def editing(self):
        while True:
            try:
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
                                                "Press 'Enter' to add another line or enter 'exit' to return to Employee Panel:\n>>>").strip().lower()
                                            if user_input0 == "exit":
                                                return
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
                user_input = input(
                    "Enter the name of the line you would like to remove: ").strip().title()
                if user_input in self.lines:
                    self.lines.pop(user_input)
                    self.train.remove_trains_by_line(user_input)
                    print(
                        f"\n***** '{user_input}' and trains associated with it have been successfully removed *****\n")
                    user_input0 = input(
                        "Press 'Enter' to remove another line or enter 'exit' to return to Employee Panel:\n>>>").strip().lower()
                    if user_input0 == "exit":
                        return
                else:
                    raise ValueError(f"There is no line named '{user_input}'")
            except ValueError as e:
                print(e)
                user_input2 = input(
                    "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
                if user_input2 == "exit":
                    break

    def viewing(self):
        if len(self.lines) == 0:
            print("No line has been added yet")
        else:
            for key, value in self.lines.items():
                print(f"{key} : {value}")
