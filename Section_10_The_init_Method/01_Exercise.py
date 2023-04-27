"""
Exercise No. 01

Implement a class called Laptop that sets the following instance attributes when creating an instance:

    - brand
    - model
    - price

Then create an instance named Laptop with the following attribute values:

    - brand = 'Acer'
    - model = 'Predator'
    - price = 5490

Tip:
    Use the special method __init__().

In response, print the value of the __dict__ attribute of the laptop instance.

Expected result:

    {'brand': 'Acer', 'model': 'Predator', 'price': 5490}
"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


laptop = Laptop('Acer', 'Predator', 5490)

print(laptop.__dict__)
