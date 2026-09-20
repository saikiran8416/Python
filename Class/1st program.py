"""Create a class Employee with:

name
age
role

Create two objects and print their details."""

class employee:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role

emp1=employee("sam","36","Manager")
emp2=employee("Rohit","30","Senior Dev")
print(f"Employee 1:\n name: {emp1.name}\n age: {emp1.age}\n role: {emp1.role}\n")
print(f"Employee 2:\n name: {emp2.name}\n age: {emp2.age}\n role: {emp2.role}")

"""output
Employee 1:
 name: sam
 age: 36
 role: Manager

Employee 2:
 name: Rohit
 age: 30
 role: Senior Dev"""