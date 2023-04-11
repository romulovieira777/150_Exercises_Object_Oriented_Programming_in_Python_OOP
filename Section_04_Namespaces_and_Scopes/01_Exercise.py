"""
Exercise No. 01

Import the built-in datetime module and display the namespace of this module (sorted alphabetically) as given below.

Tip:

    Use the __dict__ attribute of the datetime module.

Expected result:

    MAXYEAR
    MINYEAR
    __builtins__
    __cached__
    __doc__
    __file__
    __loader__
    __name__
    __package__
    __spec__
    date
    datetime
    datetime_CAPI
    sys
    time
    timedelta
    timezone
    tzinfo
"""
import datetime

for key in sorted(datetime.__dict__):
    print(key)
