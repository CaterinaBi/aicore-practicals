# Given the following list of number plates: ["G06 WTR", "WL11 WFL", "QW68 PQR"]
number_plates = ["G06 WTR", "WL11 WFL", "QW68 PQR"]
print(number_plates)

# Extract the last two characters of the first word, which represent the year of the car
first_word = number_plates[0]
print(first_word)
last_characters = first_word[1:3]
print(last_characters)

# Print the type of each of them
character_1 = last_characters[0]
character_2 = last_characters[1]
print(type(character_1), type(character_2))

# Convert each of these years to an integer type
int(character_1)
int(character_2)
print(type(character_1), type(character_2))
