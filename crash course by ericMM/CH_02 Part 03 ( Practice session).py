# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# 3-4. Guest List:

guest = ['grandpa','grandma','sister']
one = f"Dear {guest[0]}, you are invited on a dinner tonight."
two = f"Dear {guest[1]}, you are invited on a dinner tonight."
three = f"Dear {guest[-1]}, you are invited on a dinner tonight."
print(one)
print(two)
print(three)

#3-5. Changing Guest List

guest = ['grandpa','grandma','sister']
one = f"Dear {guest[0]}, you are invited on a dinner tonight."
two = f"Dear {guest[1]}, you are invited on a dinner tonight."
guest[-1] = 'Brother' 
three = f"Dear {guest[-1]}, you are invited on a dinner tonight."
print(one)
print(two)
print(three)

# 3-6. More Guests:

guest = ['grandpa','grandma','sister']

guest.insert(0,'father') 
guest.insert(2,'mother') 
guest.append('sister') 
print(guest)

print(f"Dear {guest[0]}, you are invited on a dinner tonight.")
print(f"Dear {guest[1]}, you are invited on a dinner tonight.")
print(f"Dear {guest[2]}, you are invited on a dinner tonight.")
print(f"Dear {guest[3]}, you are invited on a dinner tonight.")
print(f"Dear {guest[-1]}, you are invited on a dinner tonight.")
print(guest)
# 3-7. Shrinking Guest List:
 
print("you can only invite two people from the list")

r1 = guest.pop(0)
print(f"Dear {r1}, I am very sorry I cannot invite you for today's dinner")
r2 = guest.pop(1)
print(f"Dear {r2}, I am very sorry I cannot invite you for today's dinner")
r3 = guest.pop(-1)
print(f"Dear {r3}, I am very sorry I cannot invite you for today's dinner")
r4 = guest.pop(-2)
print(f"Dear {r4}, I am very sorry I cannot invite you for today's dinner")

print(guest)


