print("1. Add User\n2. View Users\n3. Search User by Email\n4. Exit")
try:
    choice = int(input("Enter your choice :"))
except ValueError:
    print("choice should be in number (1 - 4)")

while choice < 4:
    
    if choice == 1:
        def add_users():
            username = input("Enter your name :")
            age = int(input("Enter your age :"))
            email = input("Enter your Email :")

            if age<18 or age>60:
                print("Age must between 18 - 60")
                return

            if '@' not in email or '.' not in email:
                print('Email must contail @ and .')
                return

            if len(username)<5:
                print("usename atleast contain 5 charchaters")
                return

            with open("users.txt","a+") as f:
                f.seek(0)
                if f.read():
                    f.write('\n')
                
                f.write(f"{username}, {age}, {email}")

        add_users()

    if choice == 2:
        def view_users():
            try:
                with open("users.txt","r") as f:
                    content = f.read()
                    print(content)
                f.close()
            except Exception as e:
                print(f"An error occurred: {e}")

        view_users()

    if choice == 3:
        def search_user():
            search_email = input("Enter the email you want to search :")
            
            found = False
            
            with open("users.txt","r") as f:
                for line in f:
                    sep_line = line.strip().split(', ')
                    if search_email == sep_line[2]:
                        print(f"Name : {sep_line[0]}, Age : {sep_line[1]}")
                        found = True
                        break

            if not found:
                print("Email not found")
        search_user()

    choice = int(input("Enter your choice :"))

else:
    print('You Exited!')
        
                
                
