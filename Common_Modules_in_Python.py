# Q1. Time tuple in python represents the various time modules that provides functions to display or manipulate the time values. The two standard representation of time are Epoch (which gives time in UTC a.k.a. GMT format) and the other is a tuple of 9 integers giving local time. These tuples are year, month, day, hours, minutes, seconds, weekday, Julian day, DST flag.



#Q2.
import datetime
print(datetime.datetime.now())

#Q3.
import datetime
x=datetime.datetime.now()
print(x.strftime(%B))

#Q4.
import datetime
x=datetime.datetime.now()
print(x.strftime(%A))

#Q5.
import datetime
x=datetime.datetime.now()
print(x.strftime(%d))

#Q6.
import time
print("Local Time is = ", time.localtime(time.time()))

#Q7.
import math
num=int(intput("Enter the number"))
f=math.factorial(x)
print("Factorial of %d is %d" %(num,f))

#Q8.
import math
x=int(input("Enter 1st number"))
y=int(input("Enter 2nd number"))
gcd=math.gcd(x,y)
print("GCD of %d and %d is = %d" %(x,y,gcd))

#Q9.
#1.
import os
print(os.getcwd())

#2.
import os
print(os.environ
