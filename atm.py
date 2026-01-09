class Account:
    def __init__(self,account_no, name, pin, balance = 0):
         self. account_number = account_no
         self.account_holder_name = name
         self.pin = pin 
         self.balance = balance
         self.access=False

    def login(self,password):
        if password==self.pin :
            print("password accepted!\n")
            self.access=True
            return True
        else:
            self.access=False
            return False

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("deposit successful")
        print(f"new balance :{self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdrawal successful")
            print(f"new balance :{self.balance}")
        else:
            print("insufficient fund")
        
    def display_balance(self):
        print(f"current balance:{self.balance}")


accounts=[
    Account(2313,"mrudul",2006,100000),
    Account(2132,"dipanshu",1234,100000)
]


def main():
    my_account = None
    user_pin = int(input("Write your password :-"))                 
    
    for acc in accounts:
        print(f"Checking account {acc.account_holder_name} with PIN {acc.pin}")
        if acc.login(user_pin):
            my_account = acc
            print(f"Login successful: {acc.account_holder_name}")
            break  

    if my_account == None:
        print("wrong password try again!")
    else:
        while True:
            print("*******welcome*******\n")
            print("1.check balance")
            print("2.deposit")
            print("3.withdraw")
            print("4.logout")

            user_choice = input("enter your choice(1-4) :- ")

            if user_choice == "1":
                my_account.display_balance()

            elif user_choice == "2":
                amount = float(input("Enter deposit amount: "))
                my_account.deposit(amount)

            elif user_choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                my_account.withdraw(amount)
                
            elif user_choice == "4":
                print("logging out")
                print("*****thank you*****")
                break
            else:
                print("invalid option")

if __name__ == "__main__":
    main()        
