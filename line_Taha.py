
Lines = {}

class Line:
    def __init__(self, name, origin, destination, num_of_stations : int, list_of_station : list):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.num_of_stations = num_of_stations
        self.list_of_station = list_of_station

    def show_info(self):
        print('*' * 8, 'Information', '*' * 8)
        print(f"Line Name: {self.name}")
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Number of Stations: {self.num_of_stations}")
        print(f"Stations: {', '.join(self.list_of_station)}")
        print('*' * 8, 'Information', '*' * 8)



def add_line():
    while True:
        name = input("Please Enter The Line Name: (or type 'back') ")
        if name.lower() == 'back':
            train_employee_panel()
        if name in Lines:
            print('The name entered is a duplicate. Please use a different name. ')
            continue
        origin = input('Please Enter The Origin: ')
        destination = input('Please Enter The Destination: ')
        num_of_stations = int(input("Please Enter Number of Stations: "))
        station_list = input('Please Enter Name of Stations: ').split()
        new_line = Line(name, origin, destination, num_of_stations, station_list)
        Lines[name] = new_line
        print(" Line added successfully.\n")
        train_employee_panel()



def update_line():
    while True:
        name = input("Enter line name to update (or type 'back'): ")
        if name.lower() == 'back':
            train_employee_panel()
        if name not in Lines:
            print('Line not found. try again')
            continue
        line = Lines[name]
        line.show_info()
        print("Which attribute would you like to update?")
        print("1. Origin\n2. Destination\n3. Stations\n4. Back")
        choice = int(input("Your choice: "))
        match choice:
            case 1:
                line.origin = input('Enter new origin')
            case 2:
                line.destination = input('Enter new destination')
            case 3:
                num = int(input("Enter new number of stations: "))
                line.num_of_stations = num
                station_list = input('Please Enter Name of Stations: ').split()
                line.list_of_station = station_list
            case 4:
                train_employee_panel()
        print(" Line updated successfully.")
        train_employee_panel()


def delete_line():
    while True:
        name = input("Enter line name to delete (or type 'back'): ")
        if name.lower() == 'back':
            train_employee_panel()
        if name not in(Lines):
            print(" Line not found. Try again.")
            continue
        del lines[name]
        print(" Line deleted successfully.\n")
        #return(ابهام در درک صورت مساله)
        train_employee_panel()


def view_lines():
    if len(Lines) == 0:
        print('No lines found.')
    else:
        print("Lines:")
        for line in Lines.values():
            line.show_info()
    while True:
        inp = input()
        if inp == 'back':
            train_employee_panel()



def train_employee_panel():
    while True:
        print('1: Add Line')
        print('2: Line Information Update')
        print('3: Delete Line')
        print('4: View the List of Lines')
        # print('5: Add Train')
        # print('6: Delete Train')
        # print('7: View the List of Trains')
        # print('8: log out')
        choice = int(input())
        match choice:
            case 1:
                add_line()
            case 2:
                update_line()
            case 3:
                delete_line()
            case 4:
                view_lines()
            case 5:
                exit()
            case _:
                print('Please Enter valid number')


train_employee_panel()