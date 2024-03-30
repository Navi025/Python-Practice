import random
 
 
class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name = ").title()
        self.balance = 0.0
        self.account_type = input("Enter account type = ").title()
 
    def display(self):
        print(f"\nAccount number = {self.account_number}")
        print(f"Account holder = {self.holder}")
        print(f"Account balance = {self.balance}")
        print(f"Account Type = {self.account_type}\n")
 
    def withdraw(self):
        amt = float(input("Enter amount to withdraw = "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance = {self.balance}")
        else:
            print("Insuffciient Balance")
 
    def deposit(self):
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt
 
    def getBalance(self):
        print(f"Your balance = {self.balance}")
 
 
b1 = Bank()
b1.display()
b1.deposit()
b1.display()
b1.withdraw()
b1.display()