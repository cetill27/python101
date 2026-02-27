# username =['user0','admin','user1','user2','user2','user4','user5']
# if username:
#     for user in username:
#         if user=='admin':
#             print("Hello admin, would you like to see a status report?")
#             break
#         else:
#             print(f"Hello {user.title()},thank you for logging in again")
# print("we need to find some users!")


current_users = ['user1','user2','user3','user4','user5',]
new_users = ['person1','user2','person3','user4','person5']
new_users_UPPER = ['PERSON1','USER2','PERSON3','USER4','PERSON5']

for user in new_users:
    if user in current_users:
        print(f"{user}username already exist")
        if user in new_users_UPPER:
            print("username already exist")
    else:
        print(f"{user}username available")
