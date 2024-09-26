# Base class
class Animal:
    # Method to be overridden by derived classes
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived class representing a Dog
class Dog(Animal):
    # Implementing the speak method for Dog
    def speak(self):
        return "Woof!"

# Derived class representing a Cat
class Cat(Animal):
    # Implementing the speak method for Cat
    def speak(self):
        return "Meow!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    # Call the speak method of the passed animal object
    print(animal.speak())

# Creating instances of Dog and Cat
dog = Dog()  # Create a Dog object
cat = Cat()  # Create a Cat object

# Using the polymorphic function to display sounds
animal_sound(dog)  # Outputs: Woof!
animal_sound(cat)  # Outputs: Meow!
