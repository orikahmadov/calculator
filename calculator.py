
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
    
    
    def root(self, a, b):
        """ Calculate the bth root of a """
        self.result = a ** (1/b)
        return self.result
    
    def clear(self):
        self.result = 0
        return self.result
    
    
    
    def get_result(self):
        return self.result
