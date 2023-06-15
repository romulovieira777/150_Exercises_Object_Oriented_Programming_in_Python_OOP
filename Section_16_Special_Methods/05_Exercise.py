"""
Exercise No. 05

An implementation of the Vector class is given. Implement __len__() special method to return the number of vector
coordinates.

Example:

    [IN]: v1 = Vector(3, 4, 5)
    [IN]: print(len(v1))

    [OUT]: 3

Create a vector from the R^3 space with coordinates: (-3, 4, 2) and assign it to the variable v1.

In response, print the number of coordinates of this vector using the built-in len() function.

Expected result:

    3
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


v1 = Vector(-3, 4, 2)
print(len(v1))
