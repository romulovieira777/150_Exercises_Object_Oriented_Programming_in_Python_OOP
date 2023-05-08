"""
Exercise No. 07

Implement a class named Person that has one protected attribute first_name. Next, implement a method get_first_name()
which reads the value of the first_name protected attribute. Declare a method set_first_name() that allows you to modify
the value of the first_name protected attribute (without validation).

Then, using the get_first_name(), set_first_name() methods and the property class (do it in the standard way) create a
property called first_name (property to read and modify).

Create an instance of the Person class and set the first_name attribute to 'John'. Then, using the set_first_name()
method, set new value 'Mike'.

In response, print the value of the first_name attribute to the console.

Expected result:

    Mike
"""


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    first_name = property(fget=get_first_name, fset=set_first_name)


person = Person('John')
person.set_first_name('Mike')

print(person.first_name)
