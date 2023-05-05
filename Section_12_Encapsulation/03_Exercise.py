"""
Exercise No. 03

A class called Laptop was implemented. The __init__() method sets the value of the price protected attribute that stores
the price of the laptop (without any validation).

Create an instance of the Laptop class with a price of 3499 and try to set the price to -3000 using the set_price()
method. If an error is raised, print the error message to the console. Use a try ... except ... clause in your solution.

Expected result:

    The price attribute must be a positive int or float value.
"""


class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or float value.')
        self._price = value


laptop = Laptop(3499)

try:
    laptop.set_price(-3000)
except ValueError as error:
    print(error)
