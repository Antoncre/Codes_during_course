

books = []


def add_book(book_name, book_author):
    books.append({'name': book_name, 'author': book_author, 'read': False})


def list_books():
    for book in books:
        if book['read'] is False:
            print(F"Name:{book['name'].title()} |Author:{book['author'].title()}")
        if book['read'] is True:
            print(F"Name:{book['name'].title()} |Author:{book['author'].title()} |*already read*")


def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True
        else:
            pass


def delete_book(name):
    global books
    books = [book for book in books
             if book['name'] != name
             ]