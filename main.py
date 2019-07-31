import datetime

# defining a class
class Employee:

    # class variables
    num_of_employees = 0
    raise_amt = 1.04
    
    # contstructor
    def __init__(self,first: str, last: str, pay: int) -> object:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    # property object (get/set/delete)
    @property
    def email(self) -> str:
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self) -> str:
        return f'{self.first} {self.last}'

    # property object setter
    @fullname.setter
    def fullname(self, name: str) -> None:
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # property object deleter
    @fullname.deleter
    def fullname(self) -> None:
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self) -> float:
        self.pay = int(self.pay * self.raise_amt)

    # method which acts on the class definition and not on the object
    @classmethod
    def set_raise_amt(cls: type, amount: float) -> None:
        cls.raise_amt = amount

    @classmethod
    def from_string(cls: type, emp_str: str) -> object:
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # method which does not act on the object or class but is related ot the class definition in behvaiour
    @staticmethod
    def is_workday(day: str) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True

    # method which is inward (developer) facing for returning a definition of the class
    def __repr__(self) -> str:
        return f'Employee("{self.first}", "{self.last}", {self.pay})'

    # method which is outward (user) facing for returning a string definition of the class
    def __str__(self) -> str:
        return f'{self.fullname()} - {self.email}'

    # dunder method can be called without referenceing the object
    def __add__(self, other: int) -> int:
        return self.pay + other.pay

    def __len__(self) -> int:
        return len(self.fullname())


# sub-class which inherits the functionality of the employee class
class Developer(Employee):

    # different class variable value than the super class
    raise_amt = 1.10

    def __init__(self,first: str, last: str, pay: int, prog_lang: str) -> object:
        # use the super keyword to reference the super class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    # do not pass iterable objects to constructors so default the value to none
    def __init__(self,first: str, last: str, pay: int, employees=None) -> object:
        super().__init__(first, last, pay)
        
        # use if to populate the list
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp) -> None:
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self) -> str:
        for emp in self.employees:
            print(f'--> {emp.fullname()}')


# instatiate an object of class employee
emp_1 = Employee('John', 'Smith', 50000)

# get the employee objects value for email which is generated from first and last names
print(emp_1.email)
