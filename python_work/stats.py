digits  = [1,2,3,4,5,6,7,8]
print(min(digits))
print(max(digits))
print(sum(digits))


# slicing a list

print(digits[0:3]) 
print(digits[:3]) #till 3
print(digits[3:]) #after 3
print(digits[-3:])  # last 3



#looping through a slice 
players = ["player1","player2","player3","player4","player5","player6"]
print("here is the list of first three players on my team ")
for player in players[:3]:
    print(player.upper())


#copying the entire list

new_list = digits[:] 

print(new_list)

new_list.append("ce27")

print(new_list)

print(digits)

