# Given 2 parameters, height and weight, calculate the parameter BMI (Google the formula).
height = 0
print(height)
weight = 0
print(weight)
BMI = weight / height**2
print(BMI)

# Using the parameter BMI, write a series of if statements that print the following outcomes:
# below 18.5 --> 'Your BMI is x. You're in the underweight range.'
# between 18.5 and 24.9 --> 'Your BMI is x. You're in the healthy weight range.'
# between 25 and 29.9 --> 'Your BMI is x. You're in the overweight range.'
# between 30 and 39.9 --> 'Your BMI is x. You're in the obese range.'
if BMI < 18.5:
    print(f'Your BMI is {BMI}. You\'re in the underweight range.')
elif BMI >= 18.5 and BMI <= 24.9:
    print(f'Your BMI is {BMI}. You\'re in the healthy weight range.')
elif BMI >= 25 and BMI <= 29.9:
    print(f'Your BMI is {BMI}. You\'re in the overweight range.')
elif BMI >= 30 and BMI <= 39.9:
    print(f'Your BMI is {BMI}. You\'re in the obese range.')

# Test your code with the following cases by substituting them in for weight and height values in your code:
# Height: 1.83m, Weight: 85kg # overweight
# Height: 1.55m, Weight: 61kg # overweight
# Height: 2.09m, Weight: 135kg # obese
