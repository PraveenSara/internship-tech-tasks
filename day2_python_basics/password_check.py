def passwordCheck():

    password = input("Enter password : ")

    if len(password)<8:
        print("Password atleast contain 8 characters")
        return

    has_number = False
    for ch in password:
        if ch.isdigit():
            has_number = True
            break

    if not has_number:
        print("Password atleas contail 1 number")
        return

    has_special = False
    for ch in password:
        if ch in "!@#$%&":
            has_special = True
            break

    if not has_special:
        print("Password atleas contail 1 special character")
        return

    print("password is strong!")

passwordCheck()
