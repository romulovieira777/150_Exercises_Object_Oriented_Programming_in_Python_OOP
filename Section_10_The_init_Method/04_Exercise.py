"""
Exercise No. 04

Implement a class named Vector that takes any number of n-dimensional vector coordinates as arguments when creating an
instance (without any validation) and assign to instance attributes named components. Then create two instances with
following coordinates:

    - (1, 2)
    - (4, 5, 2)

and assign to variables v1 and v2 respectively.

In response, print the values of the components attribute for v1 and v2 instance as shown below.

Expected result:

    v1 -> (1, 2)
    v2 -> (4, 5, 2)
"""


class Vector:
    def __init__(self, *components):
        self.components = components


v1 = Vector(1, 2)
v2 = Vector(4, 5, 2)

print(f'v1 -> {v1.components}')
print(f'v2 -> {v2.components}')
