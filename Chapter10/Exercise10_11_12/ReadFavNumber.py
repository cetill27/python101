from pathlib import Path
import json

path = Path('favNumber.json')
readFile = path.read_text()
context = json.loads(readFile)
print(f"I know your favorite number is {context}")