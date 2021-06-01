#THREE PROBLEMS OF TUPLES :
mydict={
            'one' : 100,
            'two' : 200,
            'three' : 300
}
t=1,(1,2,3,5,mydict)
t1=1,(1,2,3,5),mydict

#1. I want to access dictionary from this tuple but only value of "three" named key
print("Accessing required value in tuple t : ",t[1][4]['three'])
print("Accessing required value in tuple t1 : ",t1[-1]['three'])
print("Accessing required value in tuple t (using negative indexing) : ",t[-1][-1]['three'])
print("Accessing required value in tuple (using negative indexing) t1 :",t1[2]['three'])
print()

#2. I want to change value of "one" named key : here assignment is valid since we are making changes in dictionary which are mutable
t[1][4]['one']=1000
print("Updated tuple t : ",t)
print()

#3. I want to change value of second index : Reassigning t2 will help
t1=t1=1,(1,2,3,5),t
print("Changing tuple values of t1 at index 2: ",t1)
print()