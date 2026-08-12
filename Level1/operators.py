# 1. Arithmetic Operators

a = 10
b = 3

print(a + b)   # 13   Addition
print(a - b)   # 7    Subtraction
print(a * b)   # 30   Multiplication
print(a / b)   # 3.333... Division
print(a // b)  # 3    Floor Division
print(a % b)   # 1    Modulus
print(a ** b)  # 1000 Exponentiation

# 2. Comparison Operators

a = 10
b = 3

print(a == b)  # False  Equal
print(a != b)  # True   Not equal
print(a > b)   # True   Greater than
print(a < b)   # False  Less than
print(a >= b)  # True   Greater than or equal
print(a <= b)  # False  Less than or equal


# 3. Assignment Operators

a = 10

a += 5    # a = a + 5
print(a)  # 15

a -= 3    # a = a - 3
print(a)  # 12

a *= 2    # a = a * 2
print(a)  # 24

a /= 4    # a = a / 4
print(a)  # 6.0

a //= 2   # a = a // 2
print(a)  # 3.0

a %= 2    # a = a % 2
print(a)  # 1.0

a **= 2   # a = a ** 2
print(a)  # 1.0



# 4. Logical Operators

a = 10
b = 5

print(a > 5 and b > 2)   # True
print(a > 15 or b > 2)   # True
print(not(a > 5))        # False

# 5. Bitwise Operators

a = 5
b = 3

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2

# 6. Membership Operators

fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("orange" in fruits)      # False
print("orange" not in fruits)  # True

# 7. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a is not c)  # True