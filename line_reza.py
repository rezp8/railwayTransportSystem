user = ""

class Line:
    def __init__(self):
        self.lines = {}
        self.unauthorized = []

    def add_line(self):
        while True:
            line_name = input("Please enter line_name: (or print exit to finish)")
            try:
                if line_name in self.lines:
                    NameError("This name is duplicated, please try again.")
                elif line_name == "":
                    ValueError("This value cannot be empty.")
                elif line_name == "exit":
                    return
                else:
                    break
            except NameError as e:
                print(e)
            except ValueError as e:
                print(e)
        while True:
            origin = input("Enter origin: (or print exit to finish)")
            try:
                if origin == "":
                    ValueError("This value cannot be empty.")
                elif origin == "exit":
                    return
                else:
                    break
            except ValueError as e:
                print(e)
        while True:        
            destination = input("Enter destination: (or print exit to finish)")
            try:
                if origin == "":
                    ValueError("This value cannot be empty.")
                elif destination == origin:
                    NameError("The origin name cannot be the same as the destination name.")
                elif origin == "exit":
                    return
                else:
                    break
            except ValueError as e:
                print(e)
            except NameError as e:
                print(e)

        #number = input("enter number: ")
        stations_list = []
        print("To create a list of stations, enter the name of each station, then press the enter button \nand press the f button to finish.")
        while True:
            station = input("Please print station name for add to stations_list: ")
            if station == "f":
                break
            else:
                stations_list.append(station)
        number = len(stations_list)
        print("------------------ \n"
              f"You are creating a new line in name {line_name} with origin: {origin} and destination: {destination} and staions list of {stations_list} and {number} stations")
        while True:
            ok = input("\nIs the information confirmed or are you rebuilding the line? \n"
            "1) Ok \n"
            "2) I repeat the operation again. \n")
            if ok == "1":
                self.lines[line_name] = [origin, destination, stations_list, number]
                break
            elif ok == "2":
                self.add_line()

    def update_line(self):
        while True:
            line_name = input("Enter linename: ")
            try:
                if line_name in self.lines:
                    break
                else:
                    raise KeyError("The line name is invalid. Please try again.")
            except KeyError:
                print("The line name is invalid. Please try again.")
        print(f"{line_name} line:\n\t"
              f"origin: {self.lines[line_name][0]}\n\t"
              f"destination: {self.lines[line_name][1]}\n\t"
              f"stations_list: {self.lines[line_name][2]}\n\t"
              f"number: {self.lines[line_name][3]}\n")
        print("which one update? \n"
              "1)linename \n"
              "2)origin \n"
              "3)destination \n"
              "4)stationlist")
        n = int(input())
        
        if n == 1:
            new = input("Please enter your new value: ")
            self.lines[new] = self.lines[line_name]
            self.lines.pop(line_name)
        elif n in range(2,4):
            new = input("Please enter your new value: ")
            self.lines[line_name][n-2] = new
        elif n == 4:
            x = int(input("What changes would you like to make to the station list? \n" \
            "1) Remove the station \n" \
            "2) Add station \n"))

            if x == 1:
                name = input("Please enter station name to remove.")
                self.lines[line_name][2].remove(name)
            elif x == 2:
                name = input("Please enter station name to add.")
                self.lines[line_name][2].append(name)
            self.lines[line_name][3] = len(self.lines[line_name][2])

    def delete_line(self):
        line_name = input("Enter linename to delete :")
        self.lines.pop(line_name)
        self.unauthorized.append(user)

    def line_information(self):
        print(self.lines)



