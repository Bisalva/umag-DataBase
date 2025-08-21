
class BankAccount:
    def __init__(self, owner, account_number, initial_balance=0):
        self.owner = owner
        self.__account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Bank deposit completed: {amount}. Actual balance: {self.balance}.")
        
    def cash_out(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Cash out completed : {amount}. Actual balance: {self.balance}.")
        else:
            print("Not enough funds")
        
    def get_balance(self):
        return self.balance
        
    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Money transfer of {amount} to {target_account.owner} completed. Actual balance : {self.balance}.")
        else:
            print("Not enough funds or an invalid amount")

    def get_account_number(self):
        return self.__account_number

    def __str__(self):
        return f"Account owner : {self.owner} ; Account number : {self.__account_number} ; Balance : {self.balance}"

accountA = BankAccount("Ana García", "123456789", 100000)
accountB = BankAccount("Carlos López", "987654321", 50000)
accountA.transfer(accountB, 25000)

print(accountA)
print(accountB)
