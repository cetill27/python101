# using a function with while loop
# def get_formatted_name(first_name,last_name):
#     """Return a full name """
#     full_name = f"{first_name} {last_name}"
#     return first_name.title()
    
# # this is an infinite loop
# while True:
#     print("\nTell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name =input("First Name:")
#     if f_name =='q':
#         break

#     l_name =input("Last Name:")
#     if l_name =='q':
#         break
#     formatted_name  = get_formatted_name(f_name,l_name)
#     print(f"\nHello , {formatted_name}")


def city_country(city_name,country_name):
    full_name = f"{city_name},{country_name}"
    return full_name.title()

ans = city_country('alaska','india')
print(f"\"{ans}\"")
print(f'"{ans}"')
