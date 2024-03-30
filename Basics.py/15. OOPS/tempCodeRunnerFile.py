   elif choice == 4:
        diposit_acc=int(input("Enter account no to deposit: "))
        exists = False
        for obj in accounts:
            if obj.account_number==diposit_acc:
                amt_diposit = float(input("Enter ampunt to be diposited: "))
                obj.balance += amt_diposit
                print(f"Process Successfull/nCurrent Balance={obj.balance}")
            if not exists:
                print("Account no does not exists")