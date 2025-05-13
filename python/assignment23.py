from tkinter import *
root=Tk()
root.geometry("600x600")
root.title("CodeVidhya")


b=Label(root,text="CodeVidhya",height=1,width=20)
b.grid(row=0,column=0)

l=Listbox(root)
l.grid(row=1,column=0)
l.insert(END,"User 1")
l.insert(END,"User 2")
l.insert(END,"User 3")
l.insert(END,"User 4")
l.insert(END,"User 5")
l.insert(END,"User 6")
l.insert(END,"User 7")
l.insert(END,"User 8")
l.insert(END,"User 9")
l.insert(END,"User 10")
l.insert(END,"User 11")


root.mainloop()
