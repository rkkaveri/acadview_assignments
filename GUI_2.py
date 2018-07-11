#Q1.Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.

from tkinter import *

root=Tk()
root.title("Airtel User List!")
root.geometry('250x240')

d={'Smith':7891234123,
   'Wendy':9801234456,
   'Jenny':8890318789,
   'Rohit':7799331450,
   'Shashi':7348912123,
   'Aubrie':9012458129,
   'Sandy':7809714123}

#displaying dictionary contents in list GUI 
f1=Frame(root)    
f1.pack()

sb=Scrollbar(f1)
sb.pack(side=RIGHT, fill=Y)

listL=Listbox(f1,yscrollcommand=sb.set)

for i in d:
   listL.insert(END,i)

listL.pack(side=LEFT, fill=X)
sb.configure(command=listL.yview)

root.mainloop()




#Q2.In the same tkinter file as created above, create a function to insert items into the dictionary.

from tkinter import *

root=Tk()
root.title("Airtel User List!")
root.geometry('250x240')

d={'Smith':7891234123,
   'Wendy':9801234456,
   'Jenny':8890318789,
   'Rohit':7799331450,
   'Shashi':7348912123,
   'Aubrie':9012458129,
   'Sandy':7809714123}

#displaying dictionary d contents in list GUI 
f1=Frame(root)    
f1.pack()

sb=Scrollbar(f1)
sb.pack(side=RIGHT, fill=Y)

listL=Listbox(f1,yscrollcommand=sb.set)

for i in d:
   listL.insert(END,i)

listL.pack(side=LEFT, fill=X)
sb.configure(command=listL.yview)

#adding new entries in dictionary and updating the list
def addval():
     d[k.get()]=v.get()
     listL.insert(END,k.get())

#creating GUI for user input
f=Frame(root)
f.pack()
labelL=Label(f,text="Name ")
labelL.grid(row=0, column=0)
labelL=Label(f,text="Mobile No.")
labelL.grid(row=1,column=0)

k=Entry(f)
k.grid(row=0,column=1)
v=Entry(f)
v.grid(row=1,column=1)

#initialising button to trigger addval() function
b=Button(f,text="Add in Dictionary",command=addval)
b.grid(row=2,column=1)

root.mainloop()

