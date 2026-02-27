# number = 1;
# while number<=6:
#     print(number)
#     number +=1



# prompt ="\nTell me something , and i will repeat it back to you"
# prompt+="Enter 'quit' to end the program. "

# message=""
# while message !='quit':
#     message=input(prompt)
#     if message !='quit':
#         print(message)
        

#using a flag
from calendar import c


prompt ="\nTell me something , and i will repeat it back to you"
prompt+="Enter 'quit' to end the program. "

# active  = True
# while active:
#     message = input(prompt)
#     if message=='quit':
#         active = False
#     else:
#         print(message)

#using break 

# while True:
#     message=input(prompt)
#     if message=='quit':
#         break
#     else:
#         print(message)


#using continue
currentNumber  =0
while currentNumber<10:
    currentNumber+=1
    if currentNumber%2==0:
        continue
    print(currentNumber)

#Avoiding Infinite Loops
