# Write to file
file = open("student.txt", "w")
file.write("Name: Coder\n")
file.write("Age: 20\n")
file.write("Course: BEIT\n")
print("File written successfully")
file.close()

# Read from file
file = open("student.txt", "r")

for line in file:
    print(line, end="")

file.close()  


#even better , in modern python
# Write
with open("student.txt", "w") as file:
    file.write("Name: Coder\n")
    file.write("Age: 20\n")
    file.write("Course: BEIT\n")

print("File written successfully")

# Read
with open("student.txt", "r") as file:
    for line in file:
        print(line, end="")


#read()
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

#readline()
file = open("student.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(line1)
print(line2)
file.close()

# readlines()
# reads all lines and returns them as a list.
file = open("student.txt", "r")
lines = file.readlines()
print(lines)
file.close()

#reading a file using a for loop
file=open("student.txt","r")
for line in file:
    print(line)

file.close()


#writing multiple lines 
#use writelines()

lines=["Javascript\n",
       "Python\n",
       "C++\n"
]

file=open("language.txt","w")
file.writelines(lines)
print("Write multiple lines")
file.close()

#read this records
file=open("language.txt","r")
for lines in file:
    print(lines)

file.close()    


#appending to file
# "a" mode

file=open("student.txt","a")
file.write("Semester: 4th")
print("successfully added data in file")
file.close()

# Creating a new file
#use "x" mode

file=open("newfile.txt","x")
file.write("Hello Python")
file.close()

#closing a file
#why close a file?
#1. Releases system resources
#2. Ensures data is properly written
#3. Prevents unnecessary file locks
#4. Good programming practice


file = open("student.txt", "r")
data = file.read()
print(data)
file.close() #after working with a file


#use with open ->better way
#no need of file close
with open("student.txt", "r") as file:
    data = file.read()

print(data)

#reading and writing together ->use r+ operator
with open("student.txt", "r+") as file:
    data = file.read()
    print(data)

    file.write("New data")


# w+ ->create if file if necessary,delete existing content,allow both reading and writing
with open("student.txt", "w+") as file:
    file.write("Hello Python")
    file.seek(0)
    data = file.read()
    print(data)


#a+ ->allows both appending and reading
with open("student.txt", "a+") as file:
    file.write("\nNew Student")
    file.seek(0)
    data = file.read()
    print(data)


#file pointer
# When Python opens a file, it maintains a file pointer.
with open("student.txt", "r") as file:
    print(file.read(5))
    print(file.read(5))


#tell()
# tell() tells you the current position of the file pointer.
with open("student.txt", "r") as file:
    print(file.tell())
    data = file.read(5)
    print(data)
    print(file.tell())


#seek()
# seek moves the file pointer to a specific position.
with open("student.txt", "r") as file:
    print(file.read(5))
    file.seek(0)
    print(file.read(5)) 

# The second read(5) starts again from the beginning.



#Binary Files
# Binary files store data in binary form.
# e.g:Images,audio,video,pdf files
#use b mode
# rb = read binary
# wb = write binary
# ab = append binary

with open("image.png", "rb") as file:
    data = file.read()


#copying a  Binary File
with open("image.png", "rb") as source:
    data = source.read()

with open("copy.png", "wb") as destination:
    destination.write(data)


#handling file errors
#python provides try-except for handling these errors.
try:
    with open("college.txt", "r") as file:
        data = file.read()
        print(data)

except :
    print("File does not exist.")

