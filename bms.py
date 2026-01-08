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
    
              