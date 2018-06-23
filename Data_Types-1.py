#Q1. User defined List
l=[]
print("Enter 10 list elements: ")
for i in  range(0,10):
  l.append(input())
print("List : ",l)



#Q2. Adding elements to Q1. created list
l=[]
print("Enter list elements: ")
for i in  range(0,10):
  l.append(input())
print("Original List : ",l)

l1=['google','apple','facebook','microsoft','tesla']
l+=l1
print("Updated List : ",l)



#Q3. Frequency of objects
l=[1,2,3,3,4,4,4,5,5,5,6,6,6,6]
print("List: ",l)
s=set(l)
for i in s:
  print(i," occurs ",l.count(i)," times.")



#Q4. Sorting list in ascending order
l=[]
print("Enter 10 list elements: ")
for i in  range(0,10):
  l.append(int(input()))
print("Orginal List : ",l)
l.sort()
print("Sorted List : ",l)



#Q5. Merging twoo list and sorting it in ascending order
A=[1,4,7,9,10]
print("Elements of list A: ",A)
B=[2,3,5,6,8]
print("Elements of list B: ",B)
C=A+B
C.sort()
print("Elements of list C: ",C)



#Q6. Stack and Queue implementation using list
#a.Stack
stack=[1,2,3]
print(stack)
print("Pushing: 4")
stack.append(4)
print(stack)
print("Pushing: 5")
stack.append(5)
print(stack)
print("Popping: ",stack.pop())
print(stack)
print("Popping: ",stack.pop())
print(stack)

#b.Queue
queue=[1,2,3]
print(queue)
print("Adding element to queue: 4")
queue.append(4)
print(queue)
print("Removing one element from queue")
queue.pop(0)
print(queue)
print("Adding element to queue: 5")
queue.append(5)
print(queue)
print("Removing one element from queue")
queue.pop(0)
print(queue)
#OPTIONAL QUESTION--count even and odd numbers in the above queue(list)
counteve=0
for i in queue:
  if(i%2==0): counteve+=1
print("Even numbers in queue: ",counteve)
print("Odd numbers in queue: ",len(queue)-counteve)
