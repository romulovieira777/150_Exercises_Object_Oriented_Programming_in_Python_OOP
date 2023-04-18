"""
Exercise No. 10

Define two empty classes named:

    - Model
    - View

Then create two instances (one for each class):

    - model for the Model class
    - view for the View class

Using the built-in function isinstance() check whether the model and view objects are instances of the Model class.

Print the result to the console.

Expected result:

    True
    False
"""


class Model:
    """This is a Model class."""
    pass


class View:
    """This is a View class."""
    pass


model = Model()
view = View()

print(isinstance(model, Model))
print(isinstance(view, Model))
