from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("Grade Calculator")
root.configure(bg="white")

l1=Label(root,text="English",fg='black',bg="grey",font=("ariel",15))
l1.grid(padx=20,row=0,column=0)

e1=Entry(root,width=30)
e1.grid(padx=20,row=0,column=1)

l2=Label(root,text="Analytical Grade",fg='black',bg="grey",font=("ariel",15))
l2.grid(padx=20,row=1,column=0)

e2=Entry(root,width=30)
e2.grid(padx=20,row=1,column=1)

l3=Label(root,text="General Knowledge",fg='black',bg="grey",font=("ariel",15))
l3.grid(padx=20,row=2,column=0)

e3=Entry(root,width=30)
e3.grid(padx=20,row=2,column=1)

l4=Label(root,text="Total",fg="black",bg="grey",font=("ariel",15))
l4.grid(padx=20,row=3,column=0)

l5=Label(root,fg="black",bg="white",font=("ariel",15))
l5.grid(padx=20,row=3,column=1)

l6=Label(root,text="Average",fg="black",bg="grey",font=("ariel",15))
l6.grid(padx=20,row=4,column=0)

l7=Label(root,fg="black",bg="white",font=("ariel",15))
l7.grid(padx=20,row=4,column=1)

l8=Label(root,text="Grade",fg="blue",bg="grey",font=("ariel",15))
l8.grid(padx=20,row=5,column=0)

l9=Label(root,fg="black",bg="white",font=("ariel",15))
l9.grid(padx=20,row=5,column=1)

#we always create a function before calling
def calculate():
    #always do the function coding in the function and then call that function in the buttons
    english=int(e1.get())
    analytical=int(e2.get())
    general=int(e3.get())
    total=english+analytical+general
    l5.config(text=total)
    average=total/3
    l7.config(text=average)
    if total>130:
        l9.config(text="Pass")
    else:
        l9.config(text="Fail")

exit=Button(root,width=20,height=1,text="Exit",command=root.destroy)
exit.grid(row=7,column=0)

calculate1=Button(root,width=20,height=1,text="Calculate",command=calculate)
calculate1.grid(row=7,column=1)













root.mainloop()