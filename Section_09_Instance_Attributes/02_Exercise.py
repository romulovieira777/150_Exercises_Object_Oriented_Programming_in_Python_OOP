"""
Exercise No. 02

The Book class is defined. Create two instances of the Book class named book_1 and book_2. Then assign instance
attributes to these objects (using dot notation) as follows:

- to object book_1:
    - author = 'Dan Brown'
    - title = 'Inferno'

- to object book_2:
    - author = 'Dan Brown'
    - title = 'The Da Vinci Code'
    - year_of_publishment = 2003

In response, print the value of the __dict__ attribute of book_1 and book_2.

Expected result:

    {'author': 'Dan Brown', 'title': 'Inferno'}
    {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
"""


class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2 = Book()
book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

print(book_1.__dict__)
print(book_2.__dict__)
