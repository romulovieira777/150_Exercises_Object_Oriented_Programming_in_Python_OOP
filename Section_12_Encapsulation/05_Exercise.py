"""
Exercise No. 05

Implement a class named Person that has one protected instance attribute named first_name. Next, implement a method
get_first_name() which reads the value of the first_name protected attribute. Then, using the get_first_name() method
and the property class (do it in the standard way) create a property named first_name (read-only property).

Create an instance of the Person class and set the first_name attribute to 'John'. Print the value of the first_name
attribute of this instance to the console.

Expected result:

    John
"""


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    first_name = property(get_first_name)


person = Person('John')

print(person.first_name)
