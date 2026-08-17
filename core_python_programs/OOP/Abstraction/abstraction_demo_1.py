from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
    def refund(self, amount):
        print(f"Refunded ₹{amount} to Credit Card")    
        

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
    def refund(self, amount):
        print(f"Refunded ₹{amount} using UPI")
        
        
        
card = CreditCardPayment()
upi = UPIPayment()

card.pay(1000)
upi.pay(500)