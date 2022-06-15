# Create a list with two names [name_1, name_2]
spouses_names = ["caterina", "vincent"]

# Find the characters that appear in both names
my_set1 = set(spouses_names[0])
my_set2 = set(spouses_names[1])
print(my_set1, my_set2)

common_letters = my_set1.intersection(my_set2)
print("The shared characters are: ", common_letters)
