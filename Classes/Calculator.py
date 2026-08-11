class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return f"Addition of {self.a} and {self.b} is ({self.a + self.b})"
    def subtract(self):
        return f"Difference between {self.a} and {self.b} is ({self.a - self.b})"
    def multiply(self):
        return f"Multiplication of {self.a} and {self.b} is ({self.a * self.b})"
    def divide(self):
        return f"Division of {self.a} by {self.b} is ({self.a // self.b})"

cal = Calculator(10,2)
print(cal.add())
print(cal.subtract())
print(cal.multiply())
print(cal.divide())