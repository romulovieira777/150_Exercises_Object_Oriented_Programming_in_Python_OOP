"""
Exercise No. 03

Create an abstract class named TaxPayer. In the __init__() method set an instance attribute (without validation) called
salary. Then add an abstract method called calculate_tax() (use the @abstractmethod decorator).
"""
from abc import ABC, abstractmethod


class TaxPayer(ABC):
    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass
