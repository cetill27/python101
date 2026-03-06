from pathlib import Path 
import json

# numbers  =[2,3,4,11,3]
path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)

contents = path.read_text()
numbers  =json.loads(contents)
print(numbers)

