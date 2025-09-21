from final_line import Line
from final_train import Train


def employee_panel():
    print("\nWelcome employee\n")
    # we can use employee's name to welcome them
    train = Train(None)
    line = Line(train)
    train.line = line
    while True:
        try:
            print("\nYou are in Employee Panel.\nPlease choose a number from the list below:\n1.Adding a line\n2.Updating a line\n3.Removing a line\n4.Viewing all lines\n5.Adding a train\n6.Updating a train\n7.Removing a train\n8.Viewing all trains\n9.Exit your account")
            user_input = input(">>>").strip()
            reference = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if user_input in reference:
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
                    pass
            else:
                raise ValueError(f"Option '{user_input}' doesn't exist.")
        except ValueError as e:
            print(e)
            user_input2 = input(
                "Press 'Enter' to try again or enter 'exit' to return to Employee Panel: ").strip().lower()
            if user_input2 == "exit":
                break


employee_panel()
