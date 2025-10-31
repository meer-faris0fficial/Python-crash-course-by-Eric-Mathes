#  Python interprets non-empty strings as True
# 2-1. Simple Message: Assign a message to a variable, and then print that message.

message = "Assign a message to a variable, and then print that message."
print(message)

# 2-2. Simple Messages: Assign a message to a variable, and print that message.
# Then change the value of the variable to a new message, and print the new
# message.

message = "hello world"
print(message)

# first letter capital of every word in a sentence

name = "ada lovelace"
print(name.title())

# upper case
name = "ada lovelace"
print(name.upper())

# lower case
name = "ada lovelace"
print(name.lower())

# f_string "f" stands for format in python

f_name = "ada"
l_name = "lovelance"
full_name = f"{f_name} {l_name}"
print(full_name.title())

# add new tab space in a output

title = "\tPython"
print(title)

# add a new line

new_line = "hello, \n \t Iam the king"
print(new_line)

# remove extra spaces at the left end of the string temporarily

remove_space = "Python is good language      "
print(remove_space.rstrip())

# remove extra spaces at the right end of the string temporarily

remove_space = "            Python is good language"
print(remove_space.lstrip())

# remove extra spaces at the both end of the string temporarily

remove_space = "            Python is good language          "
print(remove_space.strip())

# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

name = "Tahir"
messege = f"hello {name},would you like to learn some Python today? "
print(messege)

# 2-5. Famous Quote

quote = '''Albert Einstein once said, “A person who never made a
mistake never tried anything new.”'''
print(quote)

# another method

author = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"
full_one = f'{author} once said, "{quote}"'
print(full_one)

# 2 -6

famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"
messge = f'{famous_person} once said, "{quote}"'
print(messge)


