"""
Exercise No. 01

Implement a class named Circle that will have the protected instance attribute radius - the radius of the circle (
readable and modifiable property). Use the @property decorator.

Then create an instance named circle with radius=3.

In response, display the __dict__ attribute of circle instance.

Expected result:

    {'_radius': 3}
"""


class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: float):
        self._radius = value


circle = Circle(3)
print(circle.__dict__)
