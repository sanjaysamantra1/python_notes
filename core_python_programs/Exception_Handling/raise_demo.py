balance = 1000

def withdraw(amount):
    global balance

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    if amount > balance:
        raise ValueError("Insufficient balance")

    balance -= amount
    print(f"{amount} Withdrawal successful , Remaining balance: {balance}")

try:
    withdraw(300)
    withdraw(500)
    withdraw(700)
    
except ValueError as e:
    print("Error:", e)