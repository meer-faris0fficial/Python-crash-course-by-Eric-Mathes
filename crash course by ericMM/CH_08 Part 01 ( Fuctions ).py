# ( * ) the star in the bracket is called an astrisk and is use in various functions

# defining function
def greet_users():
    print("hello")
greet_users()

# giving the argument to the function
def greet_users(username):
    print(f"hello, {username}")
greet_users('jesse')

# Positional Arguments
def pet_name(animal_type , name):
    print(f"the type of the animal is {animal_type}")
    print(f"the name of the animal is {name}")
pet_name('cat','thomas')
# Multiple Function Calls
pet_name('mouse','jerry')
# Order Matters in Positional Arguments
pet_name('harry','lion')
# Keyword Arguments
pet_name(animal_type='mouse',name='jessica') # in this the pattern of the keys donot matter

#  Default Values # NOTE if the parameter is not given then the system uses default parameter that is given in the function

def pet_name(name,animal_type='dog'): # in this the default parameter should follow the undefined parameter
    print(f"the type of the animal is {animal_type}")
    print(f"the name of the animal is {name}")
pet_name('cat','thomas') # in this the type of the animal is cat
pet_name('thomas') # in this the type of the animal uses is the default 'dog'

# Equivalent Function Calls
# key word argument and default values and multiple funtion call and positional arguments can be used together




