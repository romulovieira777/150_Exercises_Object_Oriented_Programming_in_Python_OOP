"""
Exercise No. 05

A class called Rectangle is given. Add a property called perimeter, which stores the perimeter of the rectangle
(read-only). The perimeter property should be computed only at the first reading or after modifying any of the sides of
the rectangle. Skip attribute validation.

Then create an instance named rectangle with a width = 3 and a height = 4 and print the information about the rectangle
instance to the console as shown below.

Expected result:

    width: 3, height: 4 -> perimeter: 14
"""


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self._area = None
        self._perimeter = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: float):
        self._width = value
        self._area = None
        self._perimeter = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: float):
        self._height = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._width * self._height
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * (self._width + self._height)
        return self._perimeter


rectangle = Rectangle(3, 4)
print(f'width: {rectangle.width}, height: {rectangle.height} -> perimeter: {rectangle.perimeter}')
