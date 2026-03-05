from random import choice
lottery = ['dasdsad1231','dasd12312','asd12312sdax']
def roll_lottery():
    return choice(lottery)
    
my_ticket= roll_lottery()
print(f"Any ticket matching this :{my_ticket} number wins a prize")
