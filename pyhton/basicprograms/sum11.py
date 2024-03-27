import re

# Read the file
filename = "numbers.txt"
with open(filename, 'r') as file:
    text = file.read()

# Find all numbers using regular expression
numbers = re.findall(r'\b[0-9]+\b', text)

# Convert the numbers from strings to integers and calculate the sum
total_sum = sum(int(number) for number in numbers)

# Print the sum
print("Sum:", total_sum)
