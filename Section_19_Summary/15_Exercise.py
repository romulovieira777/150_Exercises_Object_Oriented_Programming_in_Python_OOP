"""
Exercise No. 15

Create a class named StringListOnly that extends the built-in list class. Modify the behavior of the append() method so
that only objects of str type can be added to the list. If you try to add a different type of objects raise TypeError
with message:

    'Only objects of type str can be added to the list.'

Then create an instance of the StringListOnly class and add the following objects with the append() method:

    - 'Data'
    - 'Science'

in response, print result to the console.

Expected result:

    ['Data', 'Science']
"""


class StringListOnly(list):
    def append(self, value):
        if not isinstance(value, str):
            raise TypeError('Only objects of type str can be added to the list.')
        super().append(value)


slo = StringListOnly()
slo.append('Data')
slo.append('Science')

print(slo)
