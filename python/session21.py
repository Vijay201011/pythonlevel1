from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("checkboxes and dropdown")
#checkboxes are something which helps us to select one or more options
#we created an integer variable because the person will either get 1 or 0
def hello():
    if a.get()==1 and b.get()==0:
        l1.config(text="python is selected")
    if a.get()==0 and b.get()==1:
        l1.config(text="c++ is selected")
    if a.get()==1 and b.get()==1:
        l1.config(text="python and c++ is selected")
    if a.get()==0 and b.get()==0:
        l1.config(text="neither are selected")
a=IntVar()
c1=Checkbutton(root,text="python",onvalue=1,offvalue=0,variable=a)
c1.grid(row=1,column=1)
#onvalue=1 means if the person selects the checkbox then you will get the 1value and if the person doesnt select-
#the checkbox, then we get 0value and for that we have used offvalue=0
#in this case we are going to create a tkinter variable for each one of them.


b=IntVar()
c2=Checkbutton(root,text="c++",onvalue=1,offvalue=0,variable=b)
c2.grid(row=2,column=1)
l1=Label(root)
l1.grid(row=3,column=2)
i=Button(root,text="hi",command=hello)
i.grid(row=4,column=3)
root.mainloop()