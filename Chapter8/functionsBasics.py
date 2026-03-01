# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# greet_user()
# print(greet_user.__doc__)   

#passing value to a function
# def greet_user(username): 
#     """Display a simple greeting."""
#     print(f"Hello,{username.title()}")
# greet_user('alley')

#parameter and arguments
# greet_user(username)-> here username is a parameter
# greet_user('alley') -> alley in this is argument passed



# Multiple Functional Calls
# def describe_pet(animal_type,pet_name):
#     """Discplay information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is  {pet_name.title()}")
# describe_pet('hamster','harry')
# describe_pet('dog','cheeku')


#keyword arguments
# def greet_user(username): 
#     """Display a simple greeting."""
#     print(f"Hello,{username.title()}")
# greet_user(username='alley')


#default values

def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}\n")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='cheeku') 
