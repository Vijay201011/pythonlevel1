#id, name,email,grade,address
#and create add function to add the details, create getdetail function to gte details from db, delete function
#take reference from the last project, second function n edit function code need to do.


import sqlite3
db=sqlite3.connect("database.db")

csr=db.cursor()
sql="""
create table student(
Id int
Name text
Email varchar(100)
Grade int
Address varchar(30))
"""
csr.execute(sql)
db.commit()

def add():
    
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    sql=()


from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("tk")
l1=Label(root,text="ID")
l1.grid(row=0,column=0)

e1=Entry(root)
e1.grid(row=0,column=1)

l2=Label(root,text="Name")
l2.grid(row=1,column=0)

e2=Entry(root)
e2.grid(row=1,column=1)

l3=Label(root,text="Email")
l3.grid(row=2,column=0)

e3=Entry(root)
e3.grid(row=2,column=1)

l4=Label(root,text="Grade")
l4.grid(row=3,column=0)

e4=Entry(root)
e4.grid(row=3,column=1)

l5=Label(root,text="Address")
l5.grid(row=4,column=0)

e5=Entry(root)
e5.grid(row=4,column=1)

b=Button(root,text="Add",width=25,height=1,command=add)
b.grid(row=6,column=1)

b1=Button(root,text="Update",width=25,height=1)
b1.grid(row=7,column=1)

b2=Button(root,text="Delete",width=25,height=1)
b2.grid(row=8,column=1)

b3=Button(root,text="Query",width=25,height=1)
b3.grid(row=9,column=1)



root.mainloop()





