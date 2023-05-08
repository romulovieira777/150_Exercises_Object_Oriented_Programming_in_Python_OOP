"""
Exercise No. 06

Implement a class named Person that has two protected attributes named first_name and last_name, respectively. Then
implement methods named get_first_name() and get_last_name(), which reads the protected attributes: first_name and
last_name.

Then, using the get_first_name() and get_last_name() methods and the property class (do it in the standard way) create
two properties named first_name and last_name (read-only properties).

Create an instance of the Person class and set the following attributes:

    - first_name to the value 'John'
    - last_name to the value 'Dow'

Print the value of the first_name and last_name attribute of this instance to the console.

Expected result:

    John
    Dow
"""


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    first_name = property(get_first_name)
    last_name = property(get_last_name)


person = Person('John', 'Dow')

print(person.first_name)
print(person.last_name)
