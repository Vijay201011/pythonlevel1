from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("Listbox and Scrollbar")

f=Frame()
s=Scrollbar(f,orient=VERTICAL)
#listbox is a box which has a lot of items inside it 
#we can select all of these items one by one
l=Listbox(root,yscrollcommand=s.set,selectmode=MULTIPLE)
#to connect the scrollbar and listbox, inside the listbox we have to use yscrollcommand
#yscrollbar means vertical scrollbar will be attached to the listbox
#y is y axis and scroll is scrollbar
s.config(command=l.yview)
#like scrollbar has been connected to the listbox, we have to connect the listbox to the scrollbar as well 
#by using yview
s.pack(side=RIGHT,fill=Y)
f.pack()
l.pack()
l.insert(END,"apple")
l.insert(END,"banana")
l.insert(END,"pear")
l.insert(END,"grape")
l.insert(END,"mango")


k=Label(root)
k.pack()

def delete():
    l.delete(ANCHOR)
    k.config(text="")

def select():
    #in select we get the value from the listbox and display as a label
    k.config(text=l.get(ANCHOR))
    #anchor means whatever item is selected it gets only that item
    
def deleteall():
    l.delete(0,END)

def deletemultiple():
    for item in l.curselection():
        #curselection means the items which are selected so we use a for loop to get those items which are selected
        #and eventually delete them items
        l.delete(item)
        k.config(text="")

def selectmultiple():
    result=""
    #with the help of the for loop we get the items which are selected again and then display them as a label on-
    #the screen
    for item in l.curselection():
        result=result+str(l.get(item))+"\n"#/n makes the data go to the next line
    k.config(text=result)

a=Button(root,text="delete",command=delete)
a.pack()
b=Button(root,text="select",command=select)
b.pack()
c=Button(root,text="delete all",command=deleteall)
c.pack()
d=Button(root,text="delete multiple",command=deletemultiple)
d.pack()
e=Button(root,text="select multiple",command=selectmultiple)
e.pack()

#delete, select,deletall, delete multiple, select multiple,



root.mainloop()