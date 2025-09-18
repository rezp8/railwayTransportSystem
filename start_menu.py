from admin import Admin

def start_menu():
    while True:
        print("Khosh Amadid!")
        print("1. Admin")
        print("2. Karmand")
        print("3. Karbar")
        print("4. Khoroj")
        print("------------------------")
        choose = input("Koja Beram? ")
        
        if choose == "1":
            print("Admin Khosh oomadi!")
            select = Admin()
            if select.log_in():
                select.admin_panel()
                
        elif choose == "2":
            #waiting for published
            print("Karmand Khosh oomadi!")
            print("Coming Soon")
            
        elif choose == "3":
            #waiting for published
            print("Karbar Khoosh oomadi!")
            print("Coming Soon")
            
        elif choose == "4":
            print("Khoda Negahdar")
            break
        else:
            while True:
                print("Vorodi Dade Shode Dorost Namibashad")
                failed = input("1. Talash Dobare/ 2. Khoroj Az Barname ")
                if failed == "1":
                    print("------------------------")
                    break
                elif failed == "2":
                    exit()
                else:
                    print("------------------------")  
                
                    
            

        
if __name__ == "__main__":
    start_menu()   