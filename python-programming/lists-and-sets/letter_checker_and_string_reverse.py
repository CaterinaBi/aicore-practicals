# Write a program that checks if the two words in the following strings start with the same letter.

phrase1 = 'Clean Couch'
phrase2 = 'Giant Table'

print(phrase1[0] == phrase2[0])

# Write a program that returns the following strings with the words reversed (Not the characters).

my_string1 = 'This is a short phrase'
my_string2 = 'This is actually a significantly longer phrase than the previous one'

split_string1 = my_string1.split()
print(split_string1)
split_string1.reverse()
print(split_string1)

split_string2 = my_string2.split()
print(split_string2)
split_string2.reverse()
print(split_string2)
