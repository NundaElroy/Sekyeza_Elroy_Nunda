
#METHOD OVERRIDING
# Example 1: Online Payment
class Payment:
    def pay(self):
        print("Paying using generic method")

class CreditCardPayment(Payment):
    def pay(self):
        print("Paying using credit card")

# Usage
p = CreditCardPayment()
p.pay()  # Output: Paying using credit card

# Example 2: Payroll system
class Employee:
    def get_salary(self):
        return 3000

class Manager(Employee):
    def get_salary(self):
        return 6000

e = Manager()
print(e.get_salary())  # Output: 6000
