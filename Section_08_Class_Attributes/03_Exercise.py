"""
Exercise No. 03

A class named Phone is defined below. Using dot notation, modify the value of the attributes:

    - brand 'Samsung'
    - model to 'Galaxy'

In response, print the values for the brand and model attributes to the console as shown below.

Expected result:

    brand: Samsung
    model: Galaxy
"""


class Phone:
    brand = 'Apple'
    model = 'iPhone X'


Phone.brand = 'Samsung'
Phone.model = 'Galaxy'

print(f'brand: {Phone.brand}')
print(f'model: {Phone.model}')
