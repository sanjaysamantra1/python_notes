class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}, balance is {balance}")

class InvalidTransactionError(Exception):
    pass

def process_transaction(amount, balance):
    try:
        if amount <= 0:
            raise InvalidTransactionError("Amount must be positive")
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        new_balance = balance - amount
    except InvalidTransactionError as e:
        print(f"Invalid transaction: {e}")
        return balance
    except InsufficientFundsError as e:
        print(f"Insufficient funds: {e}")
        return balance
    except Exception as e:
        print(f"Unexpected error: {e}")
        return balance
    else:
        print("Transaction successful.")
        return new_balance
    finally:
        print("Transaction attempt logged.")
        
        
process_transaction(1000, 2000)