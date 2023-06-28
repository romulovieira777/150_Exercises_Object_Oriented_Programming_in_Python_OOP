"""
Exercise No. 09

The Vehicle and Car classes are listed below. Extend the display_attrs() method in the Car class so that the following
information is displayed before displaying the attributes: 'Calling from class: Car' and then the rest of the attributes
with their values. Use super() for this. For example, for the Car class:

    car = Car('Tesla', 'red', 2020, 190)
    car.display_attrs()

Returns:

    Calling from class: Car
    brand -> Tesla
    color -> red
    year -> 2020
    horsepower -> 190

Then create an instance of the class Car named car with attribute values: 'Tesla', 'black', 2018, 260.

In response, call display_attrs() on the car instance.

Expected result:

    Calling from class: Car
    brand -> Tesla
    color -> black
    year -> 2018
    horsepower -> 260
"""


class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        for key, value in self.__dict__.items():
            print(f'{key} -> {value}')


class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower

    def display_attrs(self):
        print(f'Calling from class: {self.__class__.__name__}')
        super().display_attrs()


car = Car('Tesla', 'black', 2018, 260)
car.display_attrs()
