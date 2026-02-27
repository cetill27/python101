users = {
    'alley':{
        'first':'alley',
        'last':'codes',
        'location':'delhi',
    },
    'ce27':{
        'first':'ce27',
        'last':'everyday',
        'location':'ghaziabad',
    }
}
for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = f"{user_info['location']}"
    print(f"\tFull Name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")