# String Manipulation in Python
# String manipulation means performing different operations on strings, such as creating strings, accessing characters, joining strings, changing case, searching, replacing, splitting, and formatting text.
# In Python, a string is a sequence of characters enclosed inside single quotes (' '), double quotes (" "), or triple quotes (''' ''' / """ """).


name="coder"
print(name)

message='Hello,developer'
print(message)

paragraph="""This is for multiline 
string in python"""
print(paragraph)

#characteristics of string

# 1. String are ordered
# Each character has a position called an index.

text='python'

print(text[1]) #positive index 1 ,output:y
print(text[-1]) #negative index -6 , output:n

# 2. String are immutable 
# Once a string is created, its individual characters cannot be changed.

text='python'

# text[0]='j'  #Error

# Instead, create a new string:

text = "python"
text = "j" + text[1:]
print(text)

# 3. Strings can contain spaces and special characters
a='hello , python!!!'
print(a)

#  Accessing Characters
# You can access individual characters using indexing.
a='python'
print(a[0]) 
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# if use negative indexing
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

#string slicing
#syntax:
# string[start:end]
a='python'
print(a[0:2])
print(a[2:])

#reverse a string 
a='python'
print(a[::-1])

#length
a='python'
print(len(a))

#upper case and lower case
a='PyThon'
print(a.upper())
print(a.lower())

#capitalize
a='Hello python'
print(a.capitalize())

#title
# Converts the first character of each word to uppercase.
a='python is a best programing language'
print(a.title())

# swapcase()
# Changes uppercase characters to lowercase and lowercase characters to uppercase.
a='HelLo pyThOn'
print(a.swapcase())

# strip()
# Removes spaces from both sides.

a='   python is best  '
print(a.strip())

#lstrip
a='   python is best  '
print(a.lstrip())

#rstrip
a='   python is best  '
print(a.rstrip())

#find
# Return the index of first occurrence
a = "Python Programming"
print(a.find("Program"))

# Checking Whether a String Contains Something.
# use in operator
a="python programming"
print("python" in a)
print("javascript" in a)
print("python" not in a)
print("javascript" not in a)


#count
a='rhododendron'
print(a.count('d'))

a='rhododendron is a genus of shrubs and small to (rarely) large trees'
print(a.count('rhododendron'))

#replace
a='I like javascript'
a=a.replace('javascript','python')
print(a)

# You can also specify how many replacements should occur:
a = "apple apple apple"
print(a.replace("apple", "mango", 2))

#splitting a string#max()
a='python'
print(max(a))
a="python is very easy"
b=a.split() #convert to list
print(b)

# You can specify a separator.
a='apple,banana,mango'
b=a.split(",")
print(b)

a=['KTM','is','capital','of','nepal']
b=' '.join(a)
print(b)


#checking the Type of Character
#isalpha()
a='python'
print(a.isalpha())

#isdigit()
a='12345'
print(a.isdigit())

# isalnum()
a='python123'
print(a.isalnum())

#isspace()
a=' '
print(a.isspace())

#islower
a='python'
print(a.islower())

#isupper()
a='PYTHON'
print(a.isupper())

#istitle()
a="Python Is Best Programming Language"
print(a.istitle())





#String concatenation
# Concatenation means joining two or more strings.

a="hello"
b="python"

result=a+" "+b
print(result)



# String repetition
a="hey "
print(a*3)


#comparing string
a='javascript'
b='python'
print(a==b)
print(a!=b)

#string formatting 
#using f-string

name='Ram'
age=20
print(f"My name is {name} and I am {age} years old")

# another example
a = 10
b = 20
print(f"Sum = {a + b}")


#format()
#another way for formating string
name = "Ram"
age = 20
print("My name is {} and I am {} years old.".format(name, age))


#escape characters

#new line \n
print("hello\ncoder")

#tab \t
print("name\tage")

#backslash \\
print("C:\\Users\\Student") #output:C:\Users\Student

#single quote \'
print('It\'s Python') #output:It's Python

#double quote \"
print("he said \"hello\"") #output:he said "hello"

#raw string
path = r"C:\Users\Student\Documents" #Raw strings are especially useful for Windows paths and regular expressions.
print(path)

#Padding and Alignment
# Python provides methods for controlling the width of strings.

#center()
a="python"
print(a.center(20,"*"))


#ljust()
a='python'
print(a.ljust(10, "-"))

#rjust()
a='python'
print(a.rjust(10, "-"))


#removing a specific characters
#strip()
a="###coder###"
print(a.strip("#"))

#similarly from first or last
print(a.lstrip("#"))
print(a.rstrip("#"))

#partitioning a string
#partition()
a="name=ram"
print(a.partition("="))


#some useful Built-in function with string
#len()
a='python'
print(len(a))

#max()
a='python'
print(max(a))

#min()
a='python'
print(min(a))

#sorted
a='python'
print(sorted(a))


