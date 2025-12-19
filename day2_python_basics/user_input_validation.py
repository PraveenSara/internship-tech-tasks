def validateUser():
    username = input("Enter your username : ")
    email = input("Enter Email :")

    try:
        age = int(input("Enter your current age : "))
    except ValueError:
        print("Age should be in number")
        return

    if age<18 or age>60:
        print("Age must be between 18 - 60")
        return

    if '@' not in email and '.' not in email:
        print("Email must contain @ and .")
        return

    if len(username)<5:
        print("Username atleast have 5 characters")
        return

    print('User registration successfully!')
validateUser()
