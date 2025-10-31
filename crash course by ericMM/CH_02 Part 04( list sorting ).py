#  ORGANIZING LISTS
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.sort()   # this will sort the list alphabatically
print(motorcycles)

# this will sort the list alphabatically reverse order
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.sort(reverse=True)  
print(motorcycles)

# NOTE THAT THE WILL BE PERMANENTALY CHANGED

# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here is the original list: ")
print(cars)
print("\n here is the sorted list: ")
print(sorted(cars))   # sorted(cars) will sort the list temporarily
print("\n here is the final list: ")
print(cars)

# NOTE SORT() PERMANENTALY ARRANGE LIST WHILE SORTED() TEMPORARILY ARRANGE THE LIST

# sorted() function also accept reverse=true
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))

#  Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # it will print the list in reverse order
print(cars)

#  NOTE The reverse() method changes the order of a list permanently, but you can revert to the original
# order anytime by applying reverse() to the same list a second time

#  Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# NOTE the counting of list elements start with 1



