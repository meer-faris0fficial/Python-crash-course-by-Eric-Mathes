# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# only if statements can be used
# not equal (!=)
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# numerical value
value = 34 
if value != 12:
    print("the answer is not correct please entre the correct answer")

# To check whether two conditions are both True simultaneously, use the keyword and to combine the #
# two conditional tests
age = 21
age_01 = 12
#If either test fails or if both tests fail, the expression evaluates to False.
print((age == 21) and (age_01 == 45))
# if both are true in above statement then it will print true

#Using or to Check Multiple Conditions
# An or expression fails only when both individual tests fail.
print((age == 21) or (age_01 == 34))
# if both in the above statement are false then it will print false otherwise it will print ture

# Checking Whether a Value Is in a List we use key word "in"
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings

# Checking Whether a Value Is not in a List we use key word "not"
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")





