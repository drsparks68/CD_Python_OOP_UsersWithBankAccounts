class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging $5 fee")
            return self
        self.balance -= amount
        return self
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance =  self.balance + interest
        return self


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
    def display_balance(self):
        print(f"You have {self.account.balance} in your account.")