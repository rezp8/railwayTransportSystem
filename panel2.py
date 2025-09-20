from line_class import Line
from train_class import Train
t = Train()
l = Line()
dic = {"user":["name", "last name", "email", "password"]}

def sign_in():
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    for i in dic:
        try:
            if user in l.unauthorized_list:
                print("You can't sign in")
            elif dic[i]==user and dic[i][3]==password:
                panel()
            else:
                raise ValueError("Your password or user is not correct")
        except ValueError:
            print("Your password or user is not correct")

def panel():
    print(
        "Train employee panel"
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
    try:
        if number == 1:
            l.add_line()
        elif number == 2:
            l.update_line()
        elif number == 3:
            l.delete_line()
        elif number == 4:
            l.line_information()
        elif number == 5:
            t.add_train()
        elif number == 6:
            t.update_train()
        elif number == 7:
            t.delete_train()
        elif number == 8:
            t.trains_information()
        elif number == 9:
            exit()
        else:
            raise ValueError("Please enter a number from 1 to 9")
    except:
        print("Please enter a number from 1 to 9")

sign_in()


