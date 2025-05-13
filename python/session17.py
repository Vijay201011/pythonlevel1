#declaring the variable global means that if we make any changes to one function to that variable-
#then the other functions will be able to see that changed value
#if we do not declare it as global, then if we make any changes to the variable inside the function-
#then other functions will not be able to see those changes
from tkinter import *
#  * means all - anything from the library
root=Tk()
root.geometry("400x400")
root.title("Calculator")
#tkinter variable
#tkinter variable is a variable that is used to store values that comef rom the user through tkinter widgets - 
#like entry box, check boxes, radio boxes etc.
#example - if we create a tkinter variable for the entry box, the value entered in a box by the user - 
#can be stored here in the tkinter variable
#to create a tkinter variable we can use one of the 4 functions - StringVar(), DoubleVar(), BoolVar(), IntVar().
#whatever value is coming from the user, according to that we create a variable. 
#if integer value is coming, we use IntVar() to create a variable. 
#in this calculator, we will use one tkinter variable for the entry box.
#entry boxes always accept text values 
#tkinter variable and the widget for which we have created can be anything in the case where the input box
#and tkinter variable are automatically connected that means if we enter any value in entry box it automatically-
#goes to the tkinter variable similarly, if we enter any value in the tkinter variable, it will automatically - 
#go into the tkinter variable
expression=""
#when we press any number button or sign button, it should go inside the box
def press(num):
    expression=expression+str(num)
#expression represents the previous number and num represents the current number that we have pressed so - 
# with the help of plus sign, we are joining them together
#and storing the value back in expression variable
    a.set(expression)
#set is used to put the answer in the tkinter variable
#when equal button was pressed we need to do the calculation
def equal():
#we will use one inbuilt function eval which performs all of the mathematical operations automatically
#eval will make us only have to give the things in the entry box and eval will automatically do the calculation
#we do not have to use if function - eval does it for us with the mathematical signs and numbers
    global expression
    total=str(eval(expression))
    a.set(total)
def clear1():
    global expression
    expression=''
    a.set(expression)

#calling the functions in tkinter-
#number 1, calling the parameter functions
#a function where a variable is passed around in a round bracket
#command=lambda:function name(value)
#lamdda is a key word used to call the parameter functions
#number 2, calling a normal function
#command=function name

#by using set function, we are putting the value in a variable and from variable, it will automatically - 
#go into the entry box
a=StringVar()
#creating Entry box
e=Entry(root,width=30,textvariable=a)
#we have to always connect the tkinter variable
#Does not have any height property
#ipadx,ipady,padx,pady
#ipadx and ipady is used to give the spacing outside the buttons, labels, 
#if we want to move anything to the left or right, we use ipadx because x means x axis
#if we want to move anything up or down, we use ipady because y means y axis
#padx is used to give the space inside the component like giving the space inside the button - 
#making the button bigger in size
#for left right, we use padx and for up and down we use pady
e.grid(row=0,column=0,columnspan=4,pady=10)

#column span means combining the columns
plus=Button(root,width=5,height=2,text="+",bg="dark grey",fg="white", command=lambda:press("+"))
plus.grid(row=1,column=0)
minus=Button(root,width=5,height=2,text="-",bg="dark grey",fg="white", command=lambda:press("-"))
minus.grid(row=1,column=1)
times=Button(root,width=5,height=2,text="x",bg="dark grey",fg="white", command=lambda:press("*"))
times.grid(row=1,column=2)
divide=Button(root,width=5,height=2,text="/",bg="dark grey",fg="white",command=lambda:press("/"))
divide.grid(row=1,column=3)
seven=Button(root,width=5,height=2,text="7",bg="grey",fg="black",command=lambda:press("7"))
seven.grid(row=2,column=0)
eight=Button(root,width=5,height=2,text="8",bg="grey",fg="black",command=lambda:press("8"))
eight.grid(row=2,column=1)
nine=Button(root,width=5,height=2,text="9",bg="grey",fg="black",command=lambda:press("9"))
nine.grid(row=2,column=2)
four=Button(root,width=5,height=2,text="4",bg="grey",fg="black",command=lambda:press("4"))
four.grid(row=3,column=0)
five=Button(root,width=5,height=2,text="5",bg="grey",fg="black",command=lambda:press("5"))
five.grid(row=3,column=1)
six=Button(root,width=5,height=2,text="6",bg="grey",fg="black",command=lambda:press("6"))
six.grid(row=3,column=2)
one=Button(root,width=5,height=2,text="1",bg="grey",fg="black",command=lambda:press("1"))
one.grid(row=4,column=0)
two=Button(root,width=5,height=2,text="2",bg="grey",fg="black",command=lambda:press("2"))
two.grid(row=4,column=1)
three=Button(root,width=5,height=2,text="3",bg="grey",fg="black",command=lambda:press("3"))
three.grid(row=4,column=2)
dot=Button(root,width=5,height=2,text=".",bg="grey",fg="black",command=lambda:press("."))
dot.grid(row=5,column=0)
zero=Button(root,width=5,height=2,text="0",bg="grey",fg="black",command=lambda:press("0"))
zero.grid(row=5,column=1)
clear=Button(root,width=5,height=2,text="C",bg="red",fg="white",command=clear1)
clear.grid(row=5,column=2)
equal=Button(root,width=5,height=10,text="=",bg="green",fg="white",command=equal)
equal.grid(row=2,column=3, rowspan=5)

root.mainloop()
