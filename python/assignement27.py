import sqlite3
from tkinter import *

# Establish database connection
db = sqlite3.connect("data1.db")
csr = db.cursor()

# Corrected SQL Table Creation
sql = """
CREATE TABLE IF NOT EXISTS student(
    ID INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    grade INTEGER,
    address TEXT
)
"""
csr.execute(sql)
db.commit()

# Function to add a new record
def add():
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()

    if not all([a, b, c, d, e]):
        ll.config(text="All fields are required!")
        return

    sql = "INSERT INTO student(ID, name, email, grade, address) VALUES (?, ?, ?, ?, ?)"
    try:
        csr.execute(sql, (a, b, c, d, e))
        db.commit()
        ll.config(text="Record added successfully.")
    except sqlite3.IntegrityError:
        ll.config(text="Error: ID must be unique.")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

# Function to fetch record details
def getdetail():
    a = e6.get()
    if not a:
        ll.config(text="Enter an ID to search.")
        return

    csr.execute("SELECT * FROM student WHERE ID=?", (a,))
    r = csr.fetchone()
  
    if r:
        rr = f"ID: {r[0]}\nName: {r[1]}\nEmail: {r[2]}\nGrade: {r[3]}\nAddress: {r[4]}"
    else:
        rr = "No record found."
    
    ll.config(text=rr)
    e6.delete(0, END)

# Function to delete a record
def delete1():
    b = e6.get()
    if not b:
        ll.config(text="Enter an ID to delete.")
        return

    csr.execute("DELETE FROM student WHERE ID=?", (b,))
    db.commit()
    ll.config(text="Record deleted successfully.")
    e6.delete(0, END)

# Function to edit a record
def edit():
    global e11, e12, e13, e14, e15

    a1 = e11.get()
    b1 = e12.get()
    c1 = e13.get()
    d1 = e14.get()
    e1 = e15.get()
    staff_id = e6.get()

    sql = """
    UPDATE student 
    SET name=?, email=?, grade=?, address=? 
    WHERE ID=?
    """
    csr.execute(sql, (b1, c1, d1, e1, a1))
    db.commit()
    ll.config(text="Record updated successfully.")

# Function to open the update window
def second():
    a = e6.get()
    if not a:
        ll.config(text="Please enter the ID to update.")
        return

    csr.execute("SELECT * FROM student WHERE ID=?", (a,))
    r = csr.fetchone()

    if not r:
        ll.config(text="No record found with this ID.")
        return

    screen2 = Toplevel(root)
    screen2.geometry("400x400")
    screen2.title("Edit")

    global e11, e12, e13, e14, e15

    Label(screen2, text="ID").grid(row=0, column=0)
    e11 = Entry(screen2)
    e11.grid(row=0, column=1)
    e11.insert(0, r[0])
    e11.config(state='readonly')

    Label(screen2, text="Name").grid(row=1, column=0)
    e12 = Entry(screen2)
    e12.grid(row=1, column=1)
    e12.insert(0, r[1])

    Label(screen2, text="Email").grid(row=2, column=0)
    e13 = Entry(screen2)
    e13.grid(row=2, column=1)
    e13.insert(0, r[2])

    Label(screen2, text="Grade").grid(row=3, column=0)
    e14 = Entry(screen2)
    e14.grid(row=3, column=1)
    e14.insert(0, r[3])

    Label(screen2, text="Address").grid(row=4, column=0)
    e15 = Entry(screen2)
    e15.grid(row=4, column=1)
    e15.insert(0, r[4])

    Button(screen2, text="Update", command=edit).grid(row=5, column=1)

# Main window
root = Tk()
root.geometry("600x600")
root.title("Student Management System")

global e1, e2, e3, e4, e5, e6, ll

Label(root, text="ID").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Name").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)

Label(root, text="Email").grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=2, column=1)

Label(root, text="Grade").grid(row=3, column=0)
e4 = Entry(root)
e4.grid(row=3, column=1)

Label(root, text="Address").grid(row=4, column=0)
e5 = Entry(root)
e5.grid(row=4, column=1)

Button(root, text="Add Record to Database", width=25, command=add).grid(row=6, column=1)
Button(root, text="Query the Database", width=25, command=getdetail).grid(row=7, column=1)
Button(root, text="Update", width=25, command=second).grid(row=8, column=1)
Button(root, text="Delete", width=25, command=delete1).grid(row=9, column=1)

e6 = Entry(root)
e6.grid(row=10, column=1)

ll = Label(root)
ll.grid(row=11, column=1)

root.mainloop()
