# A data type specifies what kind of value a variable stores. Python has several built-in data types.

# 1. Numeric Data Types
# int age=20
# float price=25.5
# complex z=2+3j

# eg

age = 20
price = 25.5
z = 2 + 3j

print(age)
print(price)
print(z)

# 2.String(str)
name="Coder"
print(name);



# 3.Boolean(bool)

is_student= True
print(is_student)

# 4.List(list)

# store changeable values

fruits = ["Apple", "Mango", "Banana"]
print(fruits)
print(fruits[0])
fruits[2]="Oranges"
print(fruits)
print(fruits[2])

# 5. Tuple (tuple)

# Stores multiple values but is unchangeable (immutable).

colors = ("Red", "Green", "Blue")
print(colors)
print(colors[1])
#invalid
# colors[2]="Pink"
# print(colors)
# print(colors[2])


# 6. Set (set)
# Stores unique values and does not maintain duplicate elements.

numbers = {1, 2, 3, 4}
print(numbers)
# print(numbers[1])

# 7. Dictionary (dict)
# Stores data in key-value pairs.

student = {
    "name": "Pyhon Coder",
    "age": 20
}
print(student)
print(student["name"]);

# 8. None (NoneType)
# Represents the absence of a value.
result = None
print(result)