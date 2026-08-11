class BankAccount:
    def __init__(self, username, password, pin, balance = 0):
        self.username = username
        self.password = password
        self.pin = pin
        self.balance = balance
        
    def check_password(self, password):
        return self.password == password
        
    def check_balance(self):
       print(f"\nYour current balance is: {self.balance}")
       
    def deposit(self): 
        deposit_amount = int(input("enter the amount to deposit"))
        pin = int(input(f"enter pin to confim deposit of {deposit_amount}: "))
        if self.pin == pin:
            self.balance = self.balance + deposit_amount
            print(f"you desit amount {deposit_amount}, your new balance is {self.balance}")
        else:
            print("deposit went wrong!!!!")
    
    def withdraw(self):
        withdraw_amount = int(input("enter the amount to withdraw: "))
        pin = int(input(f"enter pin to confim withdraw of {withdraw_amount}: "))   
        if self.pin != pin:
            print("Incorrect PIN. Withdrawal failed.")
        elif withdraw_amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - withdraw_amount
            print(f"you withdraw amount {withdraw_amount}, your new balance is {self.balance}")
    
def run_atm(account):
    entered_password = input("Enter your password: ")
    if not account.check_password(entered_password):
        print("Wrong password.")
        return                
                
    while True:
        print("\nWhat do you want to do?")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")            
                
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            account.deposit()
        elif choice == "3":
            account.withdraw()
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    my_account = BankAccount(username="john_doe", password="1234", pin=4321, balance=100)
    run_atm(my_account)