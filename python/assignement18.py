
from tkinter import *
from PIL import ImageTk, Image

hi=Tk()
hi.geometry("600x600")





def image1():
    img=Image.open("Screenshot (30).png")
    img=img.resize((50,50))
    img=ImageTk.PhotoImage(img)
    l=Label(image=img)
    l.image=img
    l.grid(row=1, column=0)

a=Button(hi, text="Back", command=image1)
a.grid(row=0,column=1)

def image2():
    img2=Image.open("Screenshot (75).png")
    img2=img2.resize((50,50))
    img2=ImageTk.PhotoImage(img2)
    l1=Label(image=img2)
    l1.image=img2
    l1.grid(row=1, column=0)
b=Button(hi, text="Forward", command=image2)
b.grid(row=0,column=2)


    
c=Button(hi, text="Exit", command=hi.destroy)
c.grid(row=0,column=3)




hi.mainloop()