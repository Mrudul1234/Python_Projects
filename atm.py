class Account:
    def __init__(self,account_no, name, pin, balance = 0):
         self. account_number = account_no
         self.account_holder_name = name
         self.pin = pin 
         self.balance = balance
         self.access=False

    def login(self,password):
        if password==self.pin :
            self.access=True
        else:
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
         
#error smaj aaraha he tuje ??

acc1=Account(2313,"mrudul",2006,100000)


def main():
    #my_account = Account()
    
        
    print("*******welcome*******")
    userpass = int(input("Write your password :-"))
    
    acc1.login(userpass)

    if(Account.login):
        print("1. check balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.logout")

        user_choice = input("enter your choice :- ")

        if user_choice == "1":
            Account.display_balance() 
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
        
             
    else:
        print("wrong password try again !")

main()