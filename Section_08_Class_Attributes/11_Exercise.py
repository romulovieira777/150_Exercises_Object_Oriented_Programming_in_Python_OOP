"""
Exercise No. 11

implement the HouseProject class with class attributes respectively:

    - number_of_floors = 3
    - area = 100

Then, in the HouseProject class implement a function (class callable attribute) called describe_project(), which
displays basic information about the project as follows:

    Floor number: 3
    Area: 100

In response, call describe_project() function.

Expected result:

    Floor number: 3
    Area: 100
"""


class HouseProject:
    number_of_floors = 3
    area = 100

    def describe_project(self):
        print(f'Floor number: {self.number_of_floors}')
        print(f'Area: {self.area}')


project = HouseProject()
project.describe_project()
