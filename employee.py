from start_menu import start_menu
employees = [
    {"username": "user1", "password": "pass1"},
    {"username": "user2", "password": "pass2"},
    {"username": "user3", "password": "pass3"}
]
def employee_login():
    print("welcome Employee")
    while True:
        input_username = input("username (or type 'panel' to go back to start menu): ")

        if input_username.lower() == "panel":
            start_menu()
            break
        input_password = input("password : ")

        matched_user = None
        for emp in employees:
            if emp["username"] == input_username:
                matched_user = emp
                break

        if matched_user:
            if matched_user["password"] == input_password:
                choice=input("Login was successful!")
                return 0#def employee()    
            else:
                print("Incorrect password, please try again.\n")
        else:
            print("Username not found, please try again.\n")


