from pathlib import Path
import json


def remember_user(filename):
    username = input("What is your name")
    # path = Path('username.json')
    path = Path(filename)
    contents = json.dumps(username)
    path.write_text(contents)

    print(f"We'll remember you when you come back ")