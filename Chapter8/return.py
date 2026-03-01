# def get_formatted_name(first_name,last_name):
#     """Return a full name . neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('sunny','dancer')
# print(musician)


#making an argument optional 

# def get_formatted_name(first_name,last_name,middle_name=''):
#     """Return a full name . neatly formatter,"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name
# musician = get_formatted_name('sunny','dancer')
# print(musician)
# musician2 = get_formatted_name('Mr','sunny','dancer')
# print(musician2)


#return a dictionary of information

def build_person(first_name,last_name,age=None):
    """Return a dictionnaryu of information"""
    person ={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician = build_person('sunnny','dancer',28)
print(musician)


