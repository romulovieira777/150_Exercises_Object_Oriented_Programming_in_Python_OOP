"""
Exercise No. 02

A class called Laptop was implemented.

Implement a method in the Laptop class called display_instance_attrs() that display the names of all the attributes of
the Laptop instance.

Then create an instance named laptop with the given attribute values:

    - brand = 'Dell'
    - model = 'Inspiron'
    - price = 3699

In response, call display_instance_attrs() method on the laptop instance.

Expected result:

    brand
    model
    price
"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_instance_attrs(self):
        for attr in self.__dict__:
            print(attr)


laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_instance_attrs()
