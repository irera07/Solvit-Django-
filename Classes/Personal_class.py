class Person:
    def __init__(self, gender, dob):
        self.name = "unknown"
        self.gender = gender
        self.dob = dob
    def __str__(self):
        return self.name
        return self.gender
        return self.dob
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
p1 = Person("male", "2001-3-28")
print(p1.get_name())
p1.set_name("Twizeyeyesu")
print(p1.get_name())
p2 = Person("male", "2003-1-7")
print(p1.name, p1.gender, p1.dob)
print(p2.name, p2.gender, p2.dob)