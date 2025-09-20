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
            print("Baraye Bazgasht Be Menu Ghabl '0' Ra Vared Konid")
            user = input("Nam Karbari: ")
            if user == "0":
                return False
            
            pass0 = input("Ramz Obour: ")
            if pass0 == "0":
                return False
            
            print("------------------------")
            if user == self.username and pass0 == self.password:
                return True
            
            else:
                print("Nam Karbari ya Ramz Obour Sahih namibashad")
                while True:
                    failed = input("1. Talash Dobare/ 2. Bazgasht Be Menu Ghabl ")
                    if failed == "1":
                        print("------------------------")
                        break
                    elif failed == "2":
                        print("------------------------")
                        return False
                    else:
                        print("Vorodi Sahih Nist, Dobare Talash Konid!")
                        print("------------------------")
                        continue

        
    def admin_panel(self):
        while True:
            print("Admin Ba Movafaghiat Vared Shodi")
            print("1. Ezafe Kardan Karmand Ghatar")
            print("2. Hazf Karmand Ghatar")
            print("3. List Karmandha")
            print("4. Khorooj!")
            print("------------------------")
            
            choose = input("Koja Beram? ")
            if choose == "1":
                print("Ezafe Kardan Karmand")
                self.add_employee()
            elif choose == "2":
                print("Hazf Karmand")
                self.remove_employee()
            elif choose == "3":
                print("List Karmandha")
                self.view_list()
            elif choose == "4":
                print("------------------------")
                break
            
            else:
                while True:
                    print("Vorodi Dade Shode Dorost Namibashad")
                    failed = input("1. Talash Dobare/ 2. Bazgasht Be Menu Ghabl ")
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
            print("Baray Bazgasht Be Menu Ghabl '0' Ra vared konid")
            
            while True:
                n = input("name: ").lower()
                if n == "0":
                    return
                if not n.isalpha() or len(n) < 3:
                    print("Esm Bayad Faghat Horoof Bashad Va Hadaghal 3 Harf Dashte Bashad")
                    continue
                break
            
            while True:
                f = input("family: ").lower()
                if f == "0":
                    return
                if not f.isalpha() or len(f) < 3:
                    print("famil Bayad Faghat Horoof Bashad Va Hadaghal 3 Harf Dashte Bashad")
                    continue
                break
            
            while True:
                e = input("email: ").lower()
                if e == "0":
                    return
                if not("@" in e and re.search(r"\.com$", e) and len(e) > 8):
                    print("Email Motabar Namibashad")
                    continue
                if e in self.email_checker:
                    print("Email Tekrari Ast")
                    continue
                break
            
            while True:
                u = input("username: ").lower()
                if u == "0":
                    return
                if len(u) < 4 or not u.isalnum():
                    print("Username Bayad Hadaghal 4 Harf Va Faghat Horoof Ya Adad Bashad")
                    continue
                if u in self.user_checker:
                    print("Username Tekrari Ast")
                    continue
                break
            
            while True:
                p = input("password: ")
                if p == "0":
                    return
                if len(p) < 6 or not re.search(r"\d", p):
                    print("Password Bayad Hadaghal 6 Ragham Bashad")
                    continue
                break
            
            new_dict = {"name" : n, "family": f, "email" : e, "username": u, "password": p}
            self.user_checker.append(u)
            self.email_checker.append(e)
            self.employees.append(new_dict)
            print("Karmand Ba Movafaghiat Ezaf Shod!")
            
            while True:
                print("------------------------")
                again = input("1. Ezafe kardan Karmand Jadid/ 2. Khorooj!: ")
                if again == "1":
                    break
                elif again == "2":
                    return    
                else:
                    print("vorodi Sahih Nist, Dobare Talash Konid!")
                    continue
            
    def remove_employee(self):
        while True:
            print("Baray Bazgasht Be Menu Ghabl '0' Ra vared konid")
            wanted = input("username: ")
            if wanted == "0":
                return
            
            found = False
            for emp in self.employees:
                if wanted == emp["username"]:
                    self.employees.remove(emp)
                    self.user_checker.remove(emp["username"])
                    print("karmand Ba Movafaghiat Hazf Shod!")
                    found = True
                    break
                
            if not found:
                print("Karmand Peyda Nashod!")
                
            while True:
                    print("------------------------")
                    again = input("1. Hazf kardan Karmand / 2. Khorooj!: ")
                    if again == "1":
                        break
                    elif again == "2":
                        return    
                    else:
                        print("vorodi Sahih Nist, Dobare Talash Konid!")
                        continue
    
    def view_list(self):
        while True:
            if not self.employees:
                print("Hich karmandi Hanoz Sabt Nashode")
                escape = input("Baraye Bazgash Adad '0' Ra Vared Konid: ")
                if escape == "0":
                    break
                else:
                    print("Vorodi Sahih Nist, Dobare Talash Konid!")
                    print("------------------------")
                
            else:
                for i, emp in enumerate(self.employees, 1):
                    print(f"{i}. Name: {emp['name'].title()} | Family: {emp['family'].title()} | Email: {emp['email']} | Username: {emp['username']} | Password: {emp['password']}")
                    print("------------------------")
                escape = input("Baraye Bazgash Adad '0' Ra Vared Konid: ")
                if escape == "0":
                    print("------------------------")
                    break
        
    def exit_from(self):
        return