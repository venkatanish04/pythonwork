'''# 1. Program to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")

#2. Program to display the first 7 multiples of 7

m = 7

for i in range(1, 11):
    result = m * i
    print(f"{m} x {i} = {result}")

#3. Program to check if a triangle is a right triangle

def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False
# Input lengths of sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")
'''
#4.Program to construct a pattern using a nested for loop
n=int(input("Enter number of astriks you need:"))
x = int(input("Enter number  you need:"))
x=0
for i in range (n):
        print("*"*x)
        x=x+1

for i in range(n):
            print("*" * x)
            x = x - 1

'''
def binary_divisible_by_five(input_sequence):
    binary_numbers = input_sequence.split(',')
    result_numbers = []

    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        if decimal_number % 5 == 0:
            result_numbers.append(binary_number)

    result_sequence = ','.join(result_numbers)
    return result_sequence

# Accept user input for binary numbers
user_input = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

# Output
result = binary_divisible_by_five(user_input)
print("Input Sequence:", user_input)
print("Numbers Divisible by 5:", result)
'''