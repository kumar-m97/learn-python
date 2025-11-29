#Learning Dictonaries in Python
# Creating a dictionary
# person = { 'name': 'Kumar', 'age': 28, 'height': 170 }

# print("Person's Age is: ", person['age'])

# #getting the values from the dictionary in a list
# values = list(person.values())
# keys = list(person.keys())
# print("Values in the dictionary:", values)
# print("Keys in the dictionary:", keys)
# items = list(person.items())
# print("Items in the dictionary:", items)


# #using for loop to iterate through dictionary
# for key in person.keys():
#     print(key)

# for value in person.values():
#     print(value)

# new_dict = {"cat": 'white', "dog": 'black', "fish": 'gold'}

# if 'gold' in new_dict.values():
#     print("yes")

#############################################################################
#program to count the number of occurrences of each character in a string
# new_string = input("Enter a new word of your choice:\n",)
# new_string = list(new_string)
# for i in range(len(new_string)):
#     print("count of " + new_string[i] + " in " + "".join(new_string) + " is:", new_string.count(new_string[i]))

#############################################################################

n = int(input())
n_list = list(range(n))
for num in range(len(n_list)):
    print(num**2)