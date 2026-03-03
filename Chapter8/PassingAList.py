# def greet_users(names):
#     """Print a simple greeting to each user in the list"""
#     for name in names:
#         msg = f"Hello,{name.title()}"
#         print(msg)
# username = ['allye','coder','ce27','denta']
# greet_users(username)




#Simulate printing each design , until none are left.
#Move each design to completed_model after printing
def print_model(unprinted_design,completed_models):
   
    while unprinted_design :
        current_design = unprinted_design.pop()
        print(f"Printing {current_design}:")
        completed_models.append(current_design)

def show_completed_model(completed_models):
    """Show all the models that were printed:"""
    print(f"\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)



# Start with some designs  that need to be printed
unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []


#display
print_model(unprinted_designs[:],completed_models)
show_completed_model(completed_models)
print(unprinted_designs)



# [:]use this to send copy of list in the function as an argument


