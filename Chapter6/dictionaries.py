
# alien_0={}
# alien_0 = {'color':'green','points':5}
# # print(alien_0['color'],alien_0['points'])

# alien_0['x_position']=0;
# alien_0['y_position']=5;

# print(alien_0)


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['color']
print(alien_0)

favourite_language = {
    'jem':'python',
    'sarah':'c',
    'james':'rust',
    'raj':'Go'
}

language = favourite_language['sarah'].title()
print(f"Sarah's favourite language is {language}")

alien_1 = {'color':'red','speed':'slow'}
point_value = alien_1.get('points','No point value assigned')#if we dont assign 2nd argumennt python will return None
print(point_value)

