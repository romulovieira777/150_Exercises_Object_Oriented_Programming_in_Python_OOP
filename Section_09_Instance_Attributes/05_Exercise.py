"""
Exercise No. 05

The Book class is defined. Implement a method called set_title() that allows you to set an instance attribute called
title (without validation). Then create an instance of the Book class named book and set the title attribute to
'Inferno' using the set_title() method.

In response, print the value of the title attribute of the book instance.

Expected result:

    Inferno
"""


class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        self.title = title


book = Book()

book.set_title('Inferno')

print(book.title)
