from final_line import Line


class Train:
    def __init__(self, line):
        self.trains = {}
        self.line = line

    def creating(self):
        if len(self.line.lines) == 0:
            print(
                f"\nAdding train is not possible: no line defined yet.\nPlease add a line first by choosing option 1 from Employee Panel.")
            while True:
                user_input0 = input(
                    "Enter 0 to go to Employee Panel: ").strip()
                if user_input0 == "0":
                    break
                else:
                    print("Invalid option.")

        else:
            while True:
                try:
                    while True:
                        try:
                            self.name = input("Train name: ").strip().title()
                            if self.name == "":
                                raise ValueError("Name cannot be empty.")
                            else:
                                break
                        except ValueError as e:
                            print(e)
                            while True:
                                user_input1 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input1 == "1":
                                    break
                                elif user_input1 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                    while True:
                        try:
                            print(sorted(list(self.line.lines.keys())))
                            self.moving_line = input(
                                "Please choose a line from the list above: ").strip().title()
                            if self.moving_line == "":
                                raise ValueError("Line cannot be empty.")
                            elif self.moving_line not in list(self.line.lines.keys()):
                                raise ValueError(
                                    f"Line named '{self.moving_line}' doesn't exist.")
                            else:
                                break
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

                    while True:
                        try:
                            self.avg_speed = input("Average speed: ").strip()
                            if self.avg_speed == "":
                                raise ValueError(
                                    "Average speed cannot be empty")
                            else:
                                break
                        except ValueError as e:
                            print(e)
                            while True:
                                user_input3 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input3 == "1":
                                    break
                                elif user_input3 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                    if self.line.lines[self.moving_line]["Number of stations"] == "0":
                        self.stop_per_station = None
                    else:
                        while True:
                            try:
                                print(self.line.lines[self.moving_line]
                                      ["Stations"])
                                self.stop_per_station = input(
                                    f"Please enter the stop duration for each station showed on the list above(use space to separate them): ").strip().split()
                                if len(self.stop_per_station) != int(self.line.lines[self.moving_line]["Number of stations"]):
                                    raise ValueError(
                                        f"Expected {int(self.line.lines[self.moving_line]["Number of stations"])} stop duration but recieved {len(self.stop_per_station)}")
                                # for number in self.stop_per_station:
                                #     if number.isdecim

                                else:
                                    break
                            except ValueError as e:
                                print(e)
                                while True:
                                    user_input4 = input(
                                        "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                    if user_input4 == "1":
                                        break
                                    elif user_input4 == "0":
                                        return
                                    else:
                                        print("Invalid option.")

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
                            while True:
                                user_input5 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input5 == "1":
                                    break
                                elif user_input5 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                    while True:
                        try:
                            self.ticket_price = input("Ticket price: ").strip()
                            if self.ticket_price == "":
                                raise ValueError(
                                    "Ticket price cannot be empty.")
                            else:
                                break
                        except ValueError as e:
                            print(e)
                            while True:
                                user_input6 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input6 == "1":
                                    break
                                elif user_input6 == "0":
                                    return
                                else:
                                    print("Invalid option.")

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
                            while True:
                                user_input7 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input7 == "1":
                                    break
                                elif user_input7 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                    while True:
                        try:
                            self.id = input("Train ID: ").title().strip()
                            if self.id == "":
                                raise ValueError("Train ID cannot be empty.")
                            else:
                                break
                        except ValueError as e:
                            print(e)
                            while True:
                                user_input8 = input(
                                    "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                                if user_input8 == "1":
                                    break
                                elif user_input8 == "0":
                                    return
                                else:
                                    print("Invalid option.")

                    if self.id not in self.trains:
                        self.trains[self.id] = {"Name": self.name, "Line": self.moving_line.title(), "Average speed": self.avg_speed,
                                                "Stop duration per station": self.stop_per_station, "Quality": self.quality, "Ticket price": self.ticket_price,
                                                "Capacity": self.capacity}

                        print(
                            f"\n***** Train with ID '{self.id}' has been successfully added *****\n")
                        while True:
                            user_input9 = input(
                                "Enter '0' to go back to Employee Panel or '1' to add another line: ").strip()
                            if user_input9 == "1":
                                break
                            elif user_input9 == "0":
                                return
                            else:
                                print("Invalid option.")
                    else:
                        raise ValueError(
                            f"A train with ID '{self.id}' already exists. Train IDs cannot be repetetive.")
                except ValueError as e:
                    print(e)
                    while True:
                        user_input10 = input(
                            "Enter '0' to go back to Employee Panel or '1' to try again: ").strip()
                        if user_input10 == "1":
                            break
                        elif user_input10 == "0":
                            return
                        else:
                            print("Invalid option.")

    def editing(self):
        while True:
            try:
                if len(self.trains) == 0:
                    print("No train found to edit.")
                    break
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
                if len(self.trains) == 0:
                    print("No train found to remove.")
                    break
                user_input = input(
                    "Enter the ID of the train you would like to remove: ").strip().title()
                if user_input in self.trains:
                    self.trains.pop(user_input)
                    print(
                        f"\n***** Train '{self.id}' has been successfully removed *****\n")
                    while True:
                        user_input1 = input(
                            "Enter '0' to go back to Employee Panel or '1' to remove another train: ").strip()
                        if user_input1 == "1":
                            break
                        elif user_input1 == "0":
                            return
                        else:
                            print("Invalid option.")

                else:
                    raise ValueError(
                        f"Train with ID '{user_input}' doesn't exist.")
            except ValueError as e:
                print(e)
                while True:
                    user_input1 = input(
                        "Enter '0' to go back to Employee Panel or '1' to remove another train: ").strip()
                    if user_input1 == "1":
                        break
                    elif user_input1 == "0":
                        return
                    else:
                        print("Invalid option.")

    def viewing(self):
        if len(self.trains) == 0:
            print("No train has been added yet")
        else:
            for key, value in self.trains.items():
                print(f"{key} : {value}")
        print("------------------------")
        while True:
            user_input0 = input(
                "Enter 0 to go back to Employee Panel: ").strip()
            if user_input0 == "0":
                break
            else:
                print("Invalid option.")

    def remove_trains_by_line(self, line_name):
        filtered_trains = {}
        for key, value in self.trains.items():
            if value["Line"] != line_name:
                filtered_trains[key] = value

        self.trains = filtered_trains


# self.trains[self.id] = {"Name": self.name, "Line": self.moving_line.title(), "Average speed": f"{self.avg_speed} km/h",
#                                             "Stop duration per station": self.stop_per_station, "Quality": self.quality, "Ticket price": f"{self.ticket_price} Rial",
#                                             "Capacity": f"{self.capacity} passengers"}
