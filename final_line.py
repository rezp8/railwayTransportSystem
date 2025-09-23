
class Line:
    def __init__(self, train):
        self.lines = {}
        self.train = train

    def get_valid_stations(self, num_stations, origin, destination):
        while True:
            station_names = safe_input(
                f"Please enter {num_stations} station names separated by space\n"
                "***For multi-part names use '_'\n"
                "(Enter '0' to go back to Employee Panel)\n>>> "
            ).strip().title().split()

            if station_names == ["0"]:
                return None

            if len(station_names) != num_stations:
                print(
                    f"Expected {num_stations} station names but received {len(station_names)}.")
                continue

            if len(set(station_names)) < len(station_names):
                print("Station names cannot be repetitive.")
                continue

            if any(station == origin.title() or station == destination.title() for station in station_names):
                print("Station name cannot be the same as 'Origin' or 'Destination'.")
                continue

            return station_names

    def creating(self):
        while True:
            try:
                name = safe_input(
                    "Line name:(Enter '0' to go back to employee panel ) ").strip()
                if name == "0":
                    return

                origin = safe_input("Origin: ").strip()
                if origin == "0":
                    return

                while True:
                    destination = safe_input("Destination: ").strip()
                    if destination.lower() == origin.lower():
                        print("'Destination' cannot be the same as 'Origin'")
                        continue
                    break

                while True:
                    stations_number = safe_input(
                        "Number of stations: ").strip()
                    if not stations_number.isdecimal():
                        print(
                            "Number of stations must be a whole number equal or greater than zero.")
                        continue
                    break

                if int(stations_number) == 0:
                    station_names = None
                else:
                    stations = self.get_valid_stations(
                        int(stations_number), origin, destination)
                    if stations is None:
                        return
                    station_names = stations

                if name not in self.lines:
                    self.lines[name] = {
                        "origin": origin.title(),
                        "destination": destination.title(),
                        "number of stations": stations_number,
                        "stations": station_names
                    }
                    print(
                        f"\n***** '{name}' has been successfully added *****\n")
                else:
                    print(
                        f"A line named '{name}' already exists. Line names cannot be repetitive.")

                while True:
                    user_input6 = input(
                        "Enter '0' to go back to Employee Panel or '1' to add another line: ").strip()
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
            if len(self.lines) == 0:
                print("No line found to edit.")
                print("------------------------")
                while True:
                    user_input0 = input(
                        "Enter 0 to go back to Employee Panel: ").strip()
                    if user_input0 == "0":
                        return
                    else:
                        print("Invalid option.")

            line_name_input = safe_input(
                "Enter the name of the line you would like to edit:\n"
                "(Enter '0' to go back to Employee Panel)\n>>> "
            ).strip()
            if line_name_input == "0":
                return

            if line_name_input in self.lines:
                line_name = line_name_input
            else:
                print(f"Line named '{line_name_input}' doesn't exist.")
                retry = safe_input(
                    "Enter '1' to try again or '0' to return to Employee Panel:\n>>> ").strip()
                if retry == "0":
                    return
                else:
                    continue

            print(f"{line_name} : {self.lines[line_name]}")

            while True:
                reference = ["origin", "destination",
                             "number of stations", "stations"]
                feature = safe_input(
                    "What feature would you like to edit? (origin, destination, number of stations, stations)\n"
                    "(Enter '0' to go back to Employee Panel)\n>>> "
                ).strip().lower()

                if feature == "0":
                    return

                if feature not in reference:
                    print(
                        f"There is no feature named '{feature}'. Please try again.")
                    continue

                if feature == "number of stations":
                    while True:
                        new_value = safe_input(
                            "Enter the new number of stations:\n>>> ").strip()
                        if not new_value.isdigit() or int(new_value) < 0:
                            print(
                                "Number of stations must be a whole number equal or greater than zero.")
                            continue
                        self.lines[line_name]["number of stations"] = new_value
                        if int(new_value) == 0:
                            self.lines[line_name]["stations"] = None
                        else:
                            stations = self.get_valid_stations(
                                int(new_value),
                                self.lines[line_name]["origin"],
                                self.lines[line_name]["destination"]
                            )
                            if stations is None:
                                return
                            self.lines[line_name]["stations"] = stations
                        break

                elif feature == "stations":
                    if self.lines[line_name]["number of stations"] == "0":
                        print(
                            "This line has 0 stations, edit 'number of stations' first.")
                        continue
                    stations = self.get_valid_stations(
                        int(self.lines[line_name]["number of stations"]),
                        self.lines[line_name]["origin"],
                        self.lines[line_name]["destination"]
                    )
                    if stations is None:
                        return
                    self.lines[line_name]["stations"] = stations

                else:
                    new_value = safe_input(
                        f"Enter the new value for '{feature}':\n>>> ").strip()
                    self.lines[line_name][feature] = new_value

                print(
                    f"\n***** {feature} of '{line_name}' has been successfully changed. *****\n")

                while True:
                    next_step = safe_input(
                        "Enter '0' to return to Employee Panel\n"
                        "Enter '1' to edit another feature of this line\n"
                        "Enter '2' to edit another line\n>>> "
                    ).strip()
                    if next_step == "0":
                        return
                    elif next_step == "1":
                        break
                    elif next_step == "2":
                        break
                    else:
                        print("Invalid option. Please try again.")

                if next_step == "1":
                    continue
                elif next_step == "2":
                    break

    def removing(self):
        while True:
            try:
                if len(self.lines) == 0:
                    print("No line found to remove.")
                    print("------------------------")
                    while True:
                        user_input0 = input(
                            "Enter 0 to go back to Employee Panel: ").strip()
                        if user_input0 == "0":
                            return
                        else:
                            print("Invalid option.")
                user_input = safe_input(
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
            print(f"\nNo line found to display")
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
