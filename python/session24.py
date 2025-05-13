import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Define the Notepad class
class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad App")
        self.root.geometry("600x600")

        # Create text area for typing
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Create the menu bar
        self.menu_bar()

    def menu_bar(self):
        # Step 1: Create the menu
         #we will be creating a menubar widget 
        #menubar means the bar which is created at the top and when we click on these bars, multiple items come
        #menubar includes file,edit,selection,view,Go,run given at the top of the the visual studio code
        #steps to create it 
        #1. First we create a menu
        #2. Then we create the menu bar like file, edit,selection,view,run,go
        #3. then we use add_command to create the menu items which will come when we click file, edit,selection,view,run,go
        #4. Add_cascade is used to give the name of the menubar
        Mb = tk.Menu(self.root)

        # Step 2: Create "File" menu
        file_menu = tk.Menu(Mb, tearoff=0)
        file_menu.add_command(label="New", command=self.new)
        file_menu.add_command(label="Open", command=self.open)
        file_menu.add_command(label="Save", command=self.save)
        file_menu.add_command(label="Exit", command=self.exit)
        Mb.add_cascade(label="File", menu=file_menu)

        # Step 3: Create "Edit" menu
        edit_menu = tk.Menu(Mb, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        Mb.add_cascade(label='Edit', menu=edit_menu)

        # Step 4: Create "About Us" menu
        aboutus_menu = tk.Menu(Mb, tearoff=0)
        aboutus_menu.add_command(label="About Us", command=self.aboutus)
        Mb.add_cascade(label="About Us", menu=aboutus_menu)

        # Step 5: Attach menu to the root window
        self.root.config(menu=Mb)

    # Clears the text area
    def new(self):
        self.text_area.delete(1.0, tk.END)

    # Opens a file and displays its content
    def open(self):
        file_path = filedialog.askopenfilename(
            initialdir="/",
            defaultextension=".txt",
            filetypes=[("Python Files", "*.py"), ("Text Documents", "*.txt"), ("HTML Documents", "*.html")]
        )
        if file_path:
            with open(file_path, "r") as file:
                 #first ask open file opens the file, then we use read function to get the data from there and then
            #we use insert function to put all of our text file, data, into text area
                content = file.read()  # Read file contents
                self.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_area.insert(tk.END, content)  # Insert content into text area

    # Saves current content into a file
    def save(self):
        file_path = filedialog.asksaveasfilename(
            initialdir="/",
            defaultextension=".txt",
            filetypes=[("Python Files", "*.py"), ("Text Documents", "*.txt"), ("HTML Documents", "*.html")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))  # Write text area content to file

    # Closes the application
    def exit(self):
        self.root.destroy()

    # Cut selected text
    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    # Copy selected text
    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    # Paste copied text
    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    # Show "About Us" info box
    def aboutus(self):
        messagebox.showinfo("Info", "Notepad is used to create and edit text files.")

# Create the main window
root = tk.Tk()
app = Notepad(root)
root.mainloop()