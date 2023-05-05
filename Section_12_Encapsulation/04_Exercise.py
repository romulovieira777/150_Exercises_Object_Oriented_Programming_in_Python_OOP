"""
Exercise No. 04

A class called Laptop was implemented.

Add validation of the price attribute also at the stage of creating the instance (in __init__() method).

Then try ti create an instance if the Laptop class with a price of -3499. If an error is raised, print the error message
to the console. Use a try ... except ... clause in your solution.

Expected result:

    The price attribute must be a positive int or float value.
"""
# Solution I


class Laptop:

    def __init__(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        if not price > 0:
            raise ValueError('The price attribute must be a positive int or float value.')
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')
        if not value > 0:
            raise ValueError('The price attribute must be a positive int or float value.')
        self._price = value


try:
    laptop = Laptop(-3499)
except ValueError as error:
    print(error)


# Solution II
class Laptop:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self._price

    def set_price(self, value):

        if not isinstance(value, (int, float)):
            raise TypeError('The price attribute must be an int or float type.')

        if not value > 0:
            raise ValueError('The price attribute must be a positive int or float value.')
        self._price = value


try:
    laptop = Laptop(-3499)
except ValueError as error:
    print(error)
