"""
Exercise No. 01

The stock_info() function is defined. Using the appropriate attribute of the stock_info() function, display the
names of all arguments to this function to the console.

An example of calling the function:

    print(stock_info('Apple', 'USA', 115, '$'))
    company: Apple
    country: USA
    price: $ 115

Tip:
    Use the __code__ attribute of the function.

Expected result:

    {'company', 'country', 'price', 'currency'}
"""


def stock_info(company, country, price, currency):
    return f"Company: {company}\nCountry: {country}\nPrice: {currency} {price}"


print(stock_info.__code__.co_varnames)
