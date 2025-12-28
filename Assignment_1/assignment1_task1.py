"""
1.Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
"""
print("Numbers should not be equal to zero")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

division = num1 / num2 
division=round(division,1)

print("Addition:", int(addition), "\nSubstraction:", int(subtraction), "\nMultiplication:",
       int(multiplication), "\nDivision:", division)