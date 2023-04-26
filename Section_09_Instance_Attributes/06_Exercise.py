"""
Exercise No. 06

The Book class is defined. Implement a method called set_title() that sets an instance attribute named title. Before
setting the value, check if it's an object of str type, if not raise a TypeError with the following message:

    'The value of the title attribute must be of str type.'

Then create an instance of the Book class named book and set the title attribute to 'Inferno' using the set_title()
method.

In response, print the value of the title attribute of the book instance.

Expected result:

    Inferno
"""


class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, title):
        if not isinstance(title, str):
            raise TypeError('The value of the title attribute must be of str type.')
        self.title = title


book = Book()

book.set_title('Inferno')

print(book.title)
