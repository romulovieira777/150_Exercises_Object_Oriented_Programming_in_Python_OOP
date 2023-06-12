"""
Exercise No. 05

A class named Person is given. Modify the __init__() method so that you can set two instance attributes: first_name and
last_name (bare attributes, without any validation).

Create two instances of the Person class. Then call the count_instances() class method and print result to the console.

Expected result:

    2
"""


class Person:
    instances = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(cls.instances)


person_1 = Person('John', 'Doe')
person_2 = Person('Mike', 'Smith')

print(Person.count_instances())
