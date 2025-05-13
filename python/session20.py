from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root=Tk()
root.geometry("600x600")
root.title("uploading and Saving Files")

def save():
    file=filedialog.asksaveasfile(initialdir="/",defaultextension=".txt",filetypes=[("python files","*.py"), ("text Document", "*.txt"), ("Html Document", "*.html")])
#steps to follow:
#1, first import file dialog at the top as the function "ask save as file name" is from this class
#2, use asksaveasfilename() inside this, we have to write down all of the file types which will be allowed to download
#we have to mention the extension of all of the files that we want or have to download

def upload():
    #Steps
    #1. use askopenfilename(), inside w give initialdir, defaultextension, filetypes, this will only open a iamge
    #2. because we are uploading a image that is why we will use ImageTk.PhotoImage() we use all those steps to upload  and dispay image on screen
    file=filedialog.askopenfilename(initialdir="/",defaultextension=".txt",filetypes=[("python files","*.py"), ("text Document", "*.txt"), ("Html Document", "*.html"),("image files","*.png")])
    img=Image.open(file) # file vaiable is that where our image which is elected wil; be stored
    img=ImageTk.PhotoImage(img)
    l=Label(image=img)
    l.image=img
    l.grid(row=0, column=0)

upload=Button(root,width=5,height=2,text="upload", command=upload)
upload.grid(row=0,column=0)
saving=Button(root,width=5,height=2,text="save", command=save)
saving.grid(row=0,column=1)

#------------------------------------Slider-----------------------------------
#scale is the slider and from there we can select the number from a given range
def hello():
    a=s.get()
    l1.config(text=a)

s=Scale(root,orient=HORIZONTAL,from_=1,to=10)
s.grid(row=1,column=0)
l1=Label(root)
l1.grid(row=2,column=1)
b=Button(root,width=3,height=2,text="hi",command=hello)
b.grid(row=2,column=2)
root.mainloop()