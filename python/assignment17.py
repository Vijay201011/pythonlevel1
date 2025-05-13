from tkinter import *
root=Tk()
root.geometry("800x800")
root.title("login page")
root.configure(bg="green")
#style properties
#fg=text colour it can be used to give the colour of the text to every widget eg, button text, entry box text etc
#bg=background colour of the text, button, entry box and every widget
#font is for font family and text size
#padx and pady is used to give the space from the left right top and bottom inside the boxes like button, entry box etc
#ipadx and ipady is used to give the space from the left and from the top. If we want to give a space from the left side - 
#increase the ipadx value and if we want to move it from the top to bottom or down, increase the ipady

l1=Label(root,text="Hey There",fg="white",bg="green",font=("ariel",30))
l1.pack(ipadx=100)

l2=Label(root,text="Enter the details to get started",fg="white",bg="green",font=("ariel",23))
l2.pack(ipadx=100)
#anchor used in pack to give direction w(west), e(east), n(north), s(south)
l3=Label(root,text="Email",fg='white',bg="green",font=("ariel",15))
l3.pack(anchor="w", padx=20)
#when we are using pack, then padx and pady can be used to give the space outside the box-
#and ipadx and ipady can be used to give the space inside the box. opposite thing happens in grid.


e=Entry(root,width=30)
e.pack(anchor="w",padx=20,pady=6,ipady=6)



l4=Label(root,text="Password",fg='white',bg="green",font=("ariel",15))
l4.pack(anchor="w", padx=20)

e=Entry(root,width=30)
e.pack(anchor="w",padx=20,pady=6,ipady=6)








sign_in = Button(root,width=20,height=1,text="sign in")
sign_in.pack()




root.mainloop()



