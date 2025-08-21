
class Calculator:
    def __init__(self):
        pass


    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b
    
    def mul(self,a,b):
        return a * b
    
    def div(self,a,b):
        if b == 0:
            return "You can't divide by 0"
        else:
            return a/b
    
    def __str__(self):
        return "Calculator ready to use"        

calc = Calculator()

print(calc.add(5,3))
print(calc.div(10,0))
print(calc)