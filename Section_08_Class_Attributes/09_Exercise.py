"""
Exercise No. 09

A class named OnlineShop was defined with the class attributes set accordingly:

    - sector to the value 'electronics'
    - sector_code to the value 'ELE'
    - is_public_company to the value False

Outside of the class, implement a function called describe_attrs() that display the names of all user-defined class
attributes and their values as shown below. In response, call the describe_attrs() function.

Expected result:

    sector -> electronics
    sector_code -> ELE
    is_public_company -> False
"""


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


def describe_attrs():
    for attr, value in OnlineShop.__dict__.items():
        if not attr.startswith('_'):
            print(f'{attr} -> {value}')


describe_attrs()
