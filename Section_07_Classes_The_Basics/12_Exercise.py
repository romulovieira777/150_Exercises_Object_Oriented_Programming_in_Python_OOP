"""
Exercise No. 12

Implement an empty class named Container. Then create an instance of this class named container. In response, display
the type of dictionary attribute __dict__ for the Container class and for the container instance.

Expected result:

    <class 'mappingproxy'>
    <class 'dict'>
"""


class Container:
    """This is a Container class."""
    pass


container = Container()

print(type(Container.__dict__))
print(type(container.__dict__))
