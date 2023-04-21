"""
Exercise No. 07

A class named OnlineShop was defined with the class attributes set accordingly:

    - sector to the value 'electronics'
    - sector_code to the value 'ELE'
    - is_public_company to the value False

Using the built-in delattr() function remove the class attribute sector_code. In response, print the rest of the
user-defined OnlineShop class attributes names as list as shown below.
"""


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


delattr(OnlineShop, 'sector_code')

attrs = [
    attr
    for attr in OnlineShop.__dict__.keys()
    if not attr.startswith('_')
]

print(attrs)
