"""
Exercise No. 03

An implementation of the Laptop class is given. Implement a method in the Laptop class called display_private_attrs()
that displays the names of all private attributes of the instance. Then create an instance with the given arguments:

    - 'Acer'
    - 'Predator'
    - 'AC-100'
    - 5490
    - 0.2

and assign it to the variable laptop. In response, call display_private_attrs() on the laptop instance.

Expected result:

    _Laptop__price
    _Laptop__margin
"""


# Solution I

class Laptop:
    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self.model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith('_Laptop__'):
                print(attr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()


# Solution II
class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()
