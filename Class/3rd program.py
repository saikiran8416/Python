"""Create a class Calculator with methods:

add()
subtract()
multiply()
divide()

Create an object and perform all four operations"""

class calculator:

    def __init__(_self,num1,num2):
        _self.num1=num1
        _self.num2=num2

    def add(_self):
        return _self.num1+_self.num2

    def sub(_self):
        return _self.num1-_self.num2
    
    def mul(_self):
        return _self.num1*_self.num2
    
    def div(_self):
        return _self.num1/_self.num2

cal=calculator(25,15)
print(f"addition= {cal.add()}")
print(f"subtraction= {cal.sub()}")
print(f"multiplication= {cal.mul()}")
print(f"division= {cal.div()}")
