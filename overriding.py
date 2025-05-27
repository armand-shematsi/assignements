# method overriding
#MRO is the method resolution order, which is the order 
# I need two real world examples of the above concept

# Example 1: Animal Sound (Method Overriding)
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Example 2: Payment System (Method Overriding and MRO)
class Payment:
    def pay(self):
        print("Processing generic payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Processing credit card payment")

class MobilePayment(Payment):
    def pay(self):
        print("Processing mobile payment")

# MRO Example: Multiple Inheritance
class OnlinePayment(CreditCardPayment, MobilePayment):
    pass

if __name__ == "__main__":
    print("Animal Sound Example:")
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        animal.speak()
    print("\nPayment System Example:")
    payments = [Payment(), CreditCardPayment(), MobilePayment(), OnlinePayment()]
    for payment in payments:
        payment.pay()
    print("\nMRO for OnlinePayment:")
    print(OnlinePayment.__mro__)