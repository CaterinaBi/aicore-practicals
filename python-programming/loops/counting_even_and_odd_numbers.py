# Write a for loop to count the sum of all even numbers between 1 and 100.
sum = 0

for i in range(1,101):
    if i % 2 == 0:
        print(i)
        sum = sum + i
        print("sum =", sum)

# Write another for loop to count the sum of all odd numbers between 1 and 100
sum_2 = 0

for i in range(1,101):
    if i % 2 == 1:
        print(i)
        sum_2 = sum_2 + i
        print("sum =", sum_2)
