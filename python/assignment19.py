from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("BMI calculator")
root.configure(bg="white")
#whenever we need to put the answer in an entry box, always create a tkinter variable and give the answer through-
#that. which is done in calculator and BMI. If we want to put the answer as a label, then we can use simple config.
#example, score calculator.
l1=Label(root,text="Height(m.cm eg. 1.65 (165cm))",fg='black',bg="grey",font=("ariel",15))
l1.grid(padx=20,row=0,column=0)
a=StringVar()

e1=Entry(root,width=30)

e1.grid(padx=20,row=0,column=1)

l2=Label(root,text="Weight(kg)",fg='black',bg="grey",font=("ariel",15))
l2.grid(padx=20,row=1,column=0)

e2=Entry(root,width=30)
e2.grid(padx=20,row=1,column=1)

l3=Label(root,text="BMI", fg="black", bg="grey",font=("ariel",15))
l3.grid(padx=0,row=2,column=0)

e3=Entry(root,width=30,textvariable=a)
e3.grid(padx=20,row=2,column=1)




def calculate():
    height1=float(e1.get())
    height=height1*height1
    weight=float(e2.get())
    total=weight/height
    total=str(total)
    a.set(total)


submit=Button(root,width=5,height=1,text="Submit",bg="grey",fg="black",command=calculate)
submit.grid(row=4,column=0)









root.mainloop()
