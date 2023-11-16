"""
CP1404/CP5632 - Practical
Shop calculator
"""

# Get the number of items from the user
items = int(input("Number of items: "))

# Init total price
total_price = 0

# Check that the number of items is more than 0
while items <= 0:
    items = int(input("Number of items: "))

# Get the price of each item and calculate total price
for i in range(items):
    item_price = float(input(f"Enter the price of item {i + 1}: $"))
    total_price += item_price

# Apply discount if total price is over $100
if total_price > 100:
    discount = total_price * 0.10
    total_price -= discount

    # Display total price
print(f"Total price for {items} items is {total_price:.2f}")
