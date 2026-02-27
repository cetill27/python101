pizza  = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

print(f"You ordered a pizza{pizza['crust']}-crust pizza"
    "with the following toppings:"
)
for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
 'jen': ['python', 'rust'],
 'sarah': ['c'],
 'edward': ['rust', 'go'],
 'phil': ['python', 'haskell'],
 }

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages is :")
    for language in languages:
        print(f"\t{language.title()}")
