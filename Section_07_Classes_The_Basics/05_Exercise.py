"""
Exercise No. 05

The implementation of the Container class is given:

    class Container:
        '''This is a Container class.'''

Display all __dict__ attribute keys of the Container class to the console.

Expected result:

    dict_keys(['__module__', '__doc__', '__dict__', '__weakref__'])
"""


class Container:
    """This is a Container class."""
    pass


print(Container.__dict__.keys())
