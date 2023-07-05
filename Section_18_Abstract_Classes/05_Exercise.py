"""
Exercise No. 05

An implementation of the TaxPayer abstract class is given. Create a class derived from the TaxPayer class named
DisabledTaxPayer that implements the calculate_tax() method that calculates the minimum value of the following two:

    - 12% salary tax (salary attribute)
    - 5000.0

Then create an instance of DisabledTaxPayer class named disabled and salary 50.000. In response, by calling
calculate_tax(), print the calculated tax value to the console.

Expected result:

    5000.0
"""
from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class StudentTaxPayer(TaxPayer):
    def calculate_tax(self):
        return self.salary * 0.15


class DisabledTaxPayer(TaxPayer):
    def calculate_tax(self):
        return min(self.salary * 0.12, 5000.0)


disabled = DisabledTaxPayer(50000)
print(disabled.calculate_tax())
