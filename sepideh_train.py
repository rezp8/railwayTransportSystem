from sepideh_line import Line


class Train:
    def __init__(self, line):
        self.trains = {}
        self.line = line

    def creating(self):
        while True:
            try:
                while True:
                    try:
                        self.name = input("Train name: ").strip()
                        if self.name == "":
                            raise ValueError("Train name cannot be empty.")
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
                        print(list(self.line.lines.keys()))
                        self.moving_line = input(
                            "Please choose 'Train Line' from the list above: ").strip().title()
                        if self.moving_line == "":
                            raise ValueError("Train line cannot be empty.")
                        elif self.moving_line not in list(self.line.lines.keys()):
                            raise ValueError(
                                f"Line named '{self.moving_line}' doesn't exist.")
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
                        self.avg_speed = input("Average speed: ").strip()
                        if self.avg_speed == "":
                            raise ValueError("Average speed cannot be empty")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input13 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input13 == "exit":
                            return

                if self.line.lines[self.moving_line]["Number of stations"] == "0":
                    self.stop_per_station = None
                else:
                    while True:
                        try:
                            print(self.line.lines[self.moving_line]
                                  ["Stations"])
                            self.stop_per_station = input(
                                f"The list above are the stations defined for line '{self.moving_line}'. Please enter the stop duration for each station and use space to separate them: ").strip().split()
                            if len(self.stop_per_station) == 0:
                                raise ValueError(
                                    f"Expected {int(self.line.lines[self.moving_line]["Number of stations"])} but received {len(self.stop_per_station)}")
                            elif len(self.stop_per_station) != int(self.line.stations_number):
                                raise ValueError(
                                    f"Expected {int(self.line.lines[self.moving_line]["Number of stations"])} but recieved {len(self.stop_per_station)}")
                            # for number in self.stop_per_station:
                            #     if number.isdecim

                            else:
                                break
                        except ValueError as e:
                            print(e)
                            user_input14 = input(
                                "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                            if user_input14 == "exit":
                                return

                while True:
                    try:
                        quality_reference = ["3stars", "2stars", "1star"]
                        print(quality_reference)
                        self.quality = input(
                            "Please choose 'Train Quality' from the list above: ").strip().lower()
                        if self.quality == "":
                            raise ValueError("Quality cannot be empty.")
                        elif self.quality not in quality_reference:
                            raise ValueError(
                                f"Quality '{self.quality}' has not been defined.")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input15 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input15 == "exit":
                            return

                while True:
                    try:
                        self.ticket_price = input("Ticket price: ").strip()
                        if self.ticket_price == "":
                            raise ValueError("Ticket price cannot be empty.")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input16 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input16 == "exit":
                            return

                while True:
                    try:
                        self.capacity = input("Capacity: ").strip()
                        if self.capacity == "":
                            raise ValueError("Capacity cannot be empty.")
                        elif not self.capacity.isdecimal():
                            raise ValueError(
                                "Capacity must be whole number greater than zero")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input17 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input17 == "exit":
                            return

                while True:
                    try:
                        self.id = input("Train ID: ").strip()
                        if self.id == "":
                            raise ValueError("Train ID cannot be empty.")
                        else:
                            break
                    except ValueError as e:
                        print(e)
                        user_input18 = input(
                            "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
                        if user_input18 == "exit":
                            return

                if self.id.title() not in self.trains:
                    self.trains[self.id.title()] = {"Name": self.name.title(), "Line": self.moving_line.title(), "Average speed": f"{self.avg_speed} km",
                                                    "Stop duration per station": self.stop_per_station, "Quality": self.quality, "Ticket price": f"{self.ticket_price} Rial",
                                                    "Capacity": f"{self.capacity} passengers"}

                    print(
                        f"\n***** Train with ID '{self.id}' has been successfully added *****\n")
                    break
                    # user_input3 = input(
                    #     "Press 'Enter' to add another line or enter 'exit' to return to Employee Panel: ").lower()
                    # if user_input3 == "exit":
                    #     exit()
                    # else:
                    #     continue
                else:
                    raise ValueError(
                        f"A train with ID '{self.name}' already exists.")
            except ValueError as e:
                print(e)
                user_input19 = input(
                    "Enter 'exit' to return to Employee Panel or press enter to try again: ").strip().lower()
                if user_input19 == "exit":
                    break

    def editing(self):
        while True:
            try:
                user_input = input(
                    "Enter the ID of the train you would like to edit: ").strip().title()
                if user_input in self.trains:
                    print(f"{user_input} : {self.trains[user_input]}")
                    while True:
                        try:
                            user_input2 = input(
                                "What feature would you like to edit?(Name, Line, Average speed, Stop per station, Quality, Ticket price, Capacity): ").strip().lower()
                            reference = ["name", "line", "average speed", "stop per station",
                                         "quality ", "ticket price", "capacity"]
                            if user_input2 in reference:
                                while True:
                                    try:
                                        user_input3 = input(
                                            f"Enter the new value for '{user_input2}': ")
                                        if user_input3 != "":
                                            self.trains[user_input][user_input2] = user_input3
                                            print(
                                                f"\n*****{user_input2} of train '{self.id}' has been successfully changed.*****\n")
                                            return
                                        else:
                                            raise ValueError(
                                                f"'{user_input2}' cannot be empty.")
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
                        f"Train with ID '{user_input}' doesn't exist.")
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
                    "Enter the ID of the train you would like to remove: ").strip().title()
                if user_input in self.trains:
                    self.trains.pop(user_input)
                    print(
                        f"\n***** Train '{self.id}' has been successfully removed *****\n")
                    break
                else:
                    raise ValueError(f"There is no line named '{user_input}'")
            except ValueError as e:
                print(e)
            user_input2 = input(
                "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
            if user_input2 == "exit":
                break

    def viewing(self):
        if len(self.trains) == 0:
            print("No train has been added yet")
        else:
            for key, value in self.trains.items():
                print(f"{key} : {value}")

    def remove_trains_by_line(self, line_name):
        filtered_trains = {}
        for key, value in self.trains.items():
            if value["Line"] != line_name:
                filtered_trains[key] = value

        self.trains = filtered_trains
