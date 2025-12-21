import sqlite3
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

username = input("Enter Name :").strip()
email = input("Enter Email :").strip()
age = input("Enter Age :").strip()

if not username:
    print("Username cannot be empty")

elif '@' not in email or '.' not in email:
    print("Email must contain @ and .")
    
else:
    try:
        age = int(age)
        if age < 18:
            print("Age must be 18 or above.")
        else:
            try:
                cursor.execute(
                    "INSERT INTO users (username, email, age) VALUES (?, ?, ?)", (username,email,age)
                )
                connection.commit()
                print("User added successfully")

            except sqlite3.IntegrityError:
                print("Email already exists in database.")
    except ValueError:
        print("Age must be in Number.")

connection.close()
