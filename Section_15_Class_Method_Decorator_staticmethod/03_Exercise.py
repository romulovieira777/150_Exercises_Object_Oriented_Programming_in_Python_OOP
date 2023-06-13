"""
Exercise No. 03

Complete the implementation of the Book class. In the __init__() method, set the bare attributes of the instance with
names:

    - title
    - author
    - book_id

Set the instance book_id attribute using the uuid module. Exactly the uuid.uuid4() function from this module.

An example of using this function:

    import uuid

    str(uuid.uuid4().fields[-1])[:6]

Returns a 6-element string. This will be the value of the book_id attribute.

Using the above code, create a static method of the Book class (use the @staticmethod decorator) called get_id(), which
will generate a 6-digit str object (the value of the book_id field).

Then create an instance of the class named book1 with the following arguments:

    - title = 'inferno'
    - author = 'Dan Brown'

In response, print all the __dict__ attribute keys of book1 to the console.

Expected result:

    dict_keys(['book_id', 'title', 'author'])
"""
import uuid


class Book:
    def __init__(self, title, author):
        self.book_id = self.get_id()
        self.title = title
        self.author = author

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


book1 = Book('inferno', 'Dan Brown')
print(book1.__dict__.keys())
