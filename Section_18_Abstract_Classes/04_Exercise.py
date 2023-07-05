"""
Exercise No. 04

An implementation of the TaxPayer abstract class is given. Create a class derived from TaxPayer named StudentTaxPayer
that implements the calculate_tax() method that calculates the 15% salary tax (salary attribute).

Then create an instance of the StudentTaxPayer class named student and salary 40.000. In response, by calling
calculate_tax() print the calculated tax to the console.

Expected result:

    6000.0
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


student = StudentTaxPayer(40000)
print(student.calculate_tax())
