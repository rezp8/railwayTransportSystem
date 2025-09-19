class userPanel:
    def __init__(self):
        self.currentUser = None
    
    def signUp(self):
        print("\n --Sign Up--")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # یک دیکشنری میسازیم و تو لیست users ذخیره میکنیم
        user = {
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "wallet": 0.0,
            "cards": [],
            "tickets": []
        }

        # یک آبجکت ویژگی یا متدی با اسم مشخص شده داره یا نه
        # ایجاد لیست سراسری
        if not hasattr(self, "users"):
            self.users = []
        self.users.append(user)
        print("User registered successfully!")

    def _findeUser(self, username: str):
        '''
        return user dict by username or none if not found.
        '''
        if not hasattr(self, "users"):
            return None
        for u in self.users:
            if u["username"] == username:
                return u
        return None
        
    def login(self):
        print("\n --Login--")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = self._findeUser(username)
        if user is None:
            print("User not found. Please sign up first.")
            return
        if user["password"] != password:
            print("Wrong password!")
            return
        
        self.currentUser = user
        print(f"welcome, {user['name']}!")
        self.userMenu()

    def entryMenu(self):
        '''
        منوی ابتدایی: ثبت نام یا ورود
        '''
        while True:
            print("\n --User Entry--")
            print("1) Sign Up")
            print("2) Login")
            print("3) Exit")
            userChoice = input("> ").strip()

            if userChoice == "1":
                self.signUp()

            elif userChoice == "2":
                self.login()

            elif userChoice == "3":
                print("exit")
                break

            else:
                print("invalid option!")
    
    def userMenu(self):
        '''
        منوی کاربر بعد از ورود
        '''

        while True:
            print("\n --User Panel--")
            print("1) Buy ticket")
            print("2) Charge wallet")
            print("3) View transactions")
            print("4) Edit profile")
            print("5) Logout")
            userChoice = input("> ").strip()

            if userChoice == "1":
                print("Buying ticket")
            elif userChoice == "2":
                print("Charging wallet")
            elif userChoice == "3":
                print("Transactions")
            elif userChoice == "4":
                print("Editing profile")
            elif userChoice == "5":
                print("Logged out.")
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    panel = userPanel()
    panel.entryMenu()