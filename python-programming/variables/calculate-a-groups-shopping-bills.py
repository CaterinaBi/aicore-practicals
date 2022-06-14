# Assign variables for each of these items and their prices
# Tomatoes cost 87p for a pack of 6
# 500g sugar costs £1.09
# Washing sponges cost 29p for a pack of 10
# Juice is £1.89 per 1.5l bottle
# Foil is £1.29 per 30m roll
six_pack_tomatoes = 0.87
half_kg_sugar = 1.09
ten_pack_sponges = 0.29
one_and_half_liter_juice_bottle = 1.89
thirty_meter_foil_roll = 1.29

# How much would it cost for 5 people if each person needs:
# A pack of tomatoes
# 3 washing sponges
# A litre of juice
# 20m of foil
# 180g sugar
# Assign the value to total
total = 5 * (six_pack_tomatoes + (ten_pack_sponges / 10) * 3 + (one_and_half_liter_juice_bottle / 3) * 2 + (thirty_meter_foil_roll / 3) * 2 + (half_kg_sugar / 500) * 180)

#Provide your answer as a printed variable called total.
print(total)

# These prices do not include VAT. Calculate the VAT on the total, assuming that VAT is 20%.
vat = total * 1.2
print(vat)

#Then round it appropriately to two decimal places.
print(round(vat, 2))
