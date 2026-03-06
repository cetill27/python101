from pathlib import Path
import json

fav_number = input("Tell me you Favourite Number -")
path  =Path('favNumber.json')
contents = path.write_text(fav_number)
json.dumps(contents)

