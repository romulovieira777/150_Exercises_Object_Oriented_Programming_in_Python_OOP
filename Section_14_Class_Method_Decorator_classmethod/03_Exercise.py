"""
Exercise No. 03

The Container class is given. Create an instance of this class named container and call the show_details() method from
this instance.

Expected result:

    Running from Container class.
"""


class Container:
    @classmethod
    def show_details(cls):
        print(f'Running from {cls.__name__} class.')


container = Container()
container.show_details()
