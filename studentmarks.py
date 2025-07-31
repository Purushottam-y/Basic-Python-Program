# Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that:
# 1. Creates a dictionary where student names are keys and their marks are values.
dict={'Ram':80,'Shyam Yadav':64,'Ajay Kumar Shing':45}
print(dict)

#2 Asks the user to input a student's nameL
name = input("Enter the student's name: " )
print(f"{name}'s marks: {85}")
#3. Retrieves and displays the corresponding marks.
dicr = {'Alice ': 80, 'bob':92}
name = input("Enter the student's name: ")
if name in dicr:
    print(f"{name}'s marks: {dicr[name]}")
else:
    print("Student not found")
#4. If the student's name is not found, display an appropriate message.
dicr = {'Alice ': 80, 'bob':92}
name = input("Enter the student's name: ")
if name in dicr:
    print(f"{name}'s marks: {dicr[name]}")
else:
    print("Student not found")

# Task 2: Demonstrate List Slicing
# Problem Statement: Write a Python program that:
# 1. Creates a list of numbers from 1 to 10.
lis1 = [1,2,3,4,5,6,7,8,9,10]
print("Original list:",lis1)

# 2. Extracts the first five elements form the list.
lis1 = [1,2,3,4,5,6,7,8,9,10]
first_five = lis1[:5]
print("Extracted first five elements:",first_five)

# 3. Reverses these extracted elements.
lis1 = [1,2,3,4,5,6,7,8,9,10]
l= lis1[:5]
l.reverse()
print("Reversed extracted elemnents:",l)

# 4. Prints both the extracted list and the reversed list
list1=[1,2,3,4,5,6,7,8,9,10]
print("Original list: ",list1)
list2 = list1[:5]
print("Extracted first five elements: ",list2)
list3=list2[:5]
print("Reversed extracted elements: ",list3)


