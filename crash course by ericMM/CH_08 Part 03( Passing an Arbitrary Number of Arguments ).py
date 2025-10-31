# NOTE
# " * " → collects extra positional arguments into a tuple.
# " ** " → collects extra keyword arguments into a dictionary

# Passing an Arbitrary Number of Arguments
# , Python allows a function to collect an arbitrary number of arguments from the calling statement. 
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    for topping in toppings:
        print(f"- {topping}")
# every function call make an empty tupple and print arrguments given to the print statement will be place in
# that tupple as example given below
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# these function calls put the values of the arguments in the function which runs through the loop then
# This syntax works no matter how many arguments the function receives. 


# MIXING POSITIONAL AND ARBITARY ARGUMENTS
# in mixing the both arguments we first place the other argument that is not arbitary then place the aarbitary 
# argument and this argument is wr
def make_pizza(size, *toppings): 
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}") 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, middle, **user_info):  # doouble * is use to place arguments in the dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['middle_name'] = middle
    return user_info
user_profile = build_profile('albert', 'einstein','jin',
                             location='princeton',
                             field='physics')
print(user_profile)

