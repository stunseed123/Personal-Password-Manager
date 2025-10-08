import sqlite3
import hashlib
import random

conn = sqlite3.connect('password_database1.db')
c = conn.cursor()
conn.commit()

def create_individual(password_unique: str, name: str):
    try:
        id_unique = str(random.randint(100000, 999999))
        user_table = f"user_{id_unique}"
        data_table = f"data_{id_unique}"

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS "{user_table}" (
                main_password TEXT,
                name TEXT
            )
        ''')
        c.execute(f'INSERT INTO "{user_table}" (main_password, name) VALUES (?, ?)', (password_unique, name))

        c.execute(f'''
            CREATE TABLE IF NOT EXISTS "{data_table}" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                site TEXT,
                name TEXT,
                password TEXT
            )
        ''')

        conn.commit()
        print(f'Successfully Signed Up! Your ID is: {id_unique}')
    except Exception as e:
        print("Sign-up Error:", e)

def get_individual(id_unique: str):
    try:
        user_table = f"user_{id_unique}"
        c.execute(f'SELECT * FROM "{user_table}"')
        data = c.fetchall()
        if data:
            return data[0][0]
        else:
            print('INVALID ID')
    except Exception as e:
        print("Login Error:", e)

def store_user_data(id_unique: str, site: str, name: str, password: str):
    try:
        data_table = f"data_{id_unique}"
        c.execute(f'INSERT INTO "{data_table}" (site, name, password) VALUES (?, ?, ?)', (site, name, password))
        conn.commit()
    except Exception as e:
        print("Data Entry Error:", e)

def view_data(id_unique: str, condition: str = None):
    try:
        data_table = f"data_{id_unique}"
        c.execute(f'SELECT * FROM "{data_table}"')
        data = c.fetchall()

        if data:
            print("ID  |   SITE NAME    |        NAME        |  PASSWORD")
            print("-----------------------------------------------------------")
            for row in data:
                if condition is None:
                    print(f"{row[0]}   |  {row[1]}  |  {row[2]}  |  {row[3]}")
                elif row[2] == condition:
                    print(f"{row[0]}   |  {row[1]}  |  {row[2]}  |  {row[3]}")
        else:
            print("No data found")
    except Exception as e:
        print("View Error:", e)

def main():
    main_choice = input("Do you want to Login or Sign up? (1 = Login, 2 = Sign Up): ")

    if main_choice == "2":
        name = input("Please enter your name: ")
        password = input("Create your password: ")
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        create_individual(password_hash, name)
        main()

    elif main_choice == "1":
        ID_ = input("Enter your ID: ")
        password_check = input('Enter your password: ')
        password_check_hash = hashlib.sha256(password_check.encode('utf-8')).hexdigest()

        if get_individual(ID_) == password_check_hash:
            print("Login successful!")
            while True:
                choice = input("Enter Data (1), View Data (2), or Exit (3): ")
                if choice == "1":
                    site_name = input("Site Name: ")
                    username = input("Username: ")
                    password = input("Password: ")
                    if not username or not password:
                        print("You can't leave either input blank!")
                    else:
                        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
                        store_user_data(ID_, site_name, username, password_hash)

                elif choice == "2":
                    search = input("Search by username (leave blank for all): ")
                    view_data(ID_, search if search else None)

                elif choice == "3":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice.")

        else:
            print("Wrong password or invalid ID.")

    else:
        print("Invalid selection.")
        main()

if __name__ == '__main__':
    main()
    conn.close()
