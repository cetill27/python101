#creating the dog class
class Dog:
    """A simple attempt to model a dog."""

    # A function that's part of a class is a method 
    #__init__ the two underscores helps python call this method automatically 
    # self method is always required in method definition


    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name}rolled over!.")

my_dog = Dog('my_dog kalia',1)
print(f"My dog name is {my_dog.name},he is {my_dog.age} years old") #this print the object reference 



my_dog.sit()
my_dog.roll_over()