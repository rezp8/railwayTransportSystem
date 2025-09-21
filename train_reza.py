class Train:
    def __init__(self):
        self.trains = {}
        self.id_counter = 0

    def add_train(self):
        pass
        from panel2 import l
        train_name = input("Enter train_name: ")
        line_name = input("Enter line_name: ")
        average_speed = input("Enter average_speed: ")
        stop_dic = {}
        for i in l.lines[line_name][3]:
           stop_dic[i] = input(f"Please enter the amount of time spent at {i} station: ")
        quality_grade = input("Enter quality_grade: ")
        ticket_cost = input("Enter ticket_cost: ")
        capacity = input("Enter capacity: ")
        train_id= f"train-{self.id_counter+1}"

        self.trains[train_id] = [
           train_name, line_name, average_speed, stop_dic, quality_grade, ticket_cost, capacity
        ]
        

    def update_train(self):
        pass

    def delete_train(self):
        train_id = input("Please enter train_id: ")
        self.trains.pop(train_id)

    def trains_information(self):
        print(self.trains)