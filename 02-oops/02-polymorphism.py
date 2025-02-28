# Polymorphism allows methods to be executed differently based on the object type. It enables functions and methods to operate on different data types dynamically.

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


# Example of polymorphism with the classes defined above
def animal_sound(animal):
    return animal.speak()

# Different objects, same method call
print(animal_sound(dog))  # Output: Buddy says Woof!
print(animal_sound(cat))  # Output: Whiskers says Meow!