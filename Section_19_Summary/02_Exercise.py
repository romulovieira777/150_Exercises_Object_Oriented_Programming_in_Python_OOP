"""
Exercise No. 02

The following Point class is given. Implement a reset() method that allows you to set the values of the x and y
attributes to zero. Then create an instance of the Point class with coordinates (4, 2) and print it to the console. Call
the reset() method on this instance to the console again.

Expected result:

    Point(x=4, y=2)
    Point(x=0, y=0)
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


point = Point(4, 2)
print(point)

point.reset()
print(point)
