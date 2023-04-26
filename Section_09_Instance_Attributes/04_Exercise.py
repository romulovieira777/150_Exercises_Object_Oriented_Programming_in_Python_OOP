"""
Exercise No. 04

The book class is defined. A list books_data is also given.

    books_data = [
        {
            'author': 'Dan Brown',
            'title': 'Inferno'
        },
        {
            'author': 'Dan Brown',
            'title': 'The Da Vinci Code',
            'year_of_publishment': 2003
        },
    ]

Based on this data, create two instances of the Book class, where the instance attributes will be the keys from the
given dictionaries (books_data list) with their corresponding values.

In response, print the __dict__ attributes of the objects to the console as shown below.

Expected result:

    {'author': 'Dan Brown', 'title': 'Inferno'}
    {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
"""


class Book:
    language = 'ENG'
    is_ebook = True


books_data = [
    {
        'author': 'Dan Brown',
        'title': 'Inferno'
    },
    {
        'author': 'Dan Brown',
        'title': 'The Da Vinci Code',
        'year_of_publishment': 2003
    },
]

# Solution I
book_1 = Book()
book_2 = Book()

for key, value in books_data[0].items():
    setattr(book_1, key, value)

for key, value in books_data[1].items():
    setattr(book_2, key, value)

print(book_1.__dict__)
print(book_2.__dict__)


# Solution II
books = []

for book_data in books_data:
    book = Book()
    for key, value in book_data.items():
        setattr(book, key, value)
    books.append(book)

for book in books:
    print(book.__dict__)
