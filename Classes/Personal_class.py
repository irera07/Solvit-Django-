class Person:
    def __init__(self, Gender, Dob):
        self.Name = "unknown"
        self.Gender = Gender
        self.Dob = Dob
    #def __str__(self):
        #return self.Name
        #return self.Gender
        #return self.Dob
    def get_name(self):
        return self.Name
    def set_name(self, Name):
        self.Name = Name
    
P1 = Person("male", "2001-3-28")
print(P1.get_name())
P1.set_name("Twizeyeyesu")
print(P1.get_name())
#P2 = Person("Josue", "male", "2003-1-7")
#print(P1.Name, P1.Gender, P1.Dob)
#print(P2.Name, P2.Gender, P2.Dob)