#immutable lists are called tuples (like constants which does not change)

from hmac import new
from tkinter import Menubutton


dimensions = (100,200)# , are required to define a tuple so incase of single elemeent (3,)

# print(dimensions[0])
# print(dimensions[1])

# dimensions[1] = 1
# print(dimensions)


#LOOP IN TUPLES
for dimension in dimensions:
    print(dimension)


# we cant reassign values to the tuples but we can reassign the varible defining the tuples with new dimensions    

original  = (1,2)
for value in original:
    print(value)

original = (3,4)
for i in original:
    print(i)

buffet = ("tikka", "panner_momom", "roll", "eggs", "allu_tikki")
for menu in buffet:
    print(menu)

buffet = ("tikka", "panner_momom", "roll", "cake", "allu_tikki")
for new_menu in buffet:
    print(new_menu)

print(buffet)