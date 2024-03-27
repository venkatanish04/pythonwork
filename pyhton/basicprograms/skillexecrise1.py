'''1 st code:
n=int(input("Enter The Number : \t"))
if n==0:
    print("WrongInput")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)


x=0
str1="thisismycountryindia "
for i in str1:
    x=x-1
    print(str1[0:x])
for i in str1:
        x = x + 1
        print(str1[0:x])
       '''
'''
# Program for printing "*" according to the given input
n=int(input("Enter number of astriks you need:"))
x=n
for i in range (n):
        print("*"*x)
        x=x-1
x=1
for i in range (n):
        print("*"*x)
        x=x+1
'''
'''
a1=int(input("Enter The Number in decimal:"))
a2=format(a1,'b')
print(a2)

a1=int(input("Enter The Number decimal:"))
a2=format(a1,'o')
print(a2)

a1=int(input("Enter The Number decimal:"))
a2=format(a1,'d')
print(a2)

a1=int(input("Enter The Number decimal:"))
a2=format(a1,'x')
print(a2)

a1 = input("Enter a binary number: ")
a2 = int(a1, 2)
print("Decimal equivalent:", a2)

a1 = input("Enter a binary number: ")
a2 = int(a1, 8)
print("Octal equivalent:", a2)
a1 = input("Enter a binary number: ")
a2 = int(a1, 16)
print("Hexa equivalent:", a2)
'''

#workbook problems
'''
#1.Program to Calculate an Average in Python
n = int(input("Enter the number of elements: "))
t = 0
for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    t += num
a = t / n
print(f"The average is: {a}")


#2. Program to accept an integer value from a user in Python and to convert an input string value into an integer using an int() function.
user_input = int(input("Enter an integer: "))
print(f"You entered: {user_input}")
str_input = input("Enter a string representing an integer: ")
converted_int = int(str_input)
print(f"Converted integer: {converted_int}")

#3. Program to add two complex, float, and integer numbers
# Adding two complex numbers
complex1 = 2 + 3j
complex2 = 1 + 4j
sum_complex = complex1 + complex2
print(f"Sum of complex numbers: {sum_complex}")
# Adding two float numbers
float1 = float(input("Enter The Number float1:"))
float2 = float(input("Enter The Number float2:"))
sum_float = float1 + float2
print(f"Sum of float numbers: {sum_float}")
# Adding two integer numbers
int1 = int(input("Enter The Number Int1:"))
int2 = int(input("Enter The Number Int2:"))
sum_int = int1 + int2
print(f"Sum of integer numbers: {sum_int}")

#4. Program to convert integer to float
integer = int(input("Enter The Number:"))
float= float(integer)
print(f"Converted float: {float}")
'''
#5. Program to perform addition of string and integer using explicit conversion
string= input("Enter a number as a string: ")
integer = int(string)
result = integer + 10
print(f"The result after adding 10 to the converted integer: {result}")







