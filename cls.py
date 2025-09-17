class BankAccount:
    def __init__(self):
        self.account_holder="ME"
        self.balance=2000
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("INSUFFICIENT BALANCE")
        else:
            self.balance-=amount
    def get_balance(self):
        return self.balance
account=BankAccount()
account.deposit(1000)
account.withdraw(3000)
print("Final Balance:",account.get_balance())