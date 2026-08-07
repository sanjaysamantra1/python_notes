class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


account = BankAccount("Rahul", 10000)

print(account.balance)   # 10000