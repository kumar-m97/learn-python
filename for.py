#Learning for Loop:
#The for statement is used to iterate over the elements of a sequence, 
#that means any kind of iterable object like strings, lists, tuples, dictionaries and so on. 
#It’s used when you have a piece of code which you want to repeat a certain number of times. 

#The general syntax is as followed:
#for (variable name) in (sequesnce):
#    statements

# a program for writing my name kumar 5 times using for loop

print ('Writing my name 5 times')

for i in range(4):
    print ('Kumar') 

#using for loop with disctionary

devops_exp = {"aws":5,"jenkis":4,"docker":6}

#iterating over key
for k in devops_exp:
    print(k)

#iterating over values
for v in devops_exp.values():
    print(v)

#iterating over both key and value:
for k,v in devops_exp.itmes():
    print(k,v)
