"""
Exercise No. 15

The following classes are defined. Add the __init__() method to the Departament class that sets the following attributes:

    - dept_name (department name)
    - short_dept_name (department short name)

Then create an instance of the Departament class with arguments:

    - 'Information Technology'
    - 'IT'

In response, print the value of the __dict__ attribute of this instance.

Expected result:

    {'dept_name': 'Information Technology', 'short_dept_name': 'IT'}
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):
    pass


dept = Department('Information Technology', 'IT')
print(dept.__dict__)
