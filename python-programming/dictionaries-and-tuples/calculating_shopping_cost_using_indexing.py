# Create a dictionary called shop with the following items and quantities. Where the item is the key and the quantity the value.
# 18 tomatoes
# 2 packs of washing sponges
# 4.5 litres of juice
# 4 rolls of foil
# 2kg sugar

shop = {'tomatoes': 18, 'washing sponges': 2, 'juice': 4.5, 'foil': 4, 'sugar': 2}
print(shop)

# Add another key to the shop dictionary called prices where the value is a dictionary of the following items and prices.
# Tomatoes cost 87p
# Sugar costs £1.09
# Washing sponges cost 29p
# Juice is £1.89
# Foil is £1.29

shop['prices'] = {'tomatoes': 0.87, 'sugar': 1.09, 'washing sponges': 0.29, 'juice': 1.89, 'foil': 1.29}
print(shop)

# Create another key in the shop dictionary called pack_sizes with the value as a dictionary of the following items and their quantities.
# Pack of 6 tomatoes
# 500g sugar of sugar
# Pack of 10 washing sponges
# 1.5l of juice
# 30m roll of foil
# The keys for the dictionaries contained in pack_sizes and prices should all use the name of the item.

shop['pack_sizes'] = {'tomatoes': 6, 'sugar': 0.5, 'washing sponges': 10, 'juice': 1.5, 'foil': 30}
print(shop)

# Find the subtotal (exc. VAT) as a variable called order_subtotal.
# Follow the next steps to do so:
# Check how many packs you will need of each item. You can index the pack_sizes key in the shop dictionary to check the size of the package of each item
print(shop['pack_sizes'])

# Multiply the previous value times the number of packs you are purchasing. Add this value to a new variable.
# For example for tomatoes, you can calculate the number of packs by dividing 18 by shop['pack_sizes']['tomato']
tomato_packs = shop['tomatoes'] / shop['pack_sizes']['tomatoes']
print("You will need", tomato_packs, "tomato packs.")
sugar_packs = shop['sugar'] / shop['pack_sizes']['sugar']
print("You will need", sugar_packs, "sugar packs.")
washing_sponges_packs = shop['washing sponges'] / shop['pack_sizes']['washing sponges']
print("You will need", washing_sponges_packs, "washing sponges packs.")
juice_packs = shop['juice'] / shop['pack_sizes']['juice']
print("You will need", juice_packs, "juice boxes.")
foil_packs = shop['foil'] / shop['pack_sizes']['foil']
print("You will need", foil_packs, "foil rolls.")

# Then you can multiply the result (3 in this case) times the price, so it will be 3 * 0.87
# And store that value in tomatoes_total_price (once you get more confidence coding, you will see that this variable is not necessary)
# Finally, do the same for all items and add them up
tomatoes_total_price = tomato_packs * shop['prices']['tomatoes']
sugar_total_price = sugar_packs * shop['prices']['sugar']
washing_sponges_total_price = washing_sponges_packs * shop['prices']['washing sponges']
juice_total_price = juice_packs * shop['prices']['juice']
foil_total_price = foil_packs * shop['prices']['foil']
total_price = tomatoes_total_price + sugar_total_price + washing_sponges_total_price + juice_total_price + foil_total_price
print("The total price is:", total_price)

# Find the total (inc. VAT) as a variable called order_total (VAT is 20%), remember to round to two decimal points.
