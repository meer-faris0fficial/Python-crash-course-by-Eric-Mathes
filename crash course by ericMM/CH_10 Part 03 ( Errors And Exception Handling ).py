# Handling the ZeroDivisionError Exception

"""print(3/0)""" #it will give the zero division error

# Using try-except Blocks
try:
    print(3/0)
except ZeroDivisionError:
    print("You cannot divide it by zero")

print("Give me two numbers, I will divide them for you")
print("Entre 'q' to quit the program")

while True:
    first_number = input("Entre the first number: ")
    if first_number == 'q':
        break
    second_number = input("Entre the second number: ")
    if second_number == 'q':
        break
    try:
        answer = int (first_number) / int (second_number)
    except ZeroDivisionError:
        print("you cannot divide a no with zero!")
    else:
        print(answer)
        

        
    