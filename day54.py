
import re

txt = "Daily Coding Habit"

#Search for an upper case "H" 
#character in the beginning 
#of a word, and print its position:
x = re.search(r"\bH\w+", txt)
print(x.span())
# Output: (13, 18)


#Return a list containing 
#every occurrence of "ai":
x = re.findall("i", txt)
print(x)
# output: ['i', 'i', 'i']

#The string property returns 
#the search string:
x = re.search(r"\bH\w+", txt)
print(x.string)
#output: Daily Coding Habit


#Search for an upper case "H" character 
#in the beginning of a word, 
#and print the word:
x = re.search(r"\bH\w+", txt)
print(x.group())
# output: Habit

