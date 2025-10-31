# Nesting
# store multiple dictionaries in a list

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [ alien_0, alien_1 , alien_2 ] 
for alien in aliens:
    print(alien)

# from an empty list
aliens = []
for alien in range(30):
    new_alien = {'color': 'yellow', 'points': 10}
    aliens.append(new_alien)

# modify the first three dictionaries in the above list    
for alien in aliens[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'green'
        alien['points'] = 5
    
for alien in aliens[:5]:
    print(alien)
print(".....")
print(f"total no of aliens are : {len(aliens)}")

# A List in a Dictionary
pizza = {
   'crust': 'thick',
   'toppings': ['mushrooms', 'extra cheese'],
   }

favorite_languages = {
   'jen': ['python', 'ruby'],
   'sarah': ['c'],
   'edward': ['ruby', 'go'],
   'phil': ['python', 'haskell'],
   }
for name, languages in favorite_languages.items():
   print(f"\n{name.title()}'s favorite languages are:")
   for language in languages:
       print(f"\t{language.title()}")

#  A Dictionary in a Dictionary
users = {
   'aeinstein': {
   'first': 'albert',
     'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"username : {username} ")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"
    print(full_name)
    print(location)
    


