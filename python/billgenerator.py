from tkinter import *
from reportlab.pdfgen import canvas
root=Tk()
root.title("Bill Generator")
root.geometry("600x600")
root.configure(bg="green")
l1=Label(root,text="Name",bg="green",fg="white")
l1.grid(row=0,column=0,pady=10)
e1=Entry(root)
e1.grid(row=0,column=1,pady=10)
l2=Label(root,text="Email",bg="green",fg="white")
l2.grid(row=1,column=0,pady=10)
e2=Entry(root)
e2.grid(row=1,column=1,pady=10)
l3=Label(root,text="Phone Number",bg="green",fg="white")
l3.grid(row=2,column=0,pady=10)
e3=Entry(root)
e3.grid(row=2,column=1,pady=10)
l4=Label(root,text="Items",bg="green",fg="white")
l4.grid(row=3,column=0,pady=10)
l5=Label(root,text="Quantity",bg="green",fg="white")
l5.grid(row=3,column=1,pady=10)
l6=Label(root,text="Price",bg="green",fg="white")
l6.grid(row=3,column=2,pady=10)
l7=Label(root,text="Strawberry",bg="green",fg="white")
l7.grid(row=4,column=0,pady=10)
e4=Entry(root)
e4.grid(row=4,column=1,pady=10)
e5=Entry(root)
e5.grid(row=4,column=2,pady=10)
l8=Label(root,text="Chocolate",bg="green",fg="white")
l8.grid(row=5,column=0,pady=10)
e6=Entry(root)
e6.grid(row=5,column=1,pady=10)
e7=Entry(root)
e7.grid(row=5,column=2,pady=10)

l9=Label(root,text="Vanilla",bg="green",fg="white")
l9.grid(row=6,column=0,pady=10)
e8=Entry(root)
e8.grid(row=6,column=1,pady=10)
e9=Entry(root)
e9.grid(row=6,column=2,pady=10)

l10=Label(root,text="Mango",bg="green",fg="white")
l10.grid(row=7,column=0,pady=10)
e10=Entry(root)
e10.grid(row=7,column=1,pady=10)
e11=Entry(root)
e11.grid(row=7,column=2,pady=10)

l11=Label(root,text="Cookie Dough",bg="green",fg="white")
l11.grid(row=8,column=0,pady=10)
e12=Entry(root)
e12.grid(row=8,column=1,pady=10)
e13=Entry(root)
e13.grid(row=8,column=2,pady=10)

l12=Label(root,text="Banana",bg="green",fg="white")
l12.grid(row=9,column=0,pady=10)
e14=Entry(root)
e14.grid(row=9,column=1,pady=10)
e15=Entry(root)
e15.grid(row=9,column=2,pady=10)

l14=Label(root,text="Caramel",bg="green",fg="white")
l14.grid(row=10,column=0,pady=10)
e16=Entry(root)
e16.grid(row=10,column=1,pady=10)
e17=Entry(root)
e17.grid(row=10,column=2,pady=10)


l15=Label(root,text="Total",bg="green",fg="white")
l15.grid(row=11,column=0,pady=10)
l16=Label(root)
l16.grid(row=11,column=1,pady=10)


def total():
    global total1
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
    total1=(t1*t2)+(t3*t4)+(t5*t6)+(t7*t8)+(t9*t10)
    l16.config(text=total1)



def billgenerator():
    r1=e1.get()
    c=canvas.Canvas(r1+".pdf")
    #by using drawstring we will put every information on the canvas
    c.drawString(100,800,"invoice")#the numbers are the x and y numbers
    c.drawString(100,750,"Name"+" "+e1.get())
    c.drawString(100,700,"Email"+" "+e2.get())
    c.drawString(100,650,"Phone Number"+" "+e3.get())
    c.drawString(100,600,"Strawberry"+" "+e4.get())
    c.drawString(100,550,"Chocolate"+" "+e6.get())
    c.drawString(100,500,"Vanilla"+" "+e8.get())
    c.drawString(100,450,"Mango"+" "+e10.get())
    c.drawString(100,400,"Cookie Dough"+" "+e12.get())
    c.drawString(100,350,"Banana"+" "+e14.get())
    c.drawString(100,300,"Caramel"+" "+e16.get())
    c.drawString(100,250,"Total Price"+" "+str(total1))
    c.save()
    
    


b=Button(root,text="Total",bg="orange",width=14,height=2,command=total)
b.grid(row=12,column=1,pady=10)
c=Button(root,text="Bill Generator",bg="orange",width=14,height=2,command=billgenerator)
c.grid(row=12,column=2,pady=10)















root.mainloop()