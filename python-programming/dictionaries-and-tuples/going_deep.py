# Create a set
my_set = {"caterina", "vincent", "isadora", "leone"}
print(my_set)

# Create a dictionary
my_dictionary = {"caterina":35, "vincent":42, "isadora":5, "leone":1} 
print(my_dictionary)

# Practice accessing keys and values
print(my_dictionary["caterina"])
print(my_dictionary["vincent"])

my_dictionary2 = {"caterina": [35, "italian", "female"], "vincent": {"married": "yes", "belgian": "yes"}, "isadora":5, "leone":1} 
# Access element on principal dictionary
print(my_dictionary2["isadora"])
# Access element within an embedded list
print(my_dictionary2["caterina"][1])
# Access element within embedded dictionary
print(my_dictionary2["vincent"]["married"])

# Use indexing to get the string "Python" from the following dictionary: 
# one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}

one_deep_dictionary = {'start here':1,'k1':[1,2,3,{'k2':[1,2,{'k3':['keep going',{'further':[1,2,3,4,[{'k4':'Python'}]]}]}]}]}
