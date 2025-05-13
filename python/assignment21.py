from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("pizza toppings")

def pep():
    if i.get()==1:
        l1.config("pepperoni is selected")

    if i.get()==0:
        l1.config("No toppings")

i=IntVar()

f1=Checkbutton(root,text="pepperoni",onvalue=1,offvalue=0,variable=i)
f1.grid(row=1,column=1)


l1=Label(root)
l1.grid(row=3,column=2)
b=Button(root,text="click me",command=pep)
b.grid(row=4,column=3)



root.mainloop()