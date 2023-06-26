"""
Exercise No. 07

A Vehicle class is given that has three instance attributes:

    - brand
    - color
    - year

Create a Car class that inherits from Vehicle class. Next, override the __init__() method so that the Car class in the
constructor takes four arguments:

    - brand
    - color
    - year
    - horsepower

And set them appropriately as instance attributes. Use super() in this case.

Then create following instances:

    - with the name vehicle and the attribute values: 'Tesla', 'red', 2020
    - with the name car and the attribute values: 'tesla', 'red', 2020, 300

In response, print the value of the __dict__ attribute of the vehicle and car instances.
"""


class Vehicle:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year


class Car(Vehicle):
    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower


vehicle = Vehicle('Tesla', 'red', 2020)
car = Car('Tesla', 'red', 2020, 300)

print(vehicle.__dict__)
print(car.__dict__)
