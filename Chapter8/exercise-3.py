"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time 
"""


def making_sandwitch(name,*ingrediants):
    
    for ingreadiant in ingrediants:
        print(f"Adding {ingreadiant} in the sandwitch")
    print(f"{name}we have prepared sandwitch with {ingrediants} inside")
ingred = ['bread','tikki','cucumber','tomato']
making_sandwitch('alley ',*ingred)
making_sandwitch('alley','tomato')

"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""
def make_car(car_name,car_type,**car_info):
    car_info['car name'] = car_name
    car_info['car type'] = car_type
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

    
