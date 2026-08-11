#Exercise 1: Student
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def __str__(self):
        return self.name
        return self.age
        return self.course
student1 = Student("Alice", 20, "Python") 
student2 = Student("John", 22, "Django")
student3 = Student("Joshua", 30, "Java")

print(student1.name, student1.age, student1.course)
print(student2.name, student2.age, student2.course)
print(student3.name, student3.age, student3.course)

print("\n")

#exercise 2: Car
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def desplay_info(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"year: {self.year}")
car1 = Car("Toyota", "Corolla", 2020)        
print(car1.desplay_info())

print("\n")

#Exercise 3: Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def Area(self):
        return f"Area: {self.width * self.height}"
    def perimeter(self):
        return f"Perimeter: {(self.width + self.height)*2}"
reg1 = Rectangle(10,5)
print(reg1.Area())
print(reg1.perimeter())

print("\n")

#Exercise 4: Bank Account
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        
    def deposit(self): 
        deposit_amount = int(input("enter the amount to deposit"))
        if deposit_amount > 0:
            self.balance = self.balance + deposit_amount
            print(f"you desit amount {deposit_amount}, your new balance is {self.balance}")
        else:
            print("deposit went wrong!!!!")
    
    def withdraw(self):
        withdraw_amount = int(input("enter the amount to withdraw: "))  
        if withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - withdraw_amount
            print(f"you withdraw amount {withdraw_amount}, your new balance is {self.balance}")
    def check_balance(self):
        account_number=int(input("Enter number of account: "))
        owner = input("enter owner of the account: ")
        if account_number == self.account_number and owner == self.owner:
            print(f"\nYour current balance is: {self.balance}")    
        else:
            print("invalid credential!!")

def run_account(account):
    while True:
        print("\nWhat do you want to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")            
                
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            account.deposit()
        elif choice == "2":
            account.withdraw()
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            break
        else:
            print("Invalid choice, try again.")    
        
if __name__ == "__main__":
    my_account = BankAccount(3748292, "irera")
    run_account(my_account)
    
print("\n")

