#Q1. Leap year or not
year=int(input("Enter the year: "))
if(year%4==0):
  print("It's a leap year")
else:
  print("It's not a leap year")


#Q2. Dimensions are of a square or rectangle
d1=int(input("Enter first dimension: "))
d2=int(input("Enter second dimension: "))
if(d1==d2):
  print("Dimensions are of a Square")
else:
  print("Dimensions are of a Rectangle")


#Q3. Oldest and youngest age determination
a=int(input("Enter A's age: "))
b=int(input("Enter B's age: "))
c=int(input("Enter C's age: "))
oldest=""
youngest=""
if(a>b and a>c):
   oldest="A"
   if(b>c): 
     youngest="C"
   else: 
     youngest="B"
elif(b>a and b>c):
   oldest="B"
   if(a>c): 
     youngest="C"
   else: 
     youngest="A"
else:
   oldest="C"
   if(a>b): 
     youngest="B"
   else: 
     youngest="A"
print("%s is the oldest and %s is the youngest"%(oldest,youngest))

 
#Q4. Prize won through points
points=int(input("Enter points: "))
if(points>200):
   print("Points cannot be more than 200")
elif(points>=1 and points<=50):
   print("Sorry! No prize this time.")
elif(points>=51 and points<=150):
   print("Congratulations! You won a Wooden Dog!")
elif(points>=151 and points<=180):
   print("Congratulations! You won a Book!")
else:
   print("Congratulations! You won a Chocolates!")


#Q5. Predicting total cost of user
units=int(input("Enter number of units to purchase: "))
cost=units*100
if(cost>1000):
  cost-=cost*10/100
print("Your total cost: Rs.",cost)
