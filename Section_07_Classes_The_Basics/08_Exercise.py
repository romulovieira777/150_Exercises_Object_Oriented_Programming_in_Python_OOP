"""
Exercise No. 08

An implementation of the Container class is given:

    class Container:
        '''This is a Container class.'''

Create an instance of the Container class and assign to the container variable. Then print the __class__ attribute value
of the container instance.

Note:
    The solution that the user provides is in a file named exercise.py, while the checking code (which is invisible to
the user) is executed from a file named evaluate.py from the level where the Container class is imported. Therefore,
instead of the name of the module __main__, the response will be the name of the module in which this class is
implemented, exercise in this case.

Expected result:

    <class 'exercise.Container'>
"""


class Container:
    """This is a Container class."""
    pass


container = Container()
print(container.__class__)
