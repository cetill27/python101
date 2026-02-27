#the alien movement
alien = {'x':0,'y':25,'speed':'medium'}

print(f"original postition:{alien['x']}")

#move the alien to the right 
#detrermine how far to move the alienn base on its current spped 
if alien['speed']=='slow':
    x_increment = 1
elif alien['speed']=='medium':
    x_increment=2
else:
    x_increment=3
#the new position is the old posi plus the increment 
alien['x'] = alien['x']+x_increment
print(f"New Position:{alien['x']}")