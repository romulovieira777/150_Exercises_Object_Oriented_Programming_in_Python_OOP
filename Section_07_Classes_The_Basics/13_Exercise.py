"""
Exercise No. 13

Two empty classes are defined:

    - Model
    - View

Using the built-in function issubclass() check if the classes Model and View are derived classes (subclasses) of the
built-in object class.

Expected result:

    True
    True
"""


class Model:
    """This is a Model class."""
    pass


class View:
    """This is a View class."""
    pass


print(issubclass(Model, object))
print(issubclass(View, object))
