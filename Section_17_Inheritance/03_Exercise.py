"""
Exercise No. 03

The following classes are implemented:

    - Container
    - PlasticContainer
    - MetalContainer
    - SmallPlasticContainer

Print the MRO - Method Resolution Order for SmallPlasticContainer class.

Note: The solution that the user passes is in a file named exercise.py, white the checking code (which is invisible to
the user) is executed from the level where the classes are implemented. Therefore, instead of the name of the module
__main__, the response will be the name of the module in which this class is implemented, in this case exercise.

Expected result:

    [<class 'exercise.SmallPlasticContainer'>, <class 'exercise.PlasticContainer'>, <class 'exercise.Container'>, <class 'object'>]
"""


class Container:
    pass


class PlasticContainer(Container):
    pass


class MetalContainer(Container):
    pass


class SmallPlasticContainer(PlasticContainer):
    pass


print(SmallPlasticContainer.mro())
