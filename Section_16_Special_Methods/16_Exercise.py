"""
Exercise No. 16

The following Doc class is implemented for storing text documents. Implement the __eq__() special method to compare Doc
instances. Class instances are equal when they have identical string attribute values.

Example:

    [IN]: doc1 = Doc('Finance')
    [IN]: doc2 = Doc('Finance')
    [IN]: print(doc1 == doc2)

    [OUT]: True

Then create two instances of the Doc class for the following documents:

    - 'Python'
    - '3.8'

in response, print the result of comparing these instances.

Expected result:

    False
"""


class Doc:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __eq__(self, other):
        return self.string == other.string


doc1 = Doc('Python')
doc2 = Doc('3.8')

print(doc1 == doc2)
