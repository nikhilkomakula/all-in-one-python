# Inheritance allows a class to inherit attributes and methods from another class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass  # Base method to be overridden

# Child classes inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
        
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!