user = ""

class Line:
    def __init__(self):
        self.lines = {}
        self.unauthorized = []

    def add_line(self):
        while True:
            line_name = input("Please enter line_name: ")
            if line_name in self.lines:
                print("This name is duplicated, please try again.")
            else:
                break
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
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
                self.lines[line_name] = [origin, destination, number, stations_list]
                break
            elif ok == "2":
                self.add_line()

        from panel2 import panel
        panel()

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
              f"number: {self.lines[line_name][2]}\n\t"
              f"stations_list: {self.lines[line_name][3]}\n")
        print("which one update? \n"
              "1)linename \n"
              "2)origin \n"
              "3)destination \n"
              "4)number \n"
              "5)stationlist")
        n = int(input())
        new = input("Please enter your new value: ")
        if n == 1:
            self.lines[new] = self.lines[line_name]
            self.lines.pop(line_name)
        elif n in range(2,6):
            self.lines[line_name][n-2] = new

        from panel2 import panel
        panel()

    def delete_line(self):
        line_name = input("Enter linename to delete :")
        self.lines.pop(line_name)
        self.unauthorized.append(user)

        from panel2 import panel
        panel()

    def line_information(self):
        print(self.lines)

        from panel2 import panel
        panel()


