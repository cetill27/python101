"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.

"""

# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
        
#     def describe_user(self):
#         print(f"the user is {self.first_name}{self.last_name}")
#     def greet_user(self):
#         print(f"Hi {self.first_name} u doing good bud")
# user1 = User('allye','coder')
# user1.describe_user()
# user1.greet_user()



"""
9-5. Login Attempts: Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
class User:
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"the user is {self.first_name} {self.last_name} : no of loggins {self.login_attempts}")
    def greet_user(self):
        print(f"Hi {self.first_name} u doing good bud")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempt(self):
        self.login_attempts = 0
user2 = User('alley','coder','1')
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.describe_user()