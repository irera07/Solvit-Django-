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

print("\n")

#Exercise: Employee Inheritance 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display_info(self):
        return f"name: {self.name} \n salary: {self.salary}"
    
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    def display_dev(self):
        return f"{self.display_info()} \n programming language:  {self.programming_language} \n"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def display_man(self):
        return f"{self.display_info()} \n Team_size: {self.team_size}"
        
dev = Developer("Irera", 300000, "Python")
man = Manager("Josue", 500000, 67)
print(dev.display_dev())
print(man.display_man())
            
print("\n")

#Exercise 3:  Encapsulation
class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
        
    def deposit(self, amount):
        self.amount = amount
        if amount > 0 :
            self.__balance = self.__balance + amount
            return f"you deposited {self.amount}, your new balance is {self.__balance}"
        else:
            print("amaount to deposite must greater than 0")
    
    def withdraw(self, amount):
        self.amount = amount
        if self.amount <= 0 :
            print("withdraw amount must greater than 0 please deposite first")
        elif self.amount > self.__balance:
            print("insuficient amount")
        else:
            self.__balance = self.__balance - self.amount
            return f"you have withdrawn {self.amount}, your new balance is {self.__balance}"
    def get_balance(self):
        return f"balance: {self.__balance}"

ba = BankAccount(5000)
print(ba.deposit(1000))
print(ba.withdraw(2000))
print(ba.get_balance())

print("\n")

#Exercise 4:  Inheritance + Encapsulation
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        if self.__name != None:
            return f"my name is {self.__name}"
        else: 
            return "there is no name"
        
    def get_age(self):
        return f"i am {self.__age} years old"
    def set_age(self, age):
        self.age = age
        if self.age < 0:
            return "your age is invalid"
        else:
            return self.age

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

st = Student("irera", 23, 2345, "python")
print(st.get_name())
print(st.get_age())
print(st.set_age(30))

print("\n")

#Exercise 5: Vehicle System
class Vehicle:
    def __init__(self, speed):
        self.__speed = speed
    
    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.speed = speed
        if self.speed < 0:
            return "invalid speed"
        elif self.speed > 300:
            return "overspeed detected"
        else:
            return  self.speed
                
class Car(Vehicle):
    def move(self):
        return f"your car is moving at {self.set_speed()} km/h"

class Motorcycle(Vehicle):
    def move(self):
        return f"your motorcycle is moving at {self.set_speed()} km/h"

c = Car(150)
mo = Motorcycle(90)
print(c.get_speed())
print(c.set_speed(100)) 
print(mo.get_speed())
print(mo.set_speed(80))      