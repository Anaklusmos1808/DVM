
import logging
from terminaltables import AsciiTable


logging.basicConfig(filename="Logs.log",
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class User:
    def __init__(self, role, name='Test'):
        assert role == 'Librarian' or role == 'Basic User', "please enter either Librarian or Basic User as a role"

        self.__role = role
        self.name = name

    @property
    def role(self):
        return self.__role


class Book:
    def __init__(self, name, author, ISBN):
        self.__name = name
        self.__author = author
        self.__ISBN = ISBN
        self.borrowed = False
        self.reserved = False

    def borrow_book(self, user, shelf, isbn):
        self.borrowed = True
        logger.info(f'{self.name} was borrowed by {user.name}')
        for i in shelf.shelf_arr:
            if i.ISBN == isbn:
              shelf.shelf_arr.remove(i)
              shelf.borrowed_arr.append(i)

        

    def return_book(self, shelf, isbn, user):
        self.borrowed = False
        logger.info(f'{self.name} has been returned by {user.name}')
        for i in shelf.borrowed_arr:
            if i.ISBN == isbn:
                shelf.shelf_arr.append(i)
                shelf.borrowed_arr.remove(i)

    def reserve_book(self, user):
        self.reserved = True
        logger.info(f'{self.name} has been reserved for {user.name}')

    @property
    def name(self):
        return self.__name

    @property
    def ISBN(self):
        return self.__ISBN

    @property
    def author(self):
        return self.__author


class Shelf:
    def __init__(self, books):
        assert type(books) == list, "please Enter the books as a list"

        self.shelf_arr = books
        self.borrowed_arr = list()

    def show_catalogue(self):
        if len(self.shelf_arr) > 0:
            table_dat = [
                ['NAME', 'AUTHOR', 'ISBN']
            ]

            for book in self.shelf_arr:
                table_dat.append([str(book.name), book.author, str(book.ISBN)])

            table = AsciiTable(table_dat)
            print(table.table)

        else:
            print('the shelf is empty!')

    def add_book(self, user: User):  
        try:
            if user.role == 'Librarian':
                name = str(input('Name of the book to be added: '))
                author = str(input('Name of the author: '))
                isbn = input('ISBN code: ')

                self.shelf_arr.append(Book(name, author, isbn))

                print(f'{name} has been successfully added to the shelf')

            else:
                print('you do not have access to this method')

        except AttributeError:
            print('please try again, enter a valid username')

    def remove_book(self, user: User, book_del):  
        try:
            if user.role == 'Librarian':
                for i in self.shelf_arr:
                    if i.ISBN == book_del:
                        self.shelf_arr.remove(i)

                print(f'ISBN {book_del} successfully removed from shelf')

            else:
                print('you do not have access to this method')

        except AttributeError:
            print('please try again, enter a valid username')

    def get_books_count(self):
        print(f"the number of books in this shelf are: {len(self.shelf_arr)}")

    def populate_books(self):
        import _script
        _script.populate(self)


