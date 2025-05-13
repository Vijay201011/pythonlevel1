from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("This is the root window")

def toplevel():
    top=Tk()
    top.geometry=("600x600")
    top.title="open toplevel1"
    l1=Label(top,text=" toplevel1")
    l1.grid(column=3,row=2)
    f=Button(top,text="go to third screen",command=toplevel2)
    f.grid(column=2,row=3)

def toplevel2():
    top2=Tk()
    top2.geometry=("600x600")
    
    l2=Label(top2,text="This is toplevel2")
    l2.grid(row=2,column=2)

    g=Button(top2,text="Exit",command=top2.destroy)
    g.grid(column=2,row=3)

b=Button(root, text="Click for toplevel1", command=toplevel)
b.grid(pady=50)





root.mainloop()