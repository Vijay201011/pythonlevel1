#-------------------------------------tkinter--------------------------------------
#tkinter is a gui library which is used to create interface or desktop apps, softwares in python. 
#baisc steps to follow
#1. import tkinter library
#2. create screen using Tk()
#3. create title()  and geometry() means size
#4. give background color using configure(). its an optional
#5. create labels, buttons, textbox etc...
#6. use mainloop() at the end so that our page continues to display and never closes.it is always used at the end.

#Step 1 to 4 and 6 are basics which we need to everytime. 5 will change according to what we want craete or need.

#------------------------------------set the positions of wedgets---------------------------
#the componenets are called as widgets. we can se position 
#1. pack() : if we want to se wigets one after the other and then use pack()
#2. grid() :set teh widget horizontal and vertical.
#3. place() : the widget position in x and y
#we have to use one throught the () 
#always create a function and do the function coding in there and whenever we want some action to happen, on that-
#we can call this function eg- if we want to click the button and the answer should come, then we should do the-
#coding inside the function to display the answer and then call this function on the button, which means we do-
#all our calculations in the function and then call it in the button. 
#Whenever we want to get the value from the textboxes, we can use the get function or we can create the-
#tkinter variable and get the value from there. (refer to calculator app)
#if we want to update the answer in a label, we use config. example, L.config(text="")
#entry box always accepts the answer as a text, so the value that we are getting, we want as a number-
#then convert it into int() or float()
#in order to close this screen, we use the inbuild function called as destroy eg.
#screenname.destroy
from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("Introduction to tkinter")
root.configure(bg="green")

#Label is ued to text 
#buttons for buttons
l1=Label(root,text="My first aoftware")
l1.grid(row=0, column=0)

b=Button(root, text="Clikc me")
b.grid(row=1, column=0)

c=Button(root, text="Clikc me")
c.grid(row=2,column=0)
root.mainloop()

d=Button(root, text="Clikc me")
d.grid(row=3,column=2)
root.mainloop()



