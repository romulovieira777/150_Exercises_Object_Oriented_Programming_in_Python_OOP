"""
Exercise No. 11

An implementation of the Vector class is given. Implement __mul__() special method that allows you to multiply Vector
instances (by coordinates). For simplicity, assume that the user multiplies vectors of the same length. Then create two
instances of this class:

    - v1 = Vector(4, 2)
    - v2 = Vector(-1, 3)

And perform the multiplication of these vectors. Print the result to the console.

Expected result:

    (-4, 6)
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

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same length.")
        return Vector(*[x * y for x, y in zip(self.components, other.components)])


v1 = Vector(4, 2)
v2 = Vector(-1, 3)

print(v1 * v2)
