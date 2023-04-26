"""
Exercise No. 07

The book class is defined. A method called set_title() was implemented that allows you to set an instance attribute
called title. Create an instance of the Book class named book. Then, using the try ... except ... TypeError. print the
error message to the console.

Expected result:

    The value of the title attribute must be of str type.
"""


class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError('The value of the title attribute must be of str type.')
        self.title = title


book = Book()

try:
    book.set_title(123)
except TypeError as error:
    print(error)
