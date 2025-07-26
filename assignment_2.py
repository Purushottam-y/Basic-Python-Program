# Task 1: Check if a Number is Even or Odd
a=int(input("Enter the Number"))
if a%2==0:
    print("Even Number is ",a)
else:
    print("Odd Number is ",a)

# Problem Statement: Write a Python program that:
# 1. Takes an integer input from the use.
a=int(input("Enter the integer"))
# 2. Checks whether the number is even or odd using an if-else statement.
if a%2==0:
    print(a,'is an even number')
else:
    print(a,"is an odd number")
# Displays the result according.
a=int(input("Enter the Number"))
if a%2==0:
    print(a,'is an even number')
else :
    print(a,'is an odd number')
# Task 2: Sum of Integers from 1 to 50 Using a Loop
#Problem Statement: Write a Python program that:
# 1. Uses a for loop to iterate over numbers from 1 to 50.
for i in range(1,51):
    print(i)
# 2. Calculates the sum of all integers in this range.
sum=0
for i in range(1,51):
    sum=sum+i
#Display the final sum.
print("The sum of numbers form 1 to 50 is: ",sum)