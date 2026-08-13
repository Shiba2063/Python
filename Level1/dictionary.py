# A dictionary stores data in key-value pairs
#syntax:
# dictionary = {
#     key1: value1,
#     key2: value2
# }

student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}

print(student)

#Accessing Dictionary Values
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
print(student['name'])


# Modifying Dictionary
# Dictionaries are mutable.
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
student["college"] = "NCIT"
print(student)

# Removing Elements
# 1. pop()
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
student.pop('age')
print(student)

# 2. del
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
del student["faculty"]
print(student)

# 3. clear() -> Removes everything
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
student.clear()
print(student)


#keys -> Returns all keys
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
print(student.keys())

#values ->Returns all values
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
print(student.values())

#items ->Returns key-value pairs
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
print(student.items())

#get -> Safely gets a value
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}
print(student.get("name"))



#Looping Through a Dictionary
student={
    'name':'sanjaya',
    'age':22,
    'faculty':"BECE"
}

#Keys
for key in student:
    print(key)


#Values
for value in student.values():
    print(value)


#both keys and values
for key, value in student.items():
    print(key, value)



#Nested Dictionary
# A dictionary can contain another dictionary.
students = {
    "student1": {
        "name": "Ram",
        "age": 20
    },
    "student2": {
        "name": "Shyam",
        "age": 21
    }
}

print(students["student1"]["name"])
print(students["student2"]["age"])