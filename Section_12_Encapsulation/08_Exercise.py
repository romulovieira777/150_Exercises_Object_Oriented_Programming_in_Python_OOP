"""
Exercise No. 08

Implement a class named Person that has two protected attributes: first_name and last_name, respectively. Next implement
methods named get_first_name(), set_first_name(), get_last_name(), set_last_name(), which allows you to read and modify
the value of the first_name and last_name protected attributes.

Then, using the methods get_first_name(), set_first_name(), get_last_name(), set_last_name() and the property class (do
it in the standard way) create properties: first_name and last_name (properties read and modify).

Create an instance of the Person class with the following values:

    - first_name = 'John'
    - last_name = 'Dow'

Then print the values of these attributes to the console as shown below.

Using the dot notation, modify the attribute values for this instance, respectively:

    - first_name to the value 'Tom'
    - last_name to the value 'Smith'

In response, print the __dict__ attribute of the created instance to the console.

Expected result:

    John
    Dow
    {'_first_name': 'Tom', '_last_name': 'Smith'}
"""


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    first_name = property(fget=get_first_name, fset=set_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)


person = Person('John', 'Dow')

print(person.first_name)
print(person.last_name)

person.first_name = 'Tom'
person.last_name = 'Smith'

print(person.__dict__)
