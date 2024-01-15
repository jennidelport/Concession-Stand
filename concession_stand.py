# Creating a Fair Concession Stand

menu = {"pizza slice" : 3.00,
        "jacket potato" : 2.50,
        "scotch egg" : 2.00,
        "nachos" : 3.50,
        "churros" : 2.00,
        "soda pop": 1.60,
        "apple cider" : 2.90,
        "lemonata" : 1.50}
cart = []
total = 0

print("--------- Menu ---------")
for key, value in menu.items():
    print(f"{key:15} : £{value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------- Your Order ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: £{total:.2f}")
#print(cart)