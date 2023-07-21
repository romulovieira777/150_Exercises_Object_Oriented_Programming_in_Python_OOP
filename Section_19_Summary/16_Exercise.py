"""
Exercise No. 16

Create a class named StringListOnly that extends the built-in list class. Modify the behavior of the append() method so
that only objects of str type can be added to the list. Replace all uppercase letters with lowercase before adding the
object to the list. If you try to add a different type of objects raise TypeError with message:

    'Only objects of type str can be added to the list.'

Then create an instance of the StringListOnly class and add the following objects with the append() method:

    - 'Data'
    - 'Science'
    - 'Machine Learning'

In response, print result to the console.

Expected result:

    ['data', 'science', 'machine learning']
"""


class StringListOnly(list):
    def append(self, value):
        if not isinstance(value, str):
            raise TypeError('Only objects of type str can be added to the list.')
        super().append(value.lower())


slo = StringListOnly()

slo.append('Data')
slo.append('Science')
slo.append('Machine Learning')

print(slo)
