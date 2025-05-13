from tkinter import *

root=Tk()
root.title("Invoice Project")
root.geometry("600x600")
root.configure(bg="blue")

l4=Label(root,text="Items",bg="green",fg="white")
l4.grid(row=3,column=0,pady=10)
l5=Label(root,text="Quantity",bg="green",fg="white")
l5.grid(row=3,column=1,pady=10)
l6=Label(root,text="Price",bg="green",fg="white")
l6.grid(row=3,column=2,pady=10)
l7=Label(root,text="1",bg="green",fg="white")
l7.grid(row=4,column=0,pady=10)
e4=Entry(root)
e4.grid(row=4,column=1,pady=10)
e5=Entry(root)
e5.grid(row=4,column=2,pady=10)
l8=Label(root,text="2",bg="green",fg="white")
l8.grid(row=5,column=0,pady=10)
e6=Entry(root)
e6.grid(row=5,column=1,pady=10)
e7=Entry(root)
e7.grid(row=5,column=2,pady=10)
l9=Label(root,text="3",bg="green",fg="white")
l9.grid(row=6,column=0,pady=10)
e8=Entry(root)
e8.grid(row=6,column=1,pady=10)
e9=Entry(root)
e9.grid(row=6,column=2,pady=10)

l10=Label(root,text="4",bg="green",fg="white")
l10.grid(row=7,column=0,pady=10)
e10=Entry(root)
e10.grid(row=7,column=1,pady=10)
e11=Entry(root)
e11.grid(row=7,column=2,pady=10)

l11=Label(root,text="5",bg="green",fg="white")
l11.grid(row=8,column=0,pady=10)
e12=Entry(root)
e12.grid(row=8,column=1,pady=10)
e13=Entry(root)
e13.grid(row=8,column=2,pady=10)

l12=Label(root,text="6",bg="green",fg="white")
l12.grid(row=9,column=0,pady=10)
e14=Entry(root)
e14.grid(row=9,column=1,pady=10)
e15=Entry(root)
e15.grid(row=9,column=2,pady=10)

l14=Label(root,text="7",bg="green",fg="white")
l14.grid(row=10,column=0,pady=10)
e16=Entry(root)
e16.grid(row=10,column=1,pady=10)
e17=Entry(root)
e17.grid(row=10,column=2,pady=10)

l15=Label(root,text="Total",bg="green",fg="white")
l15.grid(row=11,column=0,pady=10)
l16=Label(root)
l16.grid(row=11,column=1,pady=10)
l17=Label(root)
l17.grid(row=11,column=2,pady=10)




def quantity():
    t1=float(e4.get())
    t2=float(e5.get())
    t3=float(e6.get())
    t4=float(e7.get())
    t5=float(e8.get())
    t6=float(e9.get())
    t7=float(e10.get())
    t8=float(e11.get())
    t9=float(e12.get())
    t10=float(e13.get())
    t11=float(e14.get())
    t12=float(e15.get())
    t13=float(e16.get())
    t14=float(e17.get())
    total1=(t1+t3+t5+t7+t9+t11+t13)
    l16.config(text=total1)


def price():
    t1=float(e4.get())
    t2=float(e5.get())
    t3=float(e6.get())
    t4=float(e7.get())
    t5=float(e8.get())
    t6=float(e9.get())
    t7=float(e10.get())
    t8=float(e11.get())
    t9=float(e12.get())
    t10=float(e13.get())
    t11=float(e14.get())
    t12=float(e15.get())
    t13=float(e16.get())
    t14=float(e17.get())
    total2=(t2+t4+t6+t8+t10+t12+t14)
    l17.config(text=total2)





b=Button(root,text="Total Quanitity",bg="orange",width=14,height=2,command=quantity)
b.grid(row=12,column=1,pady=10)
c=Button(root,text="Total rate",bg="orange",width=14,height=2,command=price)
c.grid(row=12,column=2,pady=10)



#we are going to download the pdf by displaying the text on the canvas. 
#Canvas is usually used for drawing purposes but we are going to put text on it.
#We will use the canvas component from the library report lab










root.mainloop()