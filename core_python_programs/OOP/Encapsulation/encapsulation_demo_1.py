class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount

    def get_balance(self):
        return self.__balance