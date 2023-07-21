"""
Exercise No. 14

Create a class named CustomDict that extends the built-in dict class. Add a method named is_any_str_value() that returns
a boolean value:

    - True in case the created dictionary contains at least one value of str type.
    - otherwise, False.

Example I:

    [IN]: cd = CustomDict(python='mid')
    [IN]: print(cd.is_any_str_value())

returns:

    [OUT]: True

Example II:

    [IN]: cd = CustomDict(price=119.99)
    [IN]: print(cd.is_any_str_value())

returns:

    [OUT]: False

You only need to implement the CustomDict class.
"""
# Example I


class CustomDict(dict):
    def is_any_str_value(self):
        return any(isinstance(value, str) for value in self.values())


cd = CustomDict(python='mid')
print(cd.is_any_str_value())


# Example II
class CustomDict(dict):
    def is_any_str_value(self):
        flag = False
        for key in self:
            if isinstance(self[key], str):
                flag = True
                break
        return flag


cd = CustomDict(price=119.99)
print(cd.is_any_str_value())
