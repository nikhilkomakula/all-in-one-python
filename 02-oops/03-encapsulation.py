# Encapsulation is the practice of bundling data and methods that operate on that data within a single unit or object It can hide private details of a class from other objects.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner      # Public attribute
        self.__balance = balance  # Private attribute (note the double underscore)
    
    # Getter method
    def get_balance(self):
        return self.__balance
    
    # Setter method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

# Creating an account
account = BankAccount("John Doe", 1000)

# Accessing data through methods
print(f"Owner: {account.owner}")
print(f"Balance: {account.get_balance()}")

# Modifying data through methods
account.deposit(500)
print(f"New balance after deposit: {account.get_balance()}")

account.withdraw(200)
print(f"New balance after withdrawal: {account.get_balance()}")

# Direct access to private attribute will fail
# print(account.__balance)  # This would raise an AttributeError