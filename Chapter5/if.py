# # cars = ['audi','range_rover','verna','bmw',]
# # for car in cars:
# #     if(car=='bmw'):
# #         print(car.upper())
# #     else:
# #         print(car.title())

# # if(cars[0]!='bmw'):
# #     print("hold the candle noob")
# # else:
# #     print("b booing")


# # print('audi' in cars)

# # user ='gtr'
# # if user not in cars:
# #     print(user.title())

# # age  =3
# # if age<3:
# #     print("first if")
# # elif age<18:
# #     print("second if")
# # else:
# #     print("3rd if")


# requested_toppinng = ['mushrooms','extra cheese','green peppers']
# # if 'mushrooms' in requested_toppinng:
# #     print("Addinng mushrooms.")
# # if 'pepperoni' in requested_toppinng:
# #     print("Addinng pepperoni.")
# # if 'extra cheese' in requested_toppinng:
# #     print("Adding extra cheese")
# # print("\nFinished making your pizza!")


# for requested_topping in requested_toppinng:
#     if requested_topping=='green peppers':
#         print("no pepper u shaker")
#     else:
#         print(f"Adding {requested_topping}")
# print("\nFinished makeing your pizza!!")



# #checking that a list is not empty

# req_topping = []
# if req_topping:
#     for req in req_topping:
#         print(f"Adding{req}")
#     print("\nFinished makeing your pizza!")
# else:
#     print("Are you sure you want a plain pizza")


available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppinngs = ['mushrooms','extra cheese','green peppers']

for req_top in requested_toppinngs:
    if req_top in available_toppings:
        print(f"Adding {req_top}")
    else:
        print(f"Not available")
print("\nFinished making your pizza!")