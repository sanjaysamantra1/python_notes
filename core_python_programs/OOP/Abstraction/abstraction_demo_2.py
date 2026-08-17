from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")    

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")        

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification: {message}")   
        


def notify(notification, message):
    notification.send(message)
    
    
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notify(email, "Welcome!")
notify(sms, "Your OTP is 1234")
notify(push, "You have a new message")             