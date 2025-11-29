#import re

####################################################################
#search any 10 digit phone number in the given input string
# text = "My phone number is 8109623162"
# pattern = r'\b\d{10}\b'
# phoneNumber = re.findall(pattern, text)
# print("Phone Number found:", phoneNumber)
####################################################################

####################################################################
#search any words starting with 'bat' in the given input string
# input_string = "ratman and ratwoman are characters in a comic book"
# pattern = r'bat\w+'
# matches = re.findall(pattern, input_string)
# print("Matched words:", matches)
####################################################################

####################################################################
# pattern = r'bat(man|woman)'
# matches = re.findall(pattern, input_string)
# print("Matched words:", matches)
####################################################################

####################################################################
#generic regex patterns
# 1. \d - any digit from 0-9
# 2. \D - any non-digit character
# 3. \s - space, tab, newline
# 4. \S - non-space character
# 5. \w - any alphanumeric character
# 6. \W - any non-alphanumeric character
# 7. .  - any character except newline
# 8. ^  - beginning of a string
# 9. $  - end of a string
# 10. *  - zero or more occurrences
# 11. +  - one or more occurrences
# 12. ?  - zero or one occurrence
# 13. {n} - exactly n occurrences
# 14. {n,} - n or more occurrences
# 15. {n,m} - between n and m occurrences
####################################################################

####################################################################
#use of * in regex
# input_string = "bat, batman, batwoman, batmobile, batcave, bat123"
# pattern = r'bat.*'
# matches = re.findall(pattern, input_string)
# print("Matched words using *:", matches)
# ####################################################################

####################################################################
#use of + in regex
# pattern = r'bat.+' 
# matches = re.findall(pattern, input_string)
# print("Matched words using +:", matches)
####################################################################

################################################################
# re.search() - returns first match object
# re.findall() - returns list of all matches
# re.split() - splits the string at each match and returns a list
################################################################



################################################################
#program to find and count the number of vowels and consonants from the given strings

# givenString = input("Write a short sentance to find no of vowels and constants in it\n",)

# consoPattern = r'[^ aeiouAEIOU\s]'
# vowelPattern = r'[aeiouAEIOU]'

# consoMatch = re.findall(consoPattern, givenString)
# vowelMatch = re.findall(vowelPattern, givenString)

# print("Consonants Found", len(consoMatch))
# print("Vowels Found", len(vowelMatch))
