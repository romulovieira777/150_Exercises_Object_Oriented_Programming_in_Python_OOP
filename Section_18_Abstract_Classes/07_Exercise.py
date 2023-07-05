"""
Exercise No. 07

The following classes are given:

    - StudentTaxPayer
    - DisabledTaxPayer
    - WorkerTaxPayer

Create a list named tax_payers and assign four instance to it, respectively:

    - an instance of the StudentTaxPayer class with a salary of 50.000
    - an instance of the DisabledTaxPayer class with a salary of 70.000
    - an instance of the WorkerTaxPayer class with a salary of 68.000
    - an instance of the WorkerTaxPayer class with a salary of 120.000

Then, iterating through the list, call calculate_tax() method on the given instance and print the tax amount to the
console.

Expected result:

    7500.0
    8400.0
    11560.0
    26400.0
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


tax_payers = [
    StudentTaxPayer(50000),
    DisabledTaxPayer(70000),
    WorkerTaxPayer(68000),
    WorkerTaxPayer(120000)
]

for tax_payer in tax_payers:
    print(tax_payer.calculate_tax())
