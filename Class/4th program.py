"""Create:

class Employee:
    company = "ABC"

Each employee should have their own:

name
salary

Print both the employee-specific values and the common company value."""

class Employee:
    def __init__(self,company,name, salary):
        self.company=company
        self.name=name
        self.salary=salary

emp=Employee("ABC","Shan",30000)
print(f"Company= {emp.company}")
print(f"name= {emp.name}")
print(f"salary= {emp.salary}")
