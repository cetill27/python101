# user_0 = {
#     'username':'eferni',
#     'first':'enrico',
#     'last':'fermi'
# }
# for key,value in user_0.items():
#     print(f"\nkey:{key}")
#     print(f"Value:{value}")
    
from sys import set_asyncgen_hooks


favourite_language = {
    'jen':'python',
    'raj':'java',
    'alley':'rust',
    'shori':'c++',
    'shori':'c++',
}

for name,language in favourite_language.items():
    print(f"\n{name.title()} favorite language is {language}")

#keys
for key in favourite_language.keys():
    print(key)

if 'erin' not in favourite_language:
    print("erin , choose your poll boy")

#values
print("The following language have been mentioned :")
for lang in favourite_language.values():
    print(lang.title())

for name in sorted(favourite_language.keys()):
    print(f"\n{name.title()}")

for nam in set(favourite_language.values()):
    print(f"\n{nam.title()}")

