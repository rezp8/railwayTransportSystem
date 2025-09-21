from admin import Admin
from final_employee_panel import employee_login
admin = Admin()

def start_menu():
    while True:
        print("Welcome!")
        print("1. Admin")
        print("2. Employee")
        print("3. User")
        print("4. Exit")
        print("------------------------")
        choose = input("Select an option: ")
        
        if choose == "1":
            print("Welcome Admin!")
            if admin.log_in():
                admin.admin_panel()
                
        elif choose == "2":
            employee_login(admin.employees)
            
        elif choose == "3":
            #waiting for published
            print("Karbar Khoosh oomadi!")
            print("Coming Soon")
            
        elif choose == "4":
            print("Goodbye!")
            break
        else:
            while True:
                print("Invalid input")
                failed = input("1. Try again/ 2. Exit program ")
                if failed == "1":
                    print("------------------------")
                    break
                elif failed == "2":
                    exit()
                else:
                    print("------------------------")  
                
                    
        
if __name__ == "__main__":
    start_menu()