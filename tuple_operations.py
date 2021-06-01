# TUPLE Operations illustration : (only 2 operations are in tuples)

tuple1=(-11,56.8,True,'a','b','c',67,33,1,True,)

#OPERATION 1 -> Using "in" and "not in" keyword : Returns True/False
print("OPERATION 1 : Using 'in' and 'not in' keyword")
#"in" keyword
print("Is 'Kashish' present in tuple? : ",'Kashish' in tuple1)
print("Is 'True' present in tuple? : ",True in tuple1)
#"not in" keyword
print("Is 'Kashish' not present in tuple? : ",'Kashish' not in tuple1)
print("Is 'True' not present in tuple? : ",True not in tuple1)
print()

#OPERATION 2 -> Iterating through a tuple
print("OPERATION 2 : Iterating through a tuple using for loop")
#accessing the elements of tuple by value and not index , using for loop to iterate through tuple
print("Example 1 : ")
for i in tuple1:
    print(i)
print("Example 2 : ")
for i in (7,89,'d'):
    print(i)