# A set is an unordered collection of unique elements.

#syntax:
# my_set = {item1, item2, item3}

numbers = {10, 20, 30, 40}

print(numbers)

# Sets Automatically Remove Duplicates
# This is one of the most useful features of sets.

numbers = {10, 20, 20, 30, 30, 30}

print(numbers)


#adding element
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

#removing element
numbers = {10, 20, 30}
numbers.remove(20)
print(numbers)

# if we used remove() for invalid data then it throws error but so we used discard()

#used remove()
# numbers = {10, 20, 30}
# numbers.remove(40)
# print(numbers)

# used discard()
numbers = {10, 20, 30}
numbers.discard(40)
print(numbers)


#set operations in python

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Union ->combine both sets
print(A | B) #or A.union(B)


#Intersection ->Finds common elements
print(A & B) #or A.intersection(B)

#Difference ->Elements present in A but not in B.
print(A - B)

# Symmetric Difference ->Elements that are in either set, but not in both.
print(A ^ B)


#for create empty set
x = set()

#not use x = {},because this is empty dictionary