"""
Exercise No. 01

Using the classmethod class (do it in the standard way) implement a class named Person that has a class method named
show_details() which displays the following text to the console:

    "Running from Person class."

Try to pass the class name using the appropriate attribute of the the Person class.

In response, call the show_details() class method.

Expected result:

    Running from Person class.
"""
# Solution I


class Person:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')


Person.show_details()


# Solution II
class Person:

    def show_details(cls):
        print(f'Running from {cls.__name__} class.')

    show_details = classmethod(show_details)


Person.show_details()
