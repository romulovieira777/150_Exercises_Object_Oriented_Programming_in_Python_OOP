"""
Exercise No. 07

A class called Car was implemented that sets the following instance attributes when creating an instance:

    - brand
    - model
    - price
    - type_of_car, by default 'sedan'

Then create an instance named of this named car with the given values:

    - brand = 'BMW'
    - model = 'X3'
    - price = 200000
    - type_of_car = 'SUV'

In response, print the values of the __dict__ attribute of the car instance.

Expected result:

    {'brand': 'BMW', 'model': 'X3', 'price': 200000, 'type_of_car': 'SUV'}
"""


class Car:
    def __init__(self, brand, model, price, type_of_car=None):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car if type_of_car else 'sedan'


car = Car('BMW', 'X3', 200000, 'SUV')

print(car.__dict__)
