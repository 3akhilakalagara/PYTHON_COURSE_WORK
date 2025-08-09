from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
    
class Googlepay(Payment):
    def make_payment(self, amount):
        print(f"{amount} credited to your account via Gpay")
        
class Phonepay(Payment):
    def make_payment(self, amount):
        print(f"{amount} debited from your account via phnpay")

def process_payment(payment, amount):
    payment.make_payment(amount)
    

process_payment(Googlepay(), 20000)
process_payment(Phonepay(), 800)