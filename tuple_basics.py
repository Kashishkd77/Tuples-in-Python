# TUPLE Basics : ordered , indexed , immutable and duplicate values allowed
# Tuple can contain other built in types as its element

#CREATION --> with or without parantheses ()
empty_tuple=()
simple_tuple=1,2,3,4,5,6,7,8,9,10
mixed_tuple=(6.7,3,True,'a',"Kashish")
nested_tuple=((4,6,7),['x','y',0],{67,9,0},True,empty_tuple,mixed_tuple,empty_tuple)
print("CREATING NESTED TUPLE : ",nested_tuple)
print()

#PACKING --> tuple creation without using ()
pack_tuple=3,6,mixed_tuple

#UNPACKING --> Extracting values in a single variable
a,b,c=pack_tuple                            #cannot accept integer values in place of a,b,c
print("UNPACKING : ",a,",",c)
print()

#Creating tuple with single element is difficult as it is confused with "string","int",etc
single_tuple=(1)
print("SINGLED ELEMENT TUPLE TYPE : ",type(single_tuple))       #type() : Returns the type of data type

#Adding comma at the end of tuple : Avoids type conflict  in singled element tuple
single_tuple=(1,)
print("SINGLED ELEMENT TUPLE TYPE RESOLVED : ",type(single_tuple))
print()

#ACCESSING ELEMENTS OF TUPLE :
#METHOD 1 :
print("ACCESSING ELEMENTS OF TUPLE : ")
print("First element of nested_tuple : ",nested_tuple[0])
print("Third element of list in nested_tuple : ",nested_tuple[1][2])
#Empty tuple cannot have indexing i.e. nested_tuple[4][0] not possible
print("Fourth element of nested_tuple i.e. Empty tuple : ",nested_tuple[4])
#METHOD 2 : Using Negative Indexing
print("Last second element of nested_tuple : ",nested_tuple[-2])
print()

#SLICING IN TUPLE : Using slicing operator ":" i.e. colon
#simple_tuple=1,2,3,4,5,6,7,8,9,10
#METHOD 1 : start/initial index not included
print("SLICING IN TUPLE : ")
print("Elements at 2 to 5 index : ",simple_tuple[1:5])
print("Start index not given : ",simple_tuple[:6])
print("End index not given : ",simple_tuple[4:])
#METHOD 2 : Using Negative Indexing -> goes from left to right always while accessing elements , final/end index not included
print("Elements between 2-5 index : ",simple_tuple[-5:-1])          #not simple_tuple[-1:-5]
print("Start index not given : ",simple_tuple[:-4])                 #elements from -10 to -3
print("End index not given : ",simple_tuple[-4:])                   #elements from -4 to -1
print()

#CHANGING IN TUPLE : tuples are immutable
print("CHANGING IN TUPLE : ")
#nested_tuple[0]=1 --> creates TypeError : does not support item assignment
#METHOD 1 : Modifying mutable elements of tuple then tuple can be modified
nested_tuple[1][1]="Hello"
print("1 . Modifying mutable part of tuple : ",nested_tuple)
#METHOD 2 : Reassigning using "=" operator
simple_tuple=10,20,30,40,50,60,70,80,90,100
print("2 . Reassigning in tuple : ",simple_tuple)
#METHOD 3 : Concatenation using "=" operator
simple_tuple=10,20,30,40,50,60,70,80,90,100
print("3 . Concatenation of simple_tuple and nested_tuple : ",simple_tuple+nested_tuple)

#METHOD 4 : Repeatition using "*" operator
simple_tuple=10,20,30,40,50,60,70,80,90,100
repeat=("hello", "tuple")*2
print("4.1 . Repeatition in simple_tuple : ",simple_tuple*2)
print("4.2. Repeatition in tuple : ",repeat)
#print(type(repeat))
#print("Repeatition in tuple : ",("hello", "tuple")*2)
print()

#DELETING IN TUPLE :
print("DELETING IN TUPLE :")
#Doesn't support item deletion
simple_tuple=10,20,30,40,50,60,70,80,90,100
#del simple_tuple[2] : gives TypeError
#METHOD 1 : To delete item in tuple -> Delete item from mutable member of list
del nested_tuple[1][2]
print("Deleting element from mutable member of tuple : ",nested_tuple)
#deleting entire tuple
del empty_tuple
#print(empty_tuple) --> gives NameError : empty_tuple not defined