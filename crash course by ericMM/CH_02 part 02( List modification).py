# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'kawasaki'    # replace element from the list
print(motorcycles)

# add new element at the end of the list

motorcycles.append('BMW')
print(motorcycles)

# Append method

bikes = []
first = input("entre the name of your first bike: ")
second = input("entre the name of your second bike: ")
third = input("entre the name of your third bike: ")

bikes.append(first)
bikes.append(second)
bikes.append(third)

print(bikes)

# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List

motorcycle = ['honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle)

# Removing an Item Using the pop() Method the last element will be poped out

motor = ['honda', 'yamaha', 'suzuki']
motor_pop = motor.pop()
print(motor)
print(motor_pop)

# Popping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)    # pop(0) represent the position of the pop element
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# # Remember that each time you use pop(), the item you work with is nolonger stored in the list.
# If you’re unsure whether to use the del statement or the pop() method,here’s a simple way to decide: when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method


