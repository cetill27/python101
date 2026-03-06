from pathlib import Path
import json

def greet_user(filename):

    # path  =Path('username.json')
    path = Path(filename)
    contents = path.read_text()
    username = json.loads(contents)

    print(f"Welcome back, {username}!")