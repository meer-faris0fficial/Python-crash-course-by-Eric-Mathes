# storing the data using the JSON module
# The json module allows you to dump simple Python data structures into a file and load the data from that
# file the next time the program runs. You can also use json to share data between different Python programs.
# Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format
# with people who work in many other programming languages. It’s a useful and portable format, and it’s easy
# to learn.

# Using json.dump() and json.load()
import json

numbers = [2,4,3,6,7,0]
file_name = 'numbers.json'
with open('numbers.json', 'w') as f:
    json.dump(numbers, f) # make a file and print the variable value we want to write in the file 
    
with open('numbers.json') as f:
    numbers = json.load(f)  # read the file content and print it 
print(numbers)

import json

user_name = input("Please entre your name: ")
file_name = 'user_name.json'
with open('user_name.json', 'w') as f:
    json.dump(user_name,f)
    print(f"We will remember you when you come back, {user_name}")

with open('user_name.json') as f:
    user_name = json.load(f)
    print(f"wellcome back, {user_name}")
    
# using try except and else in a statement

def greet_users():
    try:
        with open('user_name.json') as f:
            user_name = json.load(f)
    except FileNotFoundError:
        username = input("What is your name: ")
        with open('user_name.json', 'w') as f:
            json.dump(username, f)
            print(f"We will remember you when you login again, {username}")
    else:
        print(f"wellcome baack,{user_name}")
    
greet_users()
    
