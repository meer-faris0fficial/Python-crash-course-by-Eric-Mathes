#  User InpUt and whIle loops

#multiple line prompt
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name}")

# # The Modulo Operator
#  A useful tool for working with numerical information is the modulo operator (%), 
# which divides one number by another number and returns the remainder
print(5 % 3)

# tell the even or odd no using module operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

#  7-2. Restaurant Seating:
dinner_group = input("how many guest will be in the dinner table: ")
group = int(dinner_group)
if group > 8:
    print("you will have to wait for the table kindly wait.")
else:
    print("your table is ready.")




