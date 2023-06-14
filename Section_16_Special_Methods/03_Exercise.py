"""
Exercise No. 03

Implement a class named Vector which, when creating an instance takes any number of arguments (vector coordinates in
n-dimensional space - without any validation) and assign it to an attribute named components.

Then implement the __repr__() special method to display a formal representation of Vector as show below:

    [IN]: v1 = Vector(1, 2)
    [IN]: print(v1)

    [OUT]: Vector(1, 2)

Create a vector from the R^3 space with coordinates: (-3, 4, 2) and assign it to the variable v1.

In response, print the variable v1 to the console.

Expected result:

    Vector(-3, 4, 2)
"""


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"


v1 = Vector(-3, 4, 2)
print(v1)
