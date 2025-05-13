from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("600x600")
root.title("Message Box")
#message box means a pop up notifier which comes up on the screen. 
#for that, first we import the message box at the top
#then, there are different functions like warning notifier, error notifier, message pop up, asking questions etc
#to show simple messages, 
messagebox.showinfo("information", "your file has been downloaded")
#to give warning
messagebox.showwarning("warning","there is a virus in the file that has been downloaded")
#to show error
messagebox.showerror("error","there is an error in the file that has been downloaded")
#to ask a question have different functions with different buttons
messagebox.askokcancel("question","do you want to download this file?")
messagebox.askquestion("question", "do you want to download the file?")
messagebox.askretrycancel("question","do you want to download the file?")
messagebox.askyesno("question","do you want to download the file?")
messagebox.askyesnocancel("question","do you want to download the file?")

#the coding of new screen we can do it in a function and call that function on that button where we want to click
#and open the new screen
def newscreen():
    screen1=Tk()
    screen1.geometry("600x600")
    screen1.title("new screen")
    screen1.configure(bg="black")
    l1=Label(screen1,text="hello")
    l1.grid(row=3,column=3)
b1=Button(root,width=6,height=3,text="click me",command=newscreen)
b1.grid(row=2,column=2)
root.mainloop()
