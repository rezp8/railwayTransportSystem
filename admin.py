import re

class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "123"
        self.employees = []
        self.user_checker = []
        self.email_checker = []
    
    def log_in(self):
        while True:
            print("Enter '0' to return to the previous menu.")
            user = input("Username: ")
            if user == "0":
                return False
            
            pass0 = input("Password: ")
            if pass0 == "0":
                return False
            
            print("------------------------")
            if user == self.username and pass0 == self.password:
                return True
            
            else:
                print("Invalid username or password.")
                while True:
                    failed = input("1. Try Again / 2. Return to Previous Menu: ")
                    if failed == "1":
                        print("------------------------")
                        break
                    elif failed == "2":
                        print("------------------------")
                        return False
                    else:
                        print("Invalid input! Please try again.")
                        print("------------------------")
                        continue

        
    def admin_panel(self):
        while True:
            print("Admin login successful.")
            print("1. Add Train Employee")
            print("2. Remove Train Employee")
            print("3. View Employee List")
            print("4. Exit")
            print("------------------------")
            
            choose = input("Select an option: ")
            if choose == "1":
                print("Adding Employee")
                self.add_employee()
            elif choose == "2":
                print("Removing Employee")
                self.remove_employee()
            elif choose == "3":
                print("Employee List")
                self.view_list()
            elif choose == "4":
                print("------------------------")
                break
            
            else:
                while True:
                    print("Invalid input!")
                    failed = input("1. Try Again / 2. Return to Previous Menu: ")
                    if failed == "1":
                        print("------------------------")
                        break
                    elif failed == "2":
                        print("------------------------")
                        return
                    else:
                        print("------------------------")
            
    def add_employee(self):
        while True:
            print("Enter '0' to return to the previous menu.")
            
            while True:
                n = input("First Name: ").lower()
                if n == "0":
                    return
                if not n.isalpha() or len(n) < 3:
                    print("Name must contain only letters and be at least 3 characters long.")
                    continue
                break
            
            while True:
                f = input("Last Name: ").lower()
                if f == "0":
                    return
                if not f.isalpha() or len(f) < 3:
                    print("Family name must contain only letters and be at least 3 characters long.")
                    continue
                break
            
            while True:
                e = input("Email: ").lower()
                if e == "0":
                    return
                if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$", e):
                    print("Invalid email format.")
                    continue
                if e in self.email_checker:
                    print("Email already exists.")
                    continue
                break
            
            while True:
                print("Username must start with a letter and contain only letters and numbers (minimum 4 characters).")
                u = input("Username: ").lower().strip()
                if u == "0":
                    return
                if not re.match(r"^[a-zA-Z][a-zA-Z0-9]{3,}$", u):
                    print("Invalid username format. Please follow the rule above.")
                    continue
                if u in self.user_checker:
                    print("Username already exists.")
                    continue
                break
            
            while True:
                print("Password must include letters, numbers, and one of the symbols '@' or '&'.")
                p = input("Password: ")
                if p == "0":
                    return
                if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@&])[A-Za-z\d@&]{6,}$", p):
                    print("Password must be at least 6 characters and include a letter, a number, and one of '@' or '&'.")
                    continue
                break
            
            new_dict = {"name" : n, "family": f, "email" : e, "username": u, "password": p}
            self.user_checker.append(u)
            self.email_checker.append(e)
            self.employees.append(new_dict)
            print("Employee added successfully!")
            
            while True:
                print("------------------------")
                again = input("1. Add another employee / 2. Exit: ")
                if again == "1":
                    break
                elif again == "2":
                    return    
                else:
                    print("Invalid input. Please try again.")
                    continue
            
    def remove_employee(self):
        while True:
            print("Enter '0' to return to the previous menu.")
            wanted = input("Username to remove: ")
            if wanted == "0":
                return
            
            found = False
            for emp in self.employees:
                if wanted == emp["username"]:
                    self.employees.remove(emp)
                    self.user_checker.remove(emp["username"])
                    print("Employee removed successfully!")
                    found = True
                    break
                
            if not found:
                print("Employee not found.")
                
            while True:
                    print("------------------------")
                    again = input("1. Remove another employee / 2. Exit: ")
                    if again == "1":
                        break
                    elif again == "2":
                        return    
                    else:
                        print("Invalid input. Please try again.")
                        continue
    
    def view_list(self):
        while True:
            if not self.employees:
                print("No employees registered yet.")
                escape = input("Enter '0' to return to the previous menu.")
                if escape == "0":
                    break
                else:
                    print("Invalid input. Please try again.")
                    print("------------------------")
                
            else:
                for i, emp in enumerate(self.employees, 1):
                    print(f"{i}. Name: {emp['name'].title()} | Family: {emp['family'].title()} | Email: {emp['email']} | Username: {emp['username']} | Password: {emp['password']}")
                    print("------------------------")
                escape = input("Enter '0' to return to the previous menu.")
                if escape == "0":
                    print("------------------------")
                    break
        
    def exit_from(self):
        return