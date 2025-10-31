# Simple if Statements
# The simplest kind of if statement has one test and one action:
#  if conditional_test:  # it is a test 
#  do something   # it is an action 

age = 12
if age >= 18:
   print("You are old enough to vote!")
   print("Have you registered to vote yet?")
else:                         # else donot use any condition
   print("Sorry, you are too young to vote.")
   print("Please register to vote as soon as you turn 18!")

# The if-elif-else Chain
age = 12
if age < 4:
   price = 0
elif age < 18:
   price = 25
else:
   price = 40
print(f"Your admission cost is ${price}.")

# Using Multiple elif Blocks
age = 4
if age < 4:
   price = 0
elif 4 < age < 18:
   price = 25
elif 18 < age < 65:
   price = 40
else:
   price = 20
print(f"Your admission cost is ${price}.")

# using only if statement
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
   print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
   print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
   print("Adding extra cheese.")
print("\nFinished making your pizza!")



