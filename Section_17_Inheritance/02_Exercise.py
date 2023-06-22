"""
Exercise No. 02

The following classes are implemented:

    - Container
    - PlasticContainer
    - MetalContainer
    - CustomContainer

Using the issubclass() built-in function, check if the class:

    - PlasticContainer
    - MetalContainer
    - CustomContainer

Are subclasses of the Container class. Print the result to the console as shown below:

    True
    True
    False
"""


class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class CustomContainer():
    pass


print(issubclass(PlasticContainer, Container))
print(issubclass(MetalContainer, Container))
print(issubclass(CustomContainer, Container))
