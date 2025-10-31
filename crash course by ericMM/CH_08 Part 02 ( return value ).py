# return values
# A function doesn’t always have to display its output directly. Instead, it can 
# process some data and then return a value or set of values. The value the 
# function returns is called a return value. 

def user_name(f_name,l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()
# in return function we need to provide a variable to the return function so it give the function call to the variable
names = user_name('tahir','hussain')
print(names)

# Making an Argument Optional
def name_format(first_name, last_name, middle_name=''): # middle name is optional and its default value is empty string this is why it is place at the end on the function
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

name = name_format('muhammad', 'tahir', 'hussain') 
print(name)       
name = name_format('tahir','hussain')
print(name)

# RETURNING DICTIONARY
#  A function can return any kind of value you need it to
def build_person(first_name, last_name):
    full_name = {'first' : first_name, 'last' : last_name}
    return full_name
f_name = build_person('tahir','hussain')
print(f_name)

# add element in the dictionary using the retuen function
def add_age(cast,location,age=None):    # "if the caller doesn't provide an age value, default it to None"
    data = {'cast' : cast, 'location' : location}
    if age:
        data['age'] = age
    return data
infoemation = add_age('mughal','sambrial',age=27) # add the age element in the dicitonary
print(infoemation)

# Using a Function with a while Loop
def name_while(fi_name, la_name):
    full_name = f"{fi_name} {la_name}"
    return full_name.title()
while True:
    print(f"\nWhat is your name?")
    print("print 'q' any time to quit? ")
    
    f_name = input("first name: ")
    if f_name == 'q':
        break

    l_name = input("last name: ")
    if l_name == 'q':
        break
    
    formated_name = name_while(f_name,l_name) # this will enter the funtion into the loop
    print(f"hello, {formated_name}.")
    



