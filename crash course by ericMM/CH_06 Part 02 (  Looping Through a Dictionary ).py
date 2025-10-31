# To write a for loop for a dictionary, you create names for the two variables that will hold the key
# and value in each keyvalue pair

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nkey : {key}")
    print(f"value : {value}")

# print the keys of the dict
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
for name in favorite_languages.keys():    # .keys() will print the first elements or the keys of dict
    print(name)

# using for loop and if statement
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():    # .keys() will print the first elements or the keys of dict
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name}, I see your favourite language is {language}")

# Looping Through a Dictionary’s Keys in a Particular Order
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
for name in sorted(favorite_languages.keys()):
    print(f"{name}")
        
# Looping Through All Values in a Dictionary        
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
print("following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

#  This approach pulls all the values from the dictionary without checking 
# for repeats. That might work fine with a small number of values, but in a 
# poll with a large number of respondents, this would result in a very repeti
#  tive list. To see each language chosen without repetition, we can use a set. 

# set()is use in this case
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
print("following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

