#Q1. User input for 10 numbers
l=[]
print("Enter the 10 numbers")
for i in range(1,11):
   l.append(int(input()))
print("The 10 numbers are : ")
for i in l:
  print(i)


#Q2. Infinite loop
i=2
while(i>1):
  print("hello")


#Q3. List of user input integers and new list with square elements
l=[]
print("Enter the 10 numbers")
for i in range(1,11):
   l.append(int(input()))
print("The user input list : ",l)
newl=[]
for i in l:
   newl.append(i*i)
print("The list with square of elements : ",newl)


#Q4. Forming list seperate list of integers,float and string
l=[1,2.9,"hey",6,"hello",5.3]
print("The user input list : ",l)
i=[] 
f=[]
s=[]
for x in range(0,6):
   if(type(l[x])==int): i.append(l[x])
   if(type(l[x])==float): f.append(l[x])
   if(type(l[x])==str): s.append(l[x])
print("List of integers: ",i)
print("List of float: ",f)
print("List of string: ",s)


#Q5. Even and odd numbers list
odd=[]
even=[]
for i in range(1,101):
   if(i%2==0): 
     even.append(i)
   else: 
     odd.append(i)
print("Odd numbers list: ",odd) 
print("Even numbers list: ",even)


#Q6. Pattern printing
for i in range(1,5):
  for j in range(1,i+1):
    print("*",end="")
  print("")


#Q7. User defined dictionay
d={}
print("Enter 5 dictionary elements: ")
for i in range(0,5):
   k=input("key: ")
   d[k]=input("value: ")
print("Dictionary elements are: ")
for k in d:
   print(k," : ",d[k])


#Q8. Searching and deleting element from list
l=[]
print("Enter 5 list elements: ")
for i in range(0,5):
  l.append(int(input()))

ele=int(input("Enter element to delete: "))
f=0
for i in l:
  if(i==ele): 
    f=1
    del i
    break
if(f==1): 
  print("Element deleted successfully")
else:
  print("Element not found")


