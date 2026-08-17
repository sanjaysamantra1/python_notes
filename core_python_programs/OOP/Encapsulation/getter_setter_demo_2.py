class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._account_type = "Savings"  # Protected
        self.__balance = balance        # Private

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    # Getter & Setter via @property decorator
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount

account = BankAccount("Alice", 1000.0)
account.deposit(500)
print(account.balance)       # 1500.0 (Using getter)
account.balance = 2000.0     # Using setter