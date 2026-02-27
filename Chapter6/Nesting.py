# alien_0 = {'color':'green','points':'4'}
# alien_1 = {'color':'yellow','points':'6'}
# alien_2 = {'color':'red','points':'10'}

# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
#     print(alien)

#an empty list for storing alies
aliens = []

#make 30 green aliens

for alien_number in range(30):
    new_alien ={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)


for alien in aliens[:3]:
    if alien['color'] == 'green':
            alien['color']= 'yellow'
            alien['speed'] = 'medium'
            alien['points'] ='10'

#show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created 
print(f"Total number of aliens: {len(aliens)}")

