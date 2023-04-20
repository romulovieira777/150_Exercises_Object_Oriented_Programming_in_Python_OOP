"""
Exercise No. 04

A class named Laptop is defined below. Using the setattr() built-in function modify the value of attributes:

    - brand to 'Acer'
    - model to 'Predator'

In response, using the built-in function getattr() and print(), print the values of the brand and model attributes to
the console as shown below.

Expected result:

    brand: Acer
    model: Predator
"""


class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'


setattr(Laptop, 'brand', 'Acer')
setattr(Laptop, 'model', 'Predator')

print(f'brand: {getattr(Laptop, "brand")}')
print(f'model: {getattr(Laptop, "model")}')
