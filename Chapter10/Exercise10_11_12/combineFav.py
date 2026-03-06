from pathlib import Path
import json

def findFav():

    path = Path('favNumbers.json')

    if path.exists():
        readFile = path.read_text()
        context = json.loads(readFile)
        print(f"I know your favorite number is {context}")
    else:
        fav_number = input("Tell me you Favourite Number -")
        content = json.dumps(fav_number)
        path.write_text(content)
        print("I'll remember your favorite number!")
findFav()