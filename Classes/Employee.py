#Exercise 5: Employee Salary
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def increase_salary(self):
        percentage = 10/100
        return f"Salary: {self.salary * percentage + self.salary}"
    
    def display_info(self):
    
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print("\n")        
        print("After 10% increase")
        print(self.increase_salary())
        
emp1 = Employee("Alice", "Developer", 500000)
print(emp1.display_info())