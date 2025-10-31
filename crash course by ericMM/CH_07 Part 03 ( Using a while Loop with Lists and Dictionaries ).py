# Using a while Loop with Lists and Dictionaries
# To modify a list as you work through it, use a while loop. 

# Moving Items from One List to Another
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"verifying user: {current_users}")
    confirmed_users.append(current_users)
print("\n the following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#  Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#  Filling a Dictionary with User Input
responses = {}
polling_active = True

while polling_active:
    name = input("\nentre your name: ")
    response = input("which mountain would you like to climb someday? ")
    # this will print the input into the dictionary
    responses[name] = response
    
    repeat = input("would you like another person to respond? (yes/no) ? ")
    if repeat == 'no':
        polling_active = False
    elif repeat != 'no' and 'yes':
        print("entre the valid input :")
        repeat = input("would you like another person to respond? (yes/no) ? ")
        
print("\n---poll results---")
for name, response in responses.items():
    print(f"{name}, would like to climb {response}")    
print(responses)