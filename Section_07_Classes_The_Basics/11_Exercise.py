"""
Exercise No. 11

Two empty classes are defined:

    - Model
    - View

Three objects were created (object1, object2, object3).

Using the built-in function isinstance() check whether the object1, object2 and object3 are instances of the Model class
or of the View class. Print the result to the console.

Expected result:

    True
    False
    False
"""


class Model:
    """This is a Model class."""
    pass


class View:
    """This is a View class."""
    pass


object1 = Model()
object2 = View()
object3 = View()

print(isinstance(object1, Model))
print(isinstance(object2, Model))
print(isinstance(object3, Model))
