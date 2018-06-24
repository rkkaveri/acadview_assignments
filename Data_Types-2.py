#TUPLES
#Q1. Creating tuple and displaying it's length
t=(1,"one",1.456,[2.2,2.3],("hi","hello"))
print("Tuple:",t)
print("Length of Tuple: ",len(t))


#Q2. largest and smallest element of tuple
t=(6,2,9,11,80,23,67,4)
print("Tuple : ",t)
print("Largest element : ",max(t))
print("Smallest element : ",min(t))


#Q3. Product of all tuple elements
t=(6,2,9,11,80,23,67,4)
print("Tuple : ",t)
product=1
for i in t:
  product*=i
print("Product of tuple element: ",product)



#SETS
#Q1. Creating two user define sets and then calculating difference and intersection between the sets
set1=set()
print("Enter 5 set elements of 1st set: ")
for i in range(0,5):
   set1.add(int(input()))
set2=set()
print("Enter 5 set elements of 2nd set: ")
for i in range(0,5):
   set2.add(int(input()))
print("Set 1: ",set1)
print("Set 2: ",set2)
print("Difference between set 1  and set 2: ",set1.difference(set2))
print("Comparision: If set 1 is subset of set 2: ",set1.issubset(set2))
print("Intersection between set 1 and set 2: ",set1.intersection(set2))



#DICTIONARY
#Q1. User input dictionary
d={}
print("Enter 10 dictionary elements: ")
for i in range(1,11):
   k=input("name: ")
   d[k]=int(input("marks: "))
print("Student Dictionary: ",d)
#Q2. Sorting above dictionary according to it's values(marks)
for key in sorted(d, key=lambda x: d[x]):#sorting using lambda
   print("%s : %s"%(key,d[key]))



#Q3. Frequency of each letter in "MISSISSIPPI" and then storing in dictionary
str1="MISSISSIPPI"
print("Word : ",str1)
print("Frequency of each letter in %s is :-"%(str1))
set1=set(str1)
d={}
for i in set1:
   d[i]=str1.count(i) #adding letters as 'key' and it's frequency as 'value' in the dictionary(d)
print(d)

