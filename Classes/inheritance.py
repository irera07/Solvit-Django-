class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name}"
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def bark(self):
        return f"barking, {self.age}"

d1 = Dog("BOB", 5)
print(d1.eat())
print(d1.bark())