# Task 1: Calculate Factorial Using a Function
# Problem Statement: Write a Python program that:
'''1 Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop
 or recursion.'''
def factorial (n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(factorial(5))
# Using Recursion 
# Calls the function with a sample number and prints the output.
def factorial (n):
    if n < 2:
        return 1
    else:
        return n*(factorial(n-1))
result = factorial(5)
print("Factorial of 5 is", result)'''
# Task 2: Using the Math Module for Calculations

# Problem Statement: Write a Python program tha:
#1 ASks the user for a number that:
#2 Uses math module to calculate the:
# Square root of the number
'''import math
n=int(input("Enter a Squar of the number"))
result=math.sqrt(n)
print("Square root of the number is",result)

# Natural logarithm (log base e) of the number
import math
n=int(input("Enter a Natrual logarithm(log base e) of the number"))
result=math.log(n)
print("Natrual logarithm of number is ",result)'
import math
n=int(input("Enter a Sine of the number (in radians)"))
result=math.sin(math.radians(n))
print("Sine of number is ",result)

