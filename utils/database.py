from .database_connection import Database_connection
"""
Concerned with storing and retrieving books from a database.
"""




#def js_err():
#    try:
#        with open(books_file, 'r') as file:
#            return json.load(file)
#    except json.JSONDecodeError:
#        return 0
#    except FileNotFoundError:
#        return 0


def create_book_table():
    with Database_connection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(book_name, book_author):
    with Database_connection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (book_name, book_author))


def list_books():
    with Database_connection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def read_book(name):
    with Database_connection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


#def _save_all_books(books):
#    with open(books_file, 'w') as file:
#       json.dump(books, file)


def delete_book(name):
    with Database_connection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))