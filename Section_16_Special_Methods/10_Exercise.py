"""
Exercise No 10

An implementation of the Vector class is given. Implement __sub__() special method that subtracts Vector instances (by
coordinates). For simplicity, assume that the user subtracts vectors of the same length. Then create two instances of
this class:

    - v1 = Vector(4, 2)
    - v2 = Vector(-1, 3)

And perform the subtraction of these vectors. Print the result to the console.

Expected result:

    (5, -1)
"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

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

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length.")
        return Vector(*[x - y for x, y in zip(self.components, other.components)])


v1 = Vector(4, 2)
v2 = Vector(-1, 3)

print(v1 - v2)
