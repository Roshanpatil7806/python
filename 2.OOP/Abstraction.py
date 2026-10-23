from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def process_payment(self):
        pass


class CreditCardPayment(Payment):

    def process_payment(self):
        print("Payment processed using Credit Card")


payment = CreditCardPayment()

payment.process_payment()