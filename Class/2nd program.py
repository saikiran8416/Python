"""Create a class Student with a constructor that accepts:

name
marks"""

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def details(self):
        print(f"name:{self.name}, marks: {self.marks}")

student1=student("sachin","450")
student2=student("Rohan","580")
student3=student("Chandra","590")
student1.details()
student2.details()
student3.details()
