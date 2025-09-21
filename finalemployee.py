from finalemployee_class import Employee


def employee_login(employees):
    print("welcome Employee")
    while True:
        username = Employee.safe_input("username (or 0 to return): ")
        if username == "0": 
            return
        password = Employee.safe_input("Enter your password: ")

        for emp in employees:   
            if emp["username"] == username and emp["password"] == password:
                print("Welcome employee!")
                employee_panel
                return True

        print("Invalid username or password. Please try again.")


def employee_panel():
        while True:
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
            "9) Sign out of the user account \n"  )
            choice = Employee.safe_input("Choose an option(0 to return to previous page ): ")
            match choice:
                case "1":
                    Employee.add_line()
                    employee_panel()
                case "2":
                    Employee.edit_line()
                    employee_panel()
                case "3":
                    Employee.delete_line()
                    employee_panel()
                case "4":
                    Employee.line_info()
                    employee_panel()
                case "5":
                    Employee.add_train()
                    employee_panel()
                case "6":
                    Employee.edit_train()
                    employee_panel()
                case "7":
                    Employee.delete_train()
                    employee_panel()
                case "8":
                    Employee.train_info()
                    employee_panel()
                case "9":
                    exit()
                case "0":
                    return
                case _:
                    print("Invalid choice.Try again.")
                    employee_panel()




               

