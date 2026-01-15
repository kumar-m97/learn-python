#Learing Exception Handling in Python

#Inside the try block, you write the code that might cause an exception. 
#If an exception occurs, Python jumps to the except block to handle it gracefully, 
#allowing the rest of your program to continue running.

try:
    numerator = 10
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator    
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

#Handling multiple exceptions
try:
    file = open("test.txt")
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")

#Finally block
#Code inside the finally block is executed whether an exception occurs or not.

try:
    file = open("test.txt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    file.close()


#raising exceptions
#By raising exceptions, you can communicate errors or unusual conditions to other parts
# of your program or to the user, helping them understand what went wrong.
x = -5
if x < 0:
    raise ValueError("Negative value error: x must be non-negative")

#Custom Exceptions
#You can define your own exception classes to represent unique error scenarios in your program. 
#This allows you to handle them in a more specialized way.