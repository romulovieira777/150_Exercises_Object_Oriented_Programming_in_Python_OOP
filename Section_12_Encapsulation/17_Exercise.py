"""
Exercise No. 17

Implement a class Game that has a property level (read and modify property, defaults to 0). The value of the level
attribute should be an integer in the range [0, 100]. Add validation at the instance creation and attribute modification
stage. If the value is not of the int type, raise a TypeError with the following message:

    'The value of level must be of type int.'

If the value is outside the range [0, 100], set the exceeded boundary value (0 or 100 respectively). Then create a list
called games consisting of four instances of the Game class:

    games = [Game(), Game(10), Game(-10), Game(120)]

Iterate through the games list and print the value of the level attribute fo each instance.

Expected result:

    0
    10
    0
    100
"""
# Solution I


class Game:
    def __init__(self, level=0):
        self.level = level

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            value = 0
        if value > 100:
            value = 100
        self._level = value


games = [Game(), Game(10), Game(-10), Game(120)]

for game in games:
    print(game.level)


# Solution II
class Game:

    def __init__(self, level=None):
        self.level = level if level else 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of type int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value


games = [Game(), Game(10), Game(-10), Game(120)]

for game in games:
    print(game.level)
