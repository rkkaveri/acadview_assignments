#Q1.Write a python program using tkinter interface to write Hello World and a exit button that closes the interface. 

from tkinter import *
root=Tk()
root.title("Heya!!")
root.geometry('200x100')
label=Label(root,text="Hello World")
label.pack()
button=Button(root,text='Exit',command=root.destroy)
button.pack()
root.mainloop()




#Q2.Write a python program to in the same interface as above and create a action when the button is click it will display some text. 

from tkinter import *

root=Tk()
root.title("Heya!!")
root.geometry('500x200')
root.configure(background='blue')


def print_msg():
   label=Label(root,text="Welcome to our page user.", font="Courier 15", bg='yellow')
   label.pack()

label=Label(root,text="Press Button Print to view the text", font="Courier", bg='red')
label.pack()

b1=Button(root,text='Print',command=print_msg)
b1.pack(side=LEFT)

b2=Button(root,text='Exit',command=root.destroy)
b2.pack(side=RIGHT)

root.mainloop()





#Q3.Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text. 

from tkinter import *

root=Tk()
root.title("Heya!!")
root.geometry('600x200')
root.configure(background='blue')


frame_1=Frame(root,bg='black')
frame_1.pack() 

label=Label(frame_1,text="Press 'Print' Button to change text", font="Courier 16 bold underline", bg='red')
label.grid(row=0,column=0)

def print_msg():
   label.configure(text="Welcome to our page user.", font="Courier 20", bg='yellow')
   label.grid(row=0,column=0)

b1=Button(root,text='Print',activebackground='green' , activeforeground='white',command=print_msg)
b1.pack(fill=X,side=TOP)

b2=Button(root,text='Exit',activebackground='green' , activeforeground='white',command=root.destroy)
b2.pack(fill=X,side=BOTTOM)

root.mainloop()





#Q4. Q4.Write a python program using tkinter interface to take an input in the GUI program and print it. 

from tkinter import *

root=Tk()
root.title("Heya!!")
root.geometry('600x200')
root.configure(background='blue')

l1=Label(root,text="Enter Your Name Below:")
l1.pack()

e1=Entry(root)
e1.pack()

def print_msg():
   name=e1.get()
   print("User name: ",name)
   txt="Welcome to our page "+name
   label=Label(root,text=txt, font="Courier 16 bold underline", bg='red')
   label.pack(fill=X)

b1=Button(root,text='Submit',activebackground='green' , activeforeground='white',command=print_msg)
b1.pack(fill=X,side=TOP)

b2=Button(root,text='Exit',activebackground='green' , activeforeground='white',command=root.destroy)
b2.pack(fill=X,side=BOTTOM)

root.mainloop()

