
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result =  a + b 
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        self.result = a / b
        return self.result
    
    
    def power(self, a, b):
        self.result = a ** b
        return self.result
    
    def get_result(self):
        return self.result
