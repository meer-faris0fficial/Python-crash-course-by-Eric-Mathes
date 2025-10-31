#  Using the range() Function
for value in range(1,5):  # it donot print 5
    print(value)

#  Using range() to Make a List of Numbers
numbers = list(range(1,5))  # it will make the list of numbers
print(numbers)

# making even numbers using range()
even_no = list(range(2,11,2))   # the third digit represent output no in range
print(even_no)
odd_no = list(range(1,12,2))
print(odd_no)

# Square of numbers from 1 to 10
squares = []
for values in range(1,11):
    square = values**2
    squares.append(square)
    
print(squares)

# comprehend code of squares
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# more comprehend code of squares
squares = [value**2 for value in range(1,11)]
print(squares)

# minimum and maximum digit of a list
list = [1,2,34,5,6,0]
print(max(list))   # maximum no in the list
print(min(list))   # minimum no the list
print(sum(list))   # add all the values of the list




