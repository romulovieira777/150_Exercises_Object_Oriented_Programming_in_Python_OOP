"""
Exercise No. 06

The implementation of the Container class is given:

    class Container:
        '''This is a Container class.'''

Display the value of the __module__ attribute of the Container class to the console.

Note:
    The solution that the user provides is in a file named exercise.py, while the checking code (which is invisible to
the user) is executed from a file named evaluate.py from the level where the Container class is imported. Therefore,
instead of the name of the module __main__, the response will be the name of the module in which this class is
implemented, exercise in this case.

Expected result:

    exercise
"""


class Container:
    """This is a Container class."""
    pass


print(Container.__module__)
