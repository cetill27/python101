# for car in cars:
#     print(f"{car.title()} is running on the track")
#     print(f"{car.upper()} is running on the track\n")
# print("this should be printed for every elemetn in the list")    

# for i in range(len(cars)-1):
#     print(f"{cars[i].title()} is running on the track")
#     print(f"{cars[i+1].title()} is running on the track\n")


#Python work with indentation
# message = "this is a message"
#     print(message)

# using the range() function

# for value in range(1,4):
#     print(value)


numbers = list(range(1,15,2))
# print(numbers)




squares= []
for i in range(1,11):
    squares.append(i**2)
print(squares)    

squares = [value**2 for value in range(1,11)]
print(squares)

