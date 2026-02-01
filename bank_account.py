class Account:
    def __init__(self,holder_name,balance):
        self.holder_name=holder_name
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"{amount} has been deposit")

        else:
            print('the amount must be greater then 0')

    def withdraw(self,amount):
        if amount<=0:
            print('amount must be greater then 0')
        elif amount>self.balance:
            print("you dont have enough balance")

        else:
            self.balance-=amount
            print(f"{amount} tk has been withdrow")

    def check_balance(self):
        print(f"Your account balace is {self.balance}")


my_account=Account("Abir Ahmmed Chowdhury",50000)
my_account.deposit(2000)
my_account.withdraw(65000)
my_account.check_balance()


