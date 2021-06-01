# TUPLE Functions illustration : (only 2 functions as they are immutable)

tuple1=(-11,56.8,True,'a','b','c',67,33,1,True,)

#len(object) function --> returns the total count of elements in a list
print("Length of tuple1 is : ",len(tuple1))

#count(value) method --> Returns the count of passed item as an argument
print("Count of 'True' in tuple1 : ",tuple1.count(True))

#index(value) method --> Returns the first index of passed item as an argument
print("Index of 'True' in tuple1 : ",tuple1.index(True))