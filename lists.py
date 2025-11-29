# #learning Lists in Python

# # Creating a list
# fruits = ['apple', 'banana', 'cherry', 'avacado']
# print("Fruits List:", fruits)

# # Accessing elements
# print("Frist fruit:", fruits[0])

# # Modifying elements
# fruits[2] = 'orange'

# print("Modified Fruits List:", fruits)

# # Adding elements
# fruits.append('grape')

# print("After appending new fruite:', fruits")

# # Removing elements
# fruits.remove('banana')

# print("After removing banana:", fruits)

# # Iterating through a list
# print("Iterating through the list:")
# for fruit in fruits:
#     print(fruit)


#more operations on lists
#assigning multiple values to a list
# list1 = [1,2,3,4,5]
# one, two, three, four, five = list1
# print("New assigned values:", list1)

# #list slicing
# sliced_list= list1[0:2]
# print("Sliced List:", sliced_list)

# #augmented assignment
# list1 += [2,3,4]
# print("After augmented assignment:", list1)

# #adding to each element in the list
# for i in range(len(list1)):
#     list1[i] += 1
# print("After adding 1 to each element:", list1)


#list methods
# list2 = [5,3,8,6,2]
# list2.sort()
# print("Sorted List2:", list2)
# print(list2.index(8))
# list2.append(4)
# print("After appending 4 and 5:", list2)
# list2.insert(2,7)
# print("After inserting 7 at index 2:", list2)


# #converting a string to a list
# string1 = "hello world"
# list_from_string = list(string1)
# print("List from string:", list_from_string)

# #converting a list to a string
# joined_string = ''.join(list_from_string)

# #strings are immutable while lists are mutable

#slicing a string to create a new string

# og_string = "a big cat"
# changed_string = "the " + og_string[2:9]
# print("Changed String:", changed_string)

# #check if the input is even and in the inclusive range of 2 and 5, print "weired" else print "not weired"
# num = int(input("Enter a number: "))


# #Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# num = int(input("Enter a number: "))

# if num % 2 != 0:
#     print("Weird")
# elif num % 2 == 0 and 2 <= num <= 5:
#     print("Not Weird")
# elif num % 2 == 0 and 6 <= num <= 20:
#     print("Weird")
# elif num % 2 == 0 and num > 20:
#     print("Not Weird")



