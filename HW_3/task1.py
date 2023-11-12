"""1) Переписатькод в соответствии с Single ResponsibilityPrinciple:
from datetime import date
class Employee:
    def init(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
        return self.base_salary - tax"""

from abc import ABCMeta, abstractmethod


class People:
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def base_salary(self):
        pass


class Employee(People):

    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class SalaryCalculator:
    def calculate_net_salary(self, people: People):
        tax = int(people.base_salary * 0.25)  # рассчитать налог другим способом
        return people.base_salary - tax
