from pathlib import Path
import json


from greet_user import greet_user
from remember_me import remember_user

filename = input("enter path for filename")
filename = f'{filename}'
path = Path(filename)
if path.exists():
    greet_user(filename)
else:
    remember_user(filename)

