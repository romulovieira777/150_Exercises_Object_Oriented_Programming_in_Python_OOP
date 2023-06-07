"""
Exercise No. 04

Implement a class named Rectangle which will have the following properties:

    - width
    - height

The width and height of rectangle, respectively (for reading and for modification). Also add a property named area that
stores the area if the rectangle (read-only). This property should be computed only at the first reading or after
modifying any of the rectangle sides. Skip attribute validation.

Then create an instance named rectangle with a width = 3 and a height = 4 and print the information about the rectangle
instance to the console as shown below.

Expected result:

    width: 3, height: 4 -> area: 12
"""


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
        self._area = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area


rectangle = Rectangle(3, 4)
print(f'width: {rectangle.width}, height: {rectangle.height} -> area: {rectangle.area}')
