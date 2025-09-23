from final_line import Line


class Train:
    def __init__(self, line):
        self.trains = {}
        self.line = line

    def creating(self):
        if len(self.line.lines) == 0:
            print(
                f"\nAdding train is not possible: no line defined yet.\nPlease add a line first by choosing option 1 from Employee Panel.")
            print("------------------------")
            while True:
                user_input0 = input(
                    "Type 'back' to go to Employee Panel: ").strip().title()
                if user_input0 == "Back":
                    break
                else:
                    print("Invalid option.")

        else:
            while True:
                try:
                    while True:
                        name = safe_input(
                            "Train name:(Type 'back' to go back to Employee Panel) ").strip().title()
                        if name == "Back":
                            return
                        elif is_float(name):
                            print(
                                "Name could be a combination of alphabets and digits but not digits only")
                        break

                    while True:
                        print(sorted(list(self.line.lines.keys())))
                        moving_line = safe_input(
                            "Please choose a line from the list above:(Type 'back' to go back to employee panel) ").strip().title()
                        if moving_line == "Back":
                            return
                        elif moving_line not in list(self.line.lines.keys()):
                            print(f"Line named '{moving_line}' doesn't exist")
                        break

                    while True:
                        avg_speed = input(
                            "Average speed:(Type 'back' to go back to employee panel) ").strip().title()
                        if avg_speed == "Back":
                            return
                        elif not is_float(avg_speed) or float(avg_speed) < 0:
                            raise ValueError(
                                "Average speed must be a whole or floating number equal or greater than zero")
                        break

                    if self.line.lines[moving_line]["number of stations"] == "0":
                        stop_per_station = None
                    else:
                        while True:
                            print(self.line.lines[moving_line]
                                  ["stations"])
                            stop_per_station = safe_input(
                                f"Stop duration(in minutes) for each station, separated by spaces\n(Enter 'back' to go back to employee panel)\n>>> ").strip().title().split()
                            for number in stop_per_station:
                                if len(stop_per_station) == 0 and number == "Back":
                                    return
                            if len(stop_per_station) != int(self.line.lines[moving_line]["number of stations"]):
                                print(
                                    f"Expected {int(self.line.lines[moving_line]["number of stations"])} stop duration but recieved {len(stop_per_station)}")
                            for number in stop_per_station:
                                if not is_float(number):
                                    print(
                                        "The format of stop duration must be a whole or floating number")
                            break

                    while True:
                        quality_reference = ["3stars", "2stars", "1star"]
                        print(quality_reference)
                        quality = input(
                            "Please choose 'Train Quality' from the list above:\n(Type 'back' to go back to employee panel) ").strip().title()
                        if quality == "Back":
                            return
                        elif quality not in quality_reference:
                            print(
                                f"Quality '{self.quality}' has not been defined.")
                        break

                    while True:
                        ticket_price = input(
                            "Ticket price:(Type 'back' to go back to employee panel) ").strip().title()
                        if ticket_price == "Back":
                            return
                        elif not is_float(ticket_price) or float(ticket_price) < 0:
                            print(
                                "Price must be a whole or floating number equal or greater than zero")
                        break

                    while True:
                        capacity = input(
                            "Capacity:(Type 'back' to go back to employee panel) ").strip().title()
                        if capacity == "Back":
                            return
                        elif not capacity.isdecimal():
                            print("Capacity must be whole number greater than zero")
                        break

                    while True:
                        train_id = input(
                            "Train ID:(Type 'back' to go back to employee panel) ").strip().title()
                        if train_id == "":
                            return
                        elif is_float(name):
                            print(
                                "Train ID could be a combination of alphabets and digits but not digits only")
                        break

                    if train_id not in self.trains:
                        self.trains[train_id] = {"Name": name, "Line": moving_line, "Average speed": avg_speed,
                                                 "Stop duration per station": stop_per_station, "Quality": quality, "Ticket price": ticket_price,
                                                 "Capacity": capacity, "empty capacity": int(capacity)}

                        print(
                            f"\n***** Train with ID '{train_id}' has been successfully added *****\n")
                    else:
                        print(
                            f"A train with ID '{train_id}' already exists. Train IDs cannot be repetetive.")
                    while True:
                        user_input6 = input(
                            "Enter '0' to go back to Employee Panel or '1' to add another train: ").strip()
                        if user_input6 == "1":
                            break
                        elif user_input6 == "0":
                            return
                        else:
                            print("Invalid option.")

                except Exception as e:
                    print(e)

    def editing(self):
        while True:
            try:
                if len(self.trains) == 0:
                    print("No train found to edit.")
                    print("------------------------")
                    while True:
                        user_input0 = input(
                            "Enter 0 to go back to Employee Panel: ").strip()
                        if user_input0 == "0":
                            return
                        else:
                            print("Invalid option.")

                print(sorted(list(self.trains.keys())))
                user_input = input(
                    "Enter the ID of the train you would like to edit from the list above: ").strip().title()
                if user_input in self.trains:
                    print(f"{user_input} : {self.trains[user_input]}")
                    while True:
                        try:
                            user_input2 = input(
                                "What feature would you like to edit?(Name, Line, Average speed, Stop duration per station, Quality, Ticket price, Capacity): ").strip().lower()
                            reference = ["name", "line", "average speed", "stop duration per station",
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
                    print(f"\nNo train found to remove.")
                    print("------------------------")
                    while True:
                        user_input0 = input(
                            "Enter 0 to go back to Employee Panel: ").strip()
                        if user_input0 == "0":
                            return
                        else:
                            print("Invalid option.")

                print(sorted(list(self.trains.keys())))
                user_input = input(
                    "Enter the ID of the train you would like to remove from the list above: ").strip().title()
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
            print("No train found to display")
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


def safe_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Input must be non-empty. Please try again.")


def is_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False
