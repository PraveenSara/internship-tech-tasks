import sqlite3

def view_all_users(cursor):
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    if not users:
        print("No users found.")

    else:
        for user in users:
            print(f"ID : {user[0]} | Name : {user[1]} | Email : {user[2]} | Age : {user[3]}")
def search_user_by_email(cursor):
    email = input("Enter Email to search :").strip()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user:
        print("User found.")
        print(f"Name : {user[1]}")
        print(f"Email : {user[2]}")
        print(f"Age : {user[3]}")
    else:
        print("User not found.")

def main():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    print("1.View all users.")
    print("2.Search user by Email.")
    print("3.Exit")

    while True:
        try:
            choice = int(input("Enter choice :"))
        except ValueError:
            print("choice must be a number.")
            continue

        if choice == 1:
            view_all_users(cursor)

        elif choice == 2:
            search_user_by_email(cursor)

        elif choice == 3:
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

    connection.close()

main()
