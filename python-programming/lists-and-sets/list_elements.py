# Create a list of five elements with a different data type. Name it list_1
list_1 = [7, 9, 22, 46, 10]
print("List 1: ", list_1)

# Now create a list with ten zeros, do it using the '*' operator. Name it list_2
list_2 = [0] * 10
print("List 2: ", list_2)

# Nest list_1 and list_2 into a new list and name it list_3. So list_3 should look like this [list_1, list2]
list_3 = []
list_3.append(list_1)
list_3.append(list_2)
print("List 3: ", list_3)

# Access the fourth element of each list_1 and list_2
# store the elements in list_4. 
# list_4 should look like this [fourth element of list_1, fourth element of list_2]
list_4 = [list_1[3], list_2[3]]
print("List 4: ", list_4)
