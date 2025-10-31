# list slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# If fist index is none then, Python automatically starts your slice at the beginning of the list
print(players[:3]) # it will give the same output as above

# Without an ending index, python count the ending of the index at end of the list
print(players[2:])

# slicing with negative no
print(players[-3:])  # it will give the last three element of the list

# Looping Through a Slice
print("here are the first three members of my team: ")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print("my favourite food is: \n", my_foods) 
print("my friend favourite food is: \n", friends_food)   
    



