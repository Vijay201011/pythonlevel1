#-----------------------------Images, icons and frames-------------------------

from tkinter import *
from PIL import ImageTk, Image

sc=Tk()
sc.geometry("600x600")
#to give icon:
#1. load or store image in variable
#2. use iconbitmap() for .ico or iconphoto() for png to give image

a=PhotoImage(file="Screenshot (30).png")
sc.iconphoto(False, a)

#image on screen
#4 Steps to give image on screen
#1. import PIL library which is pillow library at top which has function ImageTk, Image .
#very first time using in any device we ahve to install PIL : command in comand prompt : pip install pillow
#2. use Image.open() to open the image
#for adjusting size of image we use resize  eg : img=img.reszie((100, 100)) width and height . this is optional
#3. use ImageTk.PhotoImage() to load image in variable
#4. use label to display or put image on screen. label give text or image.

img=Image.open("Screenshot (30).png")
img=ImageTk.PhotoImage(img)
l=Label(image=img)
l.image=img
l.grid(row=0, column=0)

#Frame : Frame is like a box where we put things to make it look better eg : putting two button together in 1 box
#it craetes a border like thing eg : many login pages have this border nad inside that username password button are there etc...

f=Frame(sc)
f.grid(row=1, column=1)

#whatever we want inside that frame we give its name for
b=Button(f, text="Click me")
b.grid(row=1, column=1)

b1=Button(f, text="Submit")
b1.grid(row=1, column=0)
mainloop()