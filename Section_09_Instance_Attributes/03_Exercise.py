"""
Exercise No. 03

The Book class is defined.Two instances of the Book class named book_1 and book_2 was created. Then the instance
attributes were assigned to these objects (using dot notation), respectively:

- to object book_1:
    - author = 'Dan Brown'
    - title = 'Inferno'

- to object book_2:
    - author = 'Dan Brown'
    - title = 'The Da Vinci Code'
    - year_of_publishment = 2003

Then a books list was created. Create a loop to list all the attributes of the book_1 and book_2 instances with their
values as shown below (separate each instance with a line of 30 '-' characters as shown below).

Expected result:

    author -> Dan Brown
    title -> Inferno
    ------------------------------
    author -> Dan Brown
    title -> The Da Vinci Code
    year_of_publishment -> 2003
    ------------------------------
"""


class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]

# Solution I
for book in books:
    for key, value in book.__dict__.items():
        print(f'{key} -> {value}')
    print('-' * 30)


# Solution II
for book in books:
    for attr in book.__dict__:
        print(f'{attr} -> {getattr(book, attr)}')
    print('-' * 30)
