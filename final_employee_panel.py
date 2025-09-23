from final_line import Line
from final_train import Train


def employee_login(employees):
    while True:
        print("Welcome Employee")
        username = safe_input("Username (or 0 to return to Start Menu): ")
        if username == "0":
            return
        password = safe_input("Enter your password: ")
        for emp in employees:
            if emp["username"] == username and emp["password"] == password:
                print(f"Welcome {username}!\n")
                employee_panel()
                break
        else:
            print("Invalid username or password. Please try again.\n")


train = Train(None)
line = Line(train)
train.line = line


def employee_panel():

    while True:
        try:
            print("\nYou are in Employee Panel.")
            print("Please choose a number from the list below:")
            print("1. Adding a line")
            print("2. Updating a line")
            print("3. Removing a line")
            print("4. Viewing all lines")
            print("5. Adding a train")
            print("6. Updating a train")
            print("7. Removing a train")
            print("8. Viewing all trains")
            print("9. Exit your account (Logout)")

            user_input = input(">>> ").strip()
            reference = [str(i) for i in range(1, 10)]

            if user_input not in reference:
                raise ValueError(f"Option '{user_input}' doesn't exist.")

            if user_input == "1":
                line.creating()
            elif user_input == "2":
                line.editing()
            elif user_input == "3":
                line.removing()
            elif user_input == "4":
                line.viewing()
            elif user_input == "5":
                train.creating()
            elif user_input == "6":
                train.editing()
            elif user_input == "7":
                train.removing()
            elif user_input == "8":
                train.viewing()
            elif user_input == "9":
                print("Logging out and returning to Employee Login...\n")
                return
            

        except ValueError as e:
            print(e)
            while True:
                user_input1 = safe_input(
                    "Enter  '1' to try again: ").strip()
                if user_input1 == "1":
                    break
                else:
                    print("Invalid option. Please choose either '0' or '1'.")
def safe_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Input must be non-empty. Please try again")

employee_panel()