"""
Exercise No. 15

The following Hashtag class is implemented for storing text documents - hastags. Implement the __add__() special method
to add (concatenate) Hashtag instances using a space character as shown below (take into account the appropriate number
of '#' characters at the beginning of the new object).

Example:

    [IN]: hashtag1 = Hashtag('sport')
    [IN]: hashtag2 = Hashtag('travel')
    [IN]: print(hashtag1 + hashtag2)

    [OUT]: #sport #travel

Then create three Hashtag instances for the following text documents:

    - python
    - developer
    - oop

in response, print the result of adding these instances.

Expected result:

    #python #developer #oop
"""


class Hashtag:
    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(f'{self.string[1:]} {other.string}')


hashtag1 = Hashtag('python')
hashtag2 = Hashtag('developer')
hashtag3 = Hashtag('oop')

print(hashtag1 + hashtag2 + hashtag3)
