# Using if Statements with Lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding the {requested_topping} on your pizza.")
    else:
        print(f"we donot have {requested_topping}.")
print("\n your pizza is ready.")

#  5-8. Hello Admin:
user_names = ['admin','jaden','helena','caroline','amanita']
for user_name in user_names:
    if 'admin' in user_name:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")

# 5-9. No Users
user_names = []
for user_name in user_names:
    if 'admin' in user_name:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")
else:
    print("We need to find some users!")


#  5-10. Checking Usernames: 
current_users = ['admin','jaden','helena','caroline','amanita']
new_users = ['jorden','helena','caroline','mike','jack']
for new_user in new_users:
    if new_user in current_users:   # comparison of list with a string donot give any output
        print(f"{new_user} this user_name is already taken")
    else:
        print(f"{new_user}, this is available")
    
# 5-11. Ordinal Numbers:
ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for ordinal_no in ordinal_numbers:
    if ordinal_no == 1:
        print(f"{ordinal_no}st")
    elif ordinal_no == 2:
        print(f"{ordinal_no}nd")
    elif ordinal_no == 3:
        print(f"{ordinal_no}rd")
    else:
        print(f"{ordinal_no}th")
    8



