"""
Exercise No. 03

A class called Laptop was implemented.

Implement a method in the Laptop class called display_attrs_with_values(), which displays the names of all the
attributes of the Laptop class with their values as shown below (attribute name -> attribute value).

Then create an instance named laptop with the following values:

    - brand = 'Dell'
    - model = 'Inspiron'
    - price = 3699

In response, call the display_attrs_with_values() method on the laptop instance.

Expected result:

    brand -> Dell
    model -> Inspiron
    price -> 3699
"""


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs_with_values(self):
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


laptop = Laptop('Dell', 'Inspiron', 3699)
laptop.display_attrs_with_values()
