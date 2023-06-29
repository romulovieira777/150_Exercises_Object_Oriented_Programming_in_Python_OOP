"""
Exercise No. 08

The Vehicle and Car class are listed below. Implement a method named display_attrs() in the base class Vehicle, which
displays the instance attributes and their values. For example, for the Vehicle class:

    vehicle = Vehicle('Tesla', 'red', 2020)
    vehicle.display_attrs()

    brand -> Tesla
    color -> red
    year -> 2020

And for the Car class:

    car = Car('Tesla', 'red', 2020, 190)
    car.display_attrs()

    brand -> Tesla
    color -> red
    year -> 2020
    horsepower -> 190

Then create an instance of the Car class named car with attribute values: 'Opel', 'black', 2018, 160.

In response, call display_attrs() on the car instance.

Expected result:

    brand -> Opel
    color -> black
    year -> 2018
    horsepower -> 160
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


car = Car('Opel', 'black', 2018, 160)
car.display_attrs()
