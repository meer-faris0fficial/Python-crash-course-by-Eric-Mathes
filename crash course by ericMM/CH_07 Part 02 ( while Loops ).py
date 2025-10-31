#  Introducing while Loops
current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1

#  Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
messege = ""

while messege != 'quit':
    messege = input(prompt)
    print(messege)

# Using a Flag
# if the flag is set to be false then the while loops will end otherwise it will continue
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    messege = input(prompt)
    if messege == 'quit':
        active = False
    else:
        print(messege)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Using continue in a Loop
#  the continue statement tells Python to ignore the rest of the loop and return to the beginning.

# printing odd no using while loop
numbers = 0
while numbers < 10:
    numbers +=1
    if numbers % 2 == 0:
        continue
    else:
        print(numbers)
