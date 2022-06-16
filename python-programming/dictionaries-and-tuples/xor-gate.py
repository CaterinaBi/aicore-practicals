# Create two variables, A and B, whose values are True and False respectively (just to avoid confusion, you can hard code A = True and B = False)
A = True
B = False

# Using logical operators, calculate:
#The output of an OR logic gate (A or B) and store the value in C
C = A or B
print(C)

# The output of an AND logic gate (A and B) and store the value in D
D = A and B
print(D)

# The output of a NAND (not D) and store the value in D_NOT
D_NOT = not D
print(D_NOT)

# Finally, the output of the XOR gate (C and D_NOT) and store it in XOR
XOR = C and D_NOT
print(XOR)

# Can you do all the steps in one line?
XOR = A or B and not A and B
