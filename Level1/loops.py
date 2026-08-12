# 1. for loop


for i in range(5):
    print(i)


for i in range(1, 6):
    print(i)    

# 2. while loop

i = 1

while i <= 5:
    print(i)
    i = i + 1



# Others

# 3. break

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# 4. continue

for i in range(1, 6):
    if i == 3:
        continue
    print(i)