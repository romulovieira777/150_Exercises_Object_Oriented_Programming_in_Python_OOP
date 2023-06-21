"""
Exercise No. 17

The following Doc class is implemented for storing text documents. Implement the __lt__() special method to compare Doc
instances. A class instances is 'smaller' than another instance when the string attribute is shorter.

Example:

    [IN]: doc1 = Doc('Finance')
    [IN]: doc2 = Doc('Education')
    [IN]: print(doc1 < doc2)

    [OUT]: True

Then create two instances of the Doc class for the following documents:

    - 'sport'
    - 'activity'

And assign to the variables:

    - doc1
    - doc2

In response, print the result of comparing these instances (perform doc1 < doc2).

Expected result:

    True
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

    def __lt__(self, other):
        return len(self.string) < len(other.string)


doc1 = Doc('sport')
doc2 = Doc('activity')

print(doc1 < doc2)
