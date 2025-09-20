def employee_login(employees):
    print("welcome Employee")
    while True:
        input_username = input("username (or type 'panel' to go back to start menu): ")
        
        if input_username.lower() == "panel":
            break
        
        input_password = input("password : ")
        
        matched_user = None
        
        for emp in employees:
            if emp["username"] == input_username:
                matched_user = emp
                break
            
        if matched_user:
            if matched_user["password"] == input_password:
                print("Login was successful!")
                todo=input("What would you like to do next?\n1.Add a line\n2.Update line information\n3.Delete a line\n4.View list of lines\n5.Add a train\n6.Update train information\n7.Delete a train\n8.View list of trains\n9.Log out\n")
                employee_panel(todo)
                return   
            else:
                print("Incorrect password!, please try again.\n")
        else:
            print("Username not found, please try again.\n")
from line_class import Line
from employee_class import Employee

def employee_panel(todo):

    match todo:
        case "1" :
            Line.add_line( )
        case "2" :
            Line.update_line()
        case "3":
            Line.delete_line()
        case "4":
            Line.line_information()
        case "5":
            Employee.add_train()
        case "6":
            Employee.edit_train()
        case "7":
            Employee.delete_train()
        case "8":
            Employee.trains_info()


