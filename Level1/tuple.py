#tuple
# Tuples are useful when data should remain unchanged.

country=('Nepal','India','China','USA','UK')
print(country) 

#same as list but  Immutable
country[1]="portugal"
print(country) #throw error

#count
country=('Nepal','India','China','USA','UK')
print(country.count('Nepal'))


#index
country=('Nepal','India','China','USA','UK')
print(country.index('Nepal'))


# This is not a tuple:
x = (10)
print(type(x))

# For a single-element tuple, use a comma:
x = (10,)
print(type(x))
