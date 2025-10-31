# storing a function in a module
# Definig a module
# In Python, a module is simply a file that contains Python code — functions, classes, and variables — that 
# you can reuse in other programs.some are built in modules like math

# importing an entire module 
# this will copy the code of that module behind the scene

import CH_08module

CH_08module.make_pizza(16,'pepperoni')
CH_08module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions from a module
# this is the basic formula:      from module_name import function_0, function_1, function_2
# in this case we donot use module name in the function call

from CH_08module import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#  Using as to Give a Function in a module an Alias(nick name) 
# this is usually use when we have some similar names in the same program
from CH_08module import make_pizza as mp  # here mp is an alias usually called nickname
mp(16,'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# as is also use to give an alias to the entire module
import CH_08module as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#  Importing All Functions in a Module
#  You can tell Python to import every function in a module by using the asterisk (*) operator:
# astrisk use below copy all the funtion from the module
from CH_08module import *  # here astrisk(*) represent the function of the module
make_pizza(16, 'pepperoni')   # here we also donot need to call the module only function call is needed
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


