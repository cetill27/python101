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
        self.number_served = 0
    def describe_restaurant(self):
        print(f"The restaurant name is {self.name} and its cuisine type is - {self.cuisine_type}")
    def open_restaurant(self):
        print("Restaurant is now open")
# new_rest = Restaurant('molotov-chaska','bihari')
# new_rest.open_restaurant()
# new_rest.describe_restaurant()



"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0.
 Create an instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again
"""
#9-4 1.1
def set_number_served(self,set_number):
        """Set the numbers served"""
        self.number_served = set_number
        print(f"we served {self.number_served} people today in delhi branch")
def increment_number_served(self,increase_number_served):
        """Increase the number of customer served"""
        self.number_served +=increase_number_served
        print(f"we served {self.number_served} customers including the other branch")
new_Rest = Restaurant('chaska','italian')
new_Rest.describe_restaurant()
new_Rest.open_restaurant()
new_Rest.set_number_served(12)
new_Rest.increment_number_served(2)