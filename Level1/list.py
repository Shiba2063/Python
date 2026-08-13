# List is an ordered collection of item

# syntax:
# my_list=[item1,item2,item3]

country=['Nepal','India','China','USA','UK']
print(country)

print(country[0])
print(country[1])
print(country[2])
print(country[3])
print(country[4])


#negative indexing
print(country[-1]) # -1 means the last element

#modify list
country=['Nepal','India','China','USA','UK']
country[2]="pakistan"
print(country)


#append
country=['Nepal','India','China','USA','UK']
country.append('Portugal')
print(country)


#insert
country=['Nepal','India','China','USA','UK']
country.insert(3,'Brazil')
print(country)

#remove
country=['Nepal','India','China','USA','UK']
country.remove('USA')
print(country)

# pop
country=['Nepal','India','China','USA','UK']
country.pop()
print(country)

#sort
country=['Nepal','India','China','USA','UK']
country.sort() #ascending order
print(country)
country.sort(reverse=True) #descending order
print(country)

#reverse
country=['Nepal','India','China','USA','UK']
country.reverse()
print(country)

#length
country=['Nepal','India','China','USA','UK']
print(len(country))

#slice
# Slicing is used to extract a portion of a list.
country=['Nepal','India','China','USA','UK']
a=country[2:4]
print(a)

