from utils import database
import sqlite3

USER_CHOICE = """Enter:
- 'a' to add a new book to your list
- 'l' to show a list of your books 
- 'r' to mark your book as 'read'
- 'd' to delete a book and 
- 'q' to exit
Your choice:"""


database.create_book_table()

def menu():
    user_input = input(USER_CHOICE)
    while user_input.lower() != 'q':
        if user_input.lower() == 'a':
            ab()
        elif user_input.lower() == 'l':
            lb()
        elif user_input.lower() == 'r':
            rb()
        elif user_input.lower() == 'd':
            db()
        else:
            print("Unknown command, please try again")
        user_input = input(USER_CHOICE)


def ab():
    book_name = input("please enter a name of the book: ")
    book_author = input("please enter the author: ")
    try:
        database.add_book(book_name.lower(), book_author.lower())
    except sqlite3.IntegrityError:
        print("This author or book already exists, nothing added")
        return 0


def lb():
    try:
        for book in database.list_books():
            read = "Yes" if book['read'] else "No"
            print(f"{book['name']} by {book['author']}, read:{read}")
    except FileNotFoundError:
        print("Your list is empty, file doesn't exist")
        return 0
    except TypeError:
        print("Your list is empty")
        return 0
    except sqlite3.IntegrityError:
        print("This book already exists, nothing added")
        return 0




def rb():
    try:
        name = input("Enter a name of the book you want to mark as 'read': ")
        database.read_book(name.lower())
    except FileNotFoundError:
        print("Your list is empty, no books to mark as 'read'")
    except TypeError:
        print("Your list is empty, no books to mark as 'read'")



def db():
    name = input("Enter a name of the book you want to delete: ")
    database.delete_book(name.lower())


menu()




