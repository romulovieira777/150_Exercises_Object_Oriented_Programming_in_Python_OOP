"""
Exercise No. 05

The following classes are implemented:

    - Vehicle
    - LandVehicle
    - AirVehicle

Define a __display_info__() method in the Vehicle class to display the class name along with the value of the category
attribute. The method is supposed to work for all classes.

For example, the following code:

    instances = [Vehicle(), LandVehicle(), AirVehicle()]

    for instance in instances:
        print(instance)

returns:

    Vehicle -> land vehicle
    LandVehicle -> land vehicle
    AirVehicle -> air vehicle

Run the code below in response:

    instances = [Vehicle(), LandVehicle(), AirVehicle()]

    for instance in instances:
        print(instance)

Expected result:

    Vehicle -> land vehicle
    LandVehicle -> land vehicle
    AirVehicle -> air vehicle
"""
# Solution I


class Vehicle:
    def __display_info__(self):
        print(f"{self.__class__.__name__} -> {self.category}")

    @property
    def category(self):
        return 'land vehicle'


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    @property
    def category(self):
        return 'air vehicle'


instances = [Vehicle(), LandVehicle(), AirVehicle()]

for instance in instances:
    instance.__display_info__()


# Solution II
class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def display_info(self):
        print(f'{self.__class__.__name__} -> {self.category}')


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for vehicle in vehicles:
    vehicle.display_info()
