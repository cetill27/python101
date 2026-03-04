"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information,
 and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""
class Restaurant:
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type =cuisine_type
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and its cuisine type is - {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is now open")
new_rest = Restaurant('molotov-chaska','bihari')
new_rest.describe_restaurant()
new_rest.open_restaurant()