from utils import database_strt

USER_CHOICE = """Enter:
- 'a' to add a new book to your list
- 'l' to show a list of your books 
- 'r' to mark your book as 'read'
- 'd' to delete a book and 
- 'q' to exit
Your choice:"""
def menu():
    user_input = input(USER_CHOICE)
    while user_input.lower() != 'q':
        if user_input.lower() == 'a':
            book_name = input("please enter a name of the book: ")
            book_author = input("please enter the author: ")
            database_strt.add_book(book_name.lower(), book_author.lower())
            return menu()
        elif user_input.lower() == 'l':
            database_strt.list_books()
            return menu()
        elif user_input.lower() == 'r':
            name = input("Enter a name of the book you want to mark as 'read': ")
            database_strt.read_book(name.lower())
            return menu()
        elif user_input.lower() == 'd':
            name = input("Enter a name of the book you want to delete: ")
            database_strt.delete_book(name.lower())
            return menu()
        else:
            print("Unknown command, please try again")
            return menu()


menu()
exit()