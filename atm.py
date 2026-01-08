class Account:
    def __init__(self,account_no, name, pin, balance = 0):
         self. account_number = account_no
         self.account_holder_name = name
         self.pin = pin   
         self.balance = balance
         self.access=False

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


# acc1=Account(2313,"mrudul",2006,100000)
# acc1.deposit(2000)
# acc1.withdraw(6000)
# acc1.display_balance()

def login(password) :
        if(password==Account.pin):
            Account.access=True
        else :
            Account.access=False
        
def main():
    my_account = Account()
    
        
    print("*******welcome*******")
    userpass = int(input("Write your password"))

    if(login(userpass)):
        print("1. check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.logout")

        user_choice = input("enter your choice")

        if user_choice == "1":
            my_account.display_balance() 
        elif user_choice == "2":
            amount = input(f"enter the deposit amount:{amount}")
        elif user_choice == "3":
                 amount = input(f"enter withdrawal amount:{amount}") 
        elif user_choice == "4":
            print("logging out")
            print("*****thank you*****")
            #break 
            return
        else :
             print("invalid opition")
        
        #return ayega yaha break only use in loops return means use consition se return ya stop kardena he 
    else:
        print("wrong password try again !")

main()