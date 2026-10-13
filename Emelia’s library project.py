import os

FileName = "Library.txt"
books = []

def load_books():
    if not os.path.exists(FileName):
        return
    
    with open(FileName, "r", encoding="uft_8") as file:
        for line in file:
            line= line.strip()
            if line:
                parts=lins.split("|")
                if len(parts)==4:
                    book_id, title , author , quantity=0
                    books.append({
                        "id": int(book_id),
                        "title":title,
                        "author":author,
                        "quantity": int(quantity)
                    })

def save_books():
    with open(FileName, "w", encoding="uft_8") as file:
        for book in books:
            file.write(f"{book['id']}|{book['title']}|{book['author']}|{book['quantity']}\n")

def add_book():
    title= input("Enter book title:")
    if not title:
        print("Plz enter the book title")
        return
    
    author = input("Enter author name:")
    
    try:
        quntity = int(input("Enter quntity:"))
    except ValueError:
        print("Plrase the correct number")
        return
        
    new_id = len(books) + 1
    
    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "quntity": quantity
    }
    
    books.append(book)
    save_books()
    print(f"The book {title} is added successfully")

def display_books():
    if not books:
        print("No books availabe in the Emelia's library")
        return
        
    for book in books:
        print(f"Id: {book['id']}| Title: {book['title']}| Author: {book['author']}| Quantit: {book['quantity']}")

def saerch_book():
    if not books:
        print("No Books in the Emelia's library to search")
        return
        
    try:
        book_id = int(input("Enter book Id first"))
        found = False
        
        for book in books:
            if book["id"] == book_id:
                print(f"Book Found: Id: {book['id']}| Title:{book['title']}| Author: {book['author']}| Quantity: {book['quantity']}")
                found = True
                break
                
        if not found:
            print("The book is not found")
    except ValueError:
        print("Plz enter the valid number")

def barrow_book():
    display_books()
    if not found:
        return
        
    try:
        book_id = int(input("Enter book Id plz:"))
        found = False
        
        for book in books:
            if book['id'] == book_id:
                found = True
                if book['quantity'] > 0:
                    book['quantity'] -= 1
                    save_books()
                    print(f"You have borrowed the '{book['title']}' , the quantity '{book['quantity']}' ")
                else:
                    print("Sorry the book is out of Emelia's library stock")
                break
                
        if not found:
            print("The book is not found <3.")
    except ValueError:
        print("Please enter a valid number <3.")

def main_menu():
    load_books()
    while True:
        print("1.Display book")
        print("2. add book")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Exist")
        
        choice= input("(1-5) choose: ").strip()
        
        if choise == '1':
            display_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            print("Exiting, are changes are saved <3.")
            break
        else:
            print("Invalid choice, ypu can try again<3.")

main_menu()
