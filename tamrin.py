class Karmand:
    def __init__(self):
        self.lines = {}
        self.trains = {}
        self.mamnooe_list = []
        self.id_counter = 0

    def add_line(self):
        while True:
            line_name = input("input linename: ")
            if line_name in self.lines:
                print("This line name is duplicated, please try againe.")
                continue
            else:
                break
        origin = input("input origin: ")
        destination = input("input destination: ")
        number = input("input number: ")
        stations_list = input("input stations_list: ")
        self.lines[line_name] = [origin, destination, number, stations_list]

    def update_line(self):
        line_name = input("input linename: ")
        print(f"{line_name} line:\n \t"
              f"origin: {self.lines[line_name][1]}\n"
              f"destination: {self.lines[line_name][2]}\n"
              f"number: {self.lines[line_name][3]}\n"
              f"stations_list: {self.lines[line_name][4]}\n")
        print("which one update?",
              "1)linename",
              "2)origin",
              "3)destination",
              "4)number",
              "5)stationlist")
        n = int(input())
        new = input("please enter your new value: ")
        if n == 1:
            self.lines[new] = self.lines[line_name]
            self.lines.pop(line_name)
        elif n in range(2,6):
            self.lines[line_name][n-2] = new

    def delete_line(self):
        line_name = input("enter linename to delete :")
        self.lines.pop(line_name)
        self.mamnooe_list.append(user)

    def line_information(self):
        print(self.lines)

    def add_train(self):
        train_name = input("input train_name: ")
        line_name = input("input line_name: ")
        average_speed = input("input average_speed: ")
        stop_dic = {}
        for i in self.lines[line_name][3]:
            stop_dic[i] = input(f"please enter the amount of time spent at {i} station: ")
        quality_grade = input("input quality_grade: ")
        ticket_cost = input("input ticket_cost: ")
        capacity = input("input capacity: ")
        train_id= f"train-{self.id_counter+1}"

        self.trains[train_id] = [
            train_name, line_name, average_speed, stop_dic, quality_grade, ticket_cost, capacity
        ]

    def update_train(self):
        pass

    def delete_train(self):
        train_id = input("please enter train_id: ")
        self.trains.pop(train_id)

    def trains_information(self):
        print(self.trains)

def panel():
    print(
        "Welcome to Train employee panel"
        "1) add a new line"
        "2) edit and update a line"
        "3) delete a line"
        "4) see line informations"
        "5) add a new train"
        "6) edit and update a train"
        "7) delete a train"
        "8) see line informations"
        "9) Sign out of the user account"
    )
    number = int(input("pleae enter a number to continue: "))
    if number == 1:
        k.add_line()
    elif number == 2:
        k.update_line()
    elif number == 3:
        k.delete_line()
    elif number == 4:
        k.line_information()
    elif number == 5:
        k.add_train()
    elif number == 6:
        k.update_train()
    elif number == 7:
        k.delete_train()
    elif number == 8:
        k.trains_information()
    elif number == 9:
        exit()
    else:
        print("please enter a number from 1 to 9")

def sign_in():
    user = input("input your user: ")
    password = input("input your password: ")
    for i in dic:
        if user in k.mamnooe_list:
            print("you can't sign in")
        elif dic[i][3]==user and dic[i][4]==password:
            panel()
        else:
            print("your password or user is not correct")

k = Karmand() # لزوم ساخت یک شی کلاس پنل کارمند بصورت مستقل
dic = {} # اطلاعات پنل1
#Unauthorized