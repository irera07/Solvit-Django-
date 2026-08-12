#Exercise 1: Basic Inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Name: ", self.name)  
        print("Age: ", self.age)
class Student(Person):
    def __init__(self,name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def study(self):
        return "I am studying python"

std1 = Student("John", 21, "ST001")
print(std1.introduce())
print(std1.study())
        