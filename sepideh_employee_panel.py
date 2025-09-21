from sepideh_line import Line
from sepideh_train import Train


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
            # *** input should be restricted to be a number between 1 to 9. Throw Exception if the input is empty or not a number,or it's a number but not in the correct range

            reference = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            if user_input in reference:
                # while True:
                if user_input == "1":
                    # while True:
                    #     line.adding()
                    #     user_input0 = input(
                    #         "Press 'Enter' if you would like to add another line or enter 'exit' to return to Employee Panel: ").lower()
                    #     if user_input0 == "exit":
                    #         break
                    # break
                    line.creating()
                    # break
                elif user_input == "2":
                    line.editing()
                    # break
                elif user_input == "3":
                    line.removing()
                    # break
                elif user_input == "4":
                    line.viewing()
                    # break
                elif user_input == "5":
                    train.creating()
                    # break
                elif user_input == "6":
                    train.editing()
                    # break
                elif user_input == "7":
                    train.removing()
                    # break
                elif user_input == "8":
                    train.viewing()
                    # break
                elif user_input == "9":
                    pass
                    # break
            else:
                raise ValueError(f"Option '{user_input}' doesn't exist.")
        except ValueError as e:
            print(e)
            user_input2 = input(
                "Enter 'exit' to return to the previous page or press enter to try again: ").strip().lower()
            if user_input2 == "exit":
                break


employee_panel()
