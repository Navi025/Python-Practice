import random
from typing import List


class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name: ").title()
        self.balance = 0.0
        self.account_type = input("Enter account type: ").title()

    def display(self):
        print(f"\nAccount number: {self.account_number}")
        print(f"Account holder: {self.holder}")
        print(f"Account balance: {self.balance}")
        print(f"Account Type: {self.account_type}\n")

    def withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Withdrawal successful\nUpdated balance: {self.balance}")
        else:
            print("Insufficient Balance")

    def deposit(self):
        amt = float(input("Enter amount to deposit: "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt

    def get_balance(self):
        print(f"Your balance: {self.balance}")


accounts: List[Bank] = []

while True:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer")
    print("7. Exit\n")
    choice = int(input("Enter choice: "))

    if choice == 1:
        x = Bank()
        accounts.append(x)
        print("Account added successfully")

    elif choice == 2:
        if accounts:
            for obj in accounts:
                obj.display()
        else:
            print("No accounts to display")

    elif choice == 3:
        search_acc = int(input("Enter account number to search: "))
        exists = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.display()
                exists = True
                break
        if not exists:
            print("Account number does not exist")

    elif choice == 4:
        deposit_acc = int(input("Enter account number to deposit: "))
        exists = False
        for obj in accounts:
            if obj.account_number == deposit_acc:
                exists = True
                obj.deposit()
                break
        if not exists:
            print("Account does not exist")

    elif choice == 5:
        withdrawal_acc = int(input("Enter account number to withdraw: "))
        exists = False
        for obj in accounts:
            if obj.account_number == withdrawal_acc:
                exists = True
                obj.withdraw()
                break
        if not exists:
            print("Account does not exist")

    elif choice == 7:
        break

    else:
        print("Invalid Choice")
