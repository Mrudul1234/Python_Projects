class Account:
    def __init__(self,account_no, name, pin, balance = 0):
         self. account_number = account_no
         self.account_holder_name = name
         self.pin = pin   
         self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("deposit successful")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdrawal successful")
        else:
            print("insufficient fund")
        
    def display_balance(self):
        print(f"current balance:{self.balance}")      


acc1=Account(2313,"mrudul",2006,100000)
acc1.deposit(2000)
acc1.withdraw(6000)
acc1.display_balance()