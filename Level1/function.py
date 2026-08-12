# simple function 

def greet():
    print("Hello, Developer!")

greet()


# With parameters

def greet(name):
    print("Hello",name)

greet("Coder")  #code is a argument


# Multiple parameter

def sum(a,b):
    print("Sum :",a+b)

sum(2,3) #passing multiple argument



# Types of argument

# 1. Positional argument

def student(name,age):
    print("Name:",name)
    print("Age:",age)

student("Coder",20)  #give right order output
student(20,"Coder") #give wrong order output  


# 2. keyword Argument


def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Coder")


# 3. Default argument
def greet(name="Coder"):
    print("Hi ",name)

greet()    



def student(name, country="Nepal"):
    print(name, "is from", country)

student("Ram")
student("Shyam", "India")


# *args  -Multiple Positional Arguments

def add(*numbers):
    print(numbers)

add(12,87,23,32,90)   


# **kwargs -Multiple keyword argument

def student(**details):
    print(details)

student(name="Coder",age=20,gender="Male",country="Nepal")    



# return statement


def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# return multiple values

def calculate(a, b):
    return a + b, a - b, a * b

result = calculate(10, 5)

print(result)



# //locol variable

def check():
    num=10
    print(num)

check()


# but 

# def check():
#     num=10

# check()
# print(num)



# Global Variable

num=10
def check():
    print(num)
check()


# if need change a global variable ,we simply used global

x = 10

def change():
    global x
    x = 20

change()

print(x)



# //function calling  another function


def add(a, b):
    return a + b

def square(number):
    return number * number

result = square(add(2, 3))

print(result)



def factorial(n):
    if n<0:
        return "Negetive Number"
    elif n==0 or n==1:
        return 1
    
    else:
        return n*factorial(n-1)


print("Factorial:",factorial(5))


# Lambda function

square = lambda x: x * x

print(square(5))

#types hints

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))


# Docstrings

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add.__doc__)
