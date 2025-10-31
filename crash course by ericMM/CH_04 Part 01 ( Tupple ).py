# TUPPLE:
# An immutable list is called a tuple.  a = (1,) is a tupple as comma defines tupple it is must in tupple

# we can every element in the tupple
elements = (200,5000)
print(elements[0])

# Looping Through All Values in a Tuple using for loop
for element in elements:
    print(element)   # it will print element of the tupple one by one
    
# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
# So if we wanted to change our dimensions, we could redefine the entire tuple
elements = (200,5000)
print("original elements: ")
for element in elements:
    print(element)

elements = (123,400)
print("\nmodified elements: ")
for element in elements:
    print(element)

#  4-13. Buffet
menu = ('italian pizza','ham burgger','biryani','desert','mango juice')
print("Thank you for your visit to our resturent please order your food.")
print("\nour main menu is: ")
for dishes in menu:
    print(dishes.title())    




