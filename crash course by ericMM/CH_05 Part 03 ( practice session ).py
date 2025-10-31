#  5-3. Alien Colors #1:
alien_color = ['red','green','yellow']
color = 'green'
if color in alien_color:
    print("you have earned the 5 points.")

# 5-4. Alien Colors #2

al_color = 'green'
if al_color == 'green':
    print("the player just earned 5 points for shooting the alien.")
else:
    print("the player just earned 10 points.")

# 5-5. Alien Colors #3: 
alien = 'yellow'
if alien == 'green':
    print("the player earned 5 points.")
elif alien == 'yellow':
    print("the player earned 10 points.")
elif alien == 'red':
    print("the player earned 15 points.")

#  5-6. Stages of Life:
age = int(input("entre your age: "))
if age < 2:
    print(" the person is a baby.")
elif age >= 2 and age < 4 :
    print("the person is a toddeler")
elif age >= 4 and age < 13 :
    print("the person is a kid")
elif age >= 13 and age < 20 :
    print("the person is a teenager")
elif age >= 20 and age < 65 :
    print("the person is a adult")
else:
    print("the person is a elder")



