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
                return   
            else:
                print("Incorrect password, please try again.\n")
        else:
            print("Username not found, please try again.\n")


