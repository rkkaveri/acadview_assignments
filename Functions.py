#Q1.Area of Circle
def area(r):
  return 2*3.41*r*r
r=int(input("enter radius of circle"))
print("Area= ",area(r))


#Q2. Perfect Number
def perfect():
  for no in range(1,1000):
    sum=1
    for i in range(2,no):
        if(no%i==0): 
           sum+=i
    if(sum==no):
        print(no," ")

print("Perfect numbers are :\n")
perfect()



#Q3. Table of 12
def table12(i):
  if (i<=10): 
    print(" 12 x ",i," = ",(12*i))
    i+=1  
    table12(i)

table12(1)



#Q4. Power using recursion
base=int(input("enter base value: "))
expo=int(input("enter exponent value: "))
def pow(x,y):
   if (y==1):
      return x
   else:
      return (x*pow(x,y-1))

print("Power is : ",pow(base,expo))



#Q5. Calculating Factorial of number and storing in dictionary
facts={}
def factorial(n):
   fact=1
   for i in range(1,n+1):
       fact *=i
   print("Factorial of %d is : %d"%(n,fact))
   facts[5]=fact
   print(facts)
num=int(input("Enter number "))
factorial(num)
