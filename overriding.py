# Base class (parent)
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Derived class (child)
class Dog(Animal):
    def speak(self):
        print("The dog barks")

# Another derived class
class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Testing method overriding
a = Animal()
d = Dog()
c = Cat()

a.speak()   # Output: The animal makes a sound
d.speak()   # Output: The dog barks
c.speak()   # Output: The cat meows
