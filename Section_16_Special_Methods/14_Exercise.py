"""
Exercise No. 14

The following Doc class is implemented for storing text documents. Implement the __add__() special method to add Doc
instances with a space character.

Example:

    [IN]: doc1 = Doc('Object')
    [IN]: doc2 = Doc('Oriented')
    [IN]: print(doc1 + doc2)

    [OUT]: Object Oriented

Then create two instances of the Doc class for the following documents:

    - 'Python'
    - '3.8'

in response, print the result of adding these instances to the console.

Expected result:

    Python 3.8
"""


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(f'{self.string} {other.string}')


doc1 = Doc('Python')
doc2 = Doc('3.8')

print(doc1 + doc2)
