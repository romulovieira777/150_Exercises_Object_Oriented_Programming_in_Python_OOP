"""
Exercise No. 06

An implementation of the TaxPayer abstract class is given. Create a class derived from TaxPayer class named
WorkerTaxPayer that implements the calculate_tax() method that calculates the tax value according to the rule:

    - up to the amount of 80.000 -> 17% tax rate
    - everything above 80.000 -> 32% tax rate

Then create two instances of WorkerTaxPayer named worker1 and worker2 and salaries of 70.000 and 95.000 respectively.

In response, by calling calculate_tax() print the calculated tax for both instances to the console.

Expected result:

    11900.0
    18400.0
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
        return self.salary * 0.12


class WorkerTaxPayer(TaxPayer):
        def calculate_tax(self):
            if self.salary < 80000:
                return self.salary * 0.17
            else:
                return 80000 * 0.17 + (self.salary - 80000) * 0.32


worker1 = WorkerTaxPayer(70000)
worker2 = WorkerTaxPayer(95000)

print(worker1.calculate_tax())
print(worker2.calculate_tax())
