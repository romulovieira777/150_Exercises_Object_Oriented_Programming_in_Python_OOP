"""
Exercise No. 02

An implementation of the Figure and Square classes is given. Add an abstract method called perimeter() to the Figure
class, then implement it in the Square class. Then perimeter() method should return the perimeter of the square.

Create an instance of the Square class with side 10 and using the area() and perimeter() methods display the area and
perimeter of the created instance to the console.

Expected result:

    100
    40
"""
from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Figure):

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4


square = Square(10)
print(square.area())
print(square.perimeter())
