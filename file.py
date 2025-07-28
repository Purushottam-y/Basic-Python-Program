# Module 5: Files, Exceptions, and Errors in Python
# Task 1: Read a File and handle Errors
#Problem Statement: Write a Python program that:
# 1 Opens and reads a taxt file named sample.txt
file1= open("sample.txt",'r')
reading_file = file1.read()
print(reading_file)
file1.close()

#Prints its content line by line.
file1= open('sample.txt','r')
for line in file1:
    print(line.strip())
file1.close()
# 3. Handles errors gracefully if the file does not exist.
try:
    file1 = open('sample.txt','r')
    for line in file1:
        print(line.strip())
    file1.close()
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
#1. Takes user input and writes it to a file named output.txt.

user_input = input('Enter text to write to the file: ')
file1 = open('output.txt','w')
file1.write(user_input)
print('Data successfully written to output.txt')

#2 Appends additional data to the same file.
user_input = input("Enter additional text to append: Learning file handling in Python.")
file1 = open('output.txt','a')
file1.write(user_input)
print('Data successfully appened.')
#3. Reads and displays the final content of the file.
user_input = input("Enter text to write to the file: ")
file1 = open('output.txt','w')
file1.write(user_input+"\n")
print("Data successfully written to output.txt")
append_input = input("Enter additional text to append: Learning file handling in Python.")
file1 = open('output.txt','a')
file1.write(append_input+"\n")
print("Data successfully append: ")

print("\nfinal content of output.txt")
file1=open('output.txt','r')
content=file1.read()
print(content)
file1.close()
