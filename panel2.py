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
            if user in l.unauthorized:
                print("You can't sign in")
            elif i==user and dic[i][3]==password:
                panel()
            else:
                raise ValueError("Your password or user is not correct")
        except ValueError:
            print("Your password or user is not correct")
            sign_in()

def panel():
    print(
        "-------------------- \n"
        "Train employee panel \n" 
        "1) add a new line \n"
        "2) edit and update a line \n"
        "3) delete a line \n"
        "4) see line informations \n"
        "5) add a new train \n"
        "6) edit and update a train \n"
        "7) delete a train \n"
        "8) see line informations \n"
        "9) Sign out of the user account \n"
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
    except ValueError:
        print("Please enter a number from 1 to 9")



