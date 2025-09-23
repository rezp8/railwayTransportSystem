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

                    if Line.lines[moving_line]["number of stations"] == "0":
                        stop_per_station = None
                    else:
                        while True:
                            print(self.line.lines[moving_line]
                                  ["stations"])
                            stop_per_station = safe_input(
                                f"Stop duration(in minutes) for each station, separated by spaces\n(Enter 'back' to go back to employee panel)\n>>> ").strip()
                            if stop_per_station.title() == "Back":
                                return
                            stop_per_station = stop_per_station.split()
                            if len(stop_per_station) != int(self.line.lines[moving_line]["number of stations"]):
                                print(
                                    f"Expected {int(self.line.lines[moving_line]["number of stations"])} stop duration but recieved {len(stop_per_station)}")
                                continue
                            elif not all(is_float(number) for number in stop_per_station):
                                print(
                                    "The format of stop duration must be a whole or floating number")
                                continue
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
            if len(self.trains) == 0:
                print("No train found to edit.")
                print("------------------------")
                while True:
                    user_input0 = input("Enter 0 to go back to Employee Panel: ").strip()
                    if user_input0 == "0":
                        return
                    else:
                        print("Invalid option.")

            print(sorted(list(self.trains.keys())))
            train_id_input = safe_input(
                "Enter the ID of the train you would like to edit from the list above:\n"
                "(Type  'back' to go back to Employee Panel)\n>>> "
            ).strip().title()
            if train_id_input == "Back":
                return

            train_keys= {key: key for key in self.trains.keys()}
            if train_id_input.title() in train_keys:
                train_id = train_keys[train_id_input]
            else:
                print(f"Train with ID '{train_id_input}' doesn't exist.")
                retry = safe_input("Enter '1' to try again or '0' to return to Employee Panel:\n>>> ").strip()
                if retry == "0":
                    return
                else:
                    continue

            print(f"{train_id} : {self.trains[train_id]}")

            while True:
                feature_map = {
                    "1": "Name",
                    "2": "Line",
                    "3": "Average speed",
                    "4": "Stop duration per station",
                    "5": "Quality",
                    "6": "Ticket price",
                    "7": "Capacity"
                }

                feature_input = safe_input(
                    "What feature would you like to edit?\n"
                    "1. Name\n2. Line\n3. Average speed\n4. Stop duration per station\n"
                    "5. Quality\n6. Ticket price\n7. Capacity\n0. Return to Employee Panel\n>>> "
                ).strip()

                if feature_input == "0":
                    return

                feature = feature_map.get(feature_input)
                if not feature:
                    print("Invalid option. Please try again.")
                    continue

                if feature == "Stop duration per station":
                    line_name = self.trains[train_id]["Line"]
                    num_stations = int(Line.lines[line_name]["number of stations"])
                    if num_stations == 0:
                        print("This train's line has 0 stations. No stop durations to edit.")
                        continue
                    print(Line.lines[line_name]["stations"])
                    while True:
                        new_times = safe_input(
                            f"Enter new stop durations for each station, separate them by spaces:\n"
                            "(Type 'back' to cancel)\n>>> "
                        ).strip().title().split()
                        if new_times == ["Back"]:
                            return
                        if len(new_times) != num_stations:
                            print(f"Expected {num_stations} values but got {len(new_times)}.")
                            continue
                        if not all(is_float(time) for time in new_times):
                            print("All durations must be numeric.")
                            continue
                        self.trains[train_id][feature] = new_value
                        break

                else:
                    while True:
                        new_value = safe_input(f"Enter the new value for '{feature}':\n(Type 'back' to cancel)\n>>> ").strip().title()
                        if new_value == "Back":
                            break
                        if feature == "Line":
                            if new_value not in Line.lines:
                                print(f"Line '{new_value}' doesn't exist.")
                                continue
                        elif feature == "Average speed" or feature == "Ticket price":
                            if not is_float(new_value) or float(new_value) <= 0:
                                print(f"{feature} must be a positive number.")
                                continue
                        elif feature == "Capacity":
                            if not new_value.isdigit() or int(new_value) < 0:
                                print("Capacity must be a positive whole number.")
                                continue
 
                        self.trains[train_id][feature] = new_value
                        break

                print(f"\n***** {feature} of train '{train_id}' has been successfully changed. *****\n")

                next_step = safe_input(
                    "Enter '0' to return to Employee Panel\n"
                    "Enter '1' to edit another feature of this train\n"
                    "Enter '2' to edit another train\n>>> "
                ).strip()
                if next_step == "0":
                    return
                elif next_step == "1":
                    continue
                elif next_step == "2":
                    break
                else:
                    print("Invalid option. Returning to Employee Panel.")
                    return


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
