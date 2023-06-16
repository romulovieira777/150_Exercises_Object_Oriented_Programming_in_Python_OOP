"""
Exercise No. 09

An implementation of the Vector class is given. Create the following instances of this class:

    - v1 = Vector(4, 2)
    - v2 = Vector(-1, 3)

Then try to subtract these instances (perform the v1 - v2 operation). If there is an error, print the error message to
the console. Use a try ... except ... clause in your solution.

Expected result:

        unsupported operand type(s) for -: 'Vector' and 'Vector'
"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __add__(self, other):
        components = tuple(
            x + y
            for x, y in zip(self.components, other.components)
        )
        return Vector(*components)


v1 = Vector(4, 2)
v2 = Vector(-1, 3)

try:
    v1 - v2
except TypeError as error:
    print(error)
