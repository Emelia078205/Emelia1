import sqlite3
conn = sqlite3.connect("cntacts.db")
cursor = conn.cursor()

cursor.execute("""CREAT TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY
    name TEXT NOT NULL
    phone TEXT NOT NULL
    email TEXT
)
""")

conn.commit()

def add_contact():
    name = ("Enter name:").strip()

    if not name:
        print("Plz enter the name<3.")
        return

    phone = input("Enter the phone plz:")

    if not phone:
        print("Enter the phone<3.")
        email = input("Enter email (optional):").strip()
        cursor.execute("INSERT INTO contacts(id,name,phone,email)Values(?,?,?,?), ('id','name','phone','email')")

        conn.commit()
        print(f"Conact'{name}' is added successfully")

def display_contacts():
    cursor.ececute("SELECT*FROM contacts")
    rows = cursor.fetchall()

    if not rows:
        print(f"ID:{row[0]}|Name:{row[1]} | Phone: {row[2]}| Email: {row[3]}")

def search_conact():
    search_name = input("Enter thew to search for<3.")
    cursoe.execute = ("SELSECT * FROM contacts WHERE name LIKE?", ("%" + query + "%"))
    rows = cursor.fetchall()

    if not rows:
        print("Name cannot found.")
        return

    for row in rows:
        print(f"ID:{row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")

def delete_contact():
    try:
        contact_id = int(input("Enter the Id of the contact:"))
        cursor.execute = ("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        print("Contact is deleted<3.")
    except ValueError:
        print("There is a wrong in Id, plz try again<3.")

def main_menu():
    print("1. Display Contacts")
    print("2. Ad Contacts")
    print("3. Search Contacts")
    print("4. delete Contacts")
    print("5. Exit")

    choice = input("(1-5) Choose:")

    if choice == '1':
        display_contact():
    if choice == '2':
        add_contact()
    if choice == '3':
        search_contact()
    if choice == '4':
        delete_contact()
    if choice == '5':
        conn.close()
        break
    else:
        print("Invalid choice, chooce a right number<3.")

main_menu()