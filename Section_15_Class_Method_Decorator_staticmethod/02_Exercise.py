"""
Exercise No. 02

Define a Container class that has a static method (use the @staticmethod decorator) named get_current_time() returning
the current time in the format '%H:%M:%S', e.g. '09:45:10'.

Tip:
    Use the built-in time module.
"""
import time


class Container:
    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())


print(Container.get_current_time())
