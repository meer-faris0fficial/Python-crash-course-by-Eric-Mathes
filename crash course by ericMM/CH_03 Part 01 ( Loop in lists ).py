#  FOR loop in lists

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(f"{magician.title()}, that was a great trick.")   # .titlt() will capitalized the 1word
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# 4-1. Pizzas

pizzas = ["malai botti","chiken tikka","fagitta"]
for pizza in pizzas:
    print(f"i like to eat {pizza.title()} pizza.")
print("\n But i like all the pizzas!")

#  4-2. Animals:

pets = ["dog","cat","parrot"]
for pet in pets:
    print(f"A {pet.title()} would make a great pet")
print("You can buy any of them as any of these animals would make a great pet!")

