import logging
from app import books

logger = logging.getLogger('scrapper_menu')

USER_CHOICE = """

Enter one of the following:
-'b' to look at best books
-'c' to look at the cheapest books
-'n' to just get the next available book
-'q' to exit   

"""


def print_best_books():
    logger.info('Finding best books by rating...')
    five_star_books = sorted(books, key=lambda x: x.star_rating * -1)[:10]
    for book in five_star_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding the cheapest books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def nextb():
    logger.info('Generating next book...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': nextb
}


def menu():
    inp = input(USER_CHOICE)
    while inp != 'q':
        if inp in ('b', 'c', 'n'):
            user_choices[inp]()
        else:
            print("Please choose a valid command")
        inp = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()
