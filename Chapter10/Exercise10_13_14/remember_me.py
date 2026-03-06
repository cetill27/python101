from pathlib import Path
import json


# get input from user 
# store that inside dictionary 
# dump that dictionary as json to a file 

path =  Path('user_info.json')
if path.exists():
    readFile =  path.read_text()
    content  = json.loads(readFile)
    print(content)
else:
    # write to that file 
    username = input("give me your name")
    user_id = input("give me your user_id")
    empl_id = input("give me your empl_id")
    user_info = {
        "username":username,
        "user_id":user_id,
        "empl_id":empl_id
    }
    content = json.dumps(user_info)
    path.write_text(content)
    print(f"I have now remembered your data {user_info['username']}")
