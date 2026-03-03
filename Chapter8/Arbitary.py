#passing an arbitary number of arguments
# when we dont know how many argyumentrs a function needs to accept 


# def make_pizza(*toppings):
#     print("\nMaking a pizza with the follwing toppings")
#     """ Print the list of toppings that have been requested """
#     for topping in toppings:
#         print(f"-{topping}")
    

# make_pizza('pepperoni')
# make_pizza('rice','sambhar','sauce','palak','pineapple')

#Mixing Positional and Arbitary Arguments
#  for different kind of arguments

# def bake_pizza(size,*toppings):
#     """ pizza we are about to make """
#     print(f"\n Makina a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
# bake_pizza(22,'pepperoni')
# bake_pizza(22,'pepperoni','cheese','nachos')


#Using Arbitary keyword Arguments

def build_profile(first,last,**user_info):
    """Build a dictionary containing everything we kow """
    user_info['first'] = first
    user_info['last']=last
    return user_info
user_profile = build_profile('alley','codes',location = 'india',field='gaming')
#You’ll often see the parameter name **kwargs used to collect nonspecific keyword arguments
