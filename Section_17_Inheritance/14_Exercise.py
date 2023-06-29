"""
Exercise No. 14

The following classes are defined. Add the __ijnit__() method to the Person class, which sets three attributes:

    - first_name
    - last_name
    - age

Then create an instance of the Worker class passing the following arguments:

    - 'John'
    - 'Doe'
    - 35

In response, print the value of the __dict__ attribute of this instance.

Expected result:

    {'first_name': 'John', 'last_name': 'Doe', 'age': 35}
"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:
    pass


class Worker(Person, Department):
    pass


worker = Worker('John', 'Doe', 35)
print(worker.__dict__)