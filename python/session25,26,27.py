# SQLite library is a database library used to store information coming from the user.
# That means any software, website that we create in coding needs a database where we can store the data.
# Although there are many databases such as MySQL and Oracle, we are using SQLite database because:
# - It is inbuilt in Python already in the form of a library, meaning we don't have to install it separately and connect it.
# - If we have to use any different database, we have to install it separately and ensure that it gets connected properly.

# About SQLite
# - SQLite library is used to store data.
# - It is a very small library, meaning we can't store tons of data in it.
# - It is used to develop small software applications as it is a small library.
# - We do not have to worry about the connection.

# Steps to install and connect SQLite
# 1. Use the pip install sqlite3 command in CMD.
# 2. Import SQLite in the code.
# 3. Use the .connect function to connect with the database.
# 4. Then use the cursor to create a cursor variable, which can later help us out to execute our queries.
# All databases use one common language called SQL.
# So if we are able to use one database, we can easily use another database as well because all databases use the same language.
# Data in all of the databases is stored in table form.
# 5. That means we first have to create a table.

# Syntax to create a table:
# create table table_name(column_name1 datatype, column_name2 datatype, column_name3 datatype.....)
# Once the table is created, we have to make sure that the data we get from the tkinter textboxes is stored in the table above.

# Syntax to insert data from tkinter:
# insert into table_name(all column names) values(t1.get(), t2.get()......)
# We are getting the values from the textboxes to be inserted into the table.

# 3. Querying or getting the data from the database when needed:
# Syntax for this is select * from table_name where column_name=value.
# The above-mentioned query is used to select the details of a person whose value will be mentioned.
# After selecting the details, we have to use the fetchall function to fetch the details.

# 4. Updating details:
# Syntax to update:
# update table_name set detail_that_needs_to_be_updated.

# 5. Delete query:
# Syntax to delete the query:
# delete * from table_name where column_name=value.

# ------------ Database coding ----------------
import sqlite3
from tkinter import *

# Connect to the database
db = sqlite3.connect("data1.db")
# database.db is the name of the database.
# If we are giving the name for the first time, then it will create a database, but if we have used this database earlier, then it will get connected to the previous database.
csr = db.cursor()

# Create table query
sql = """
CREATE TABLE IF NOT EXISTS emp(
    staffnumber INT,
    firstname TEXT,
    lastname TEXT,
    gender TEXT,
    dateofjoining VARCHAR(30))
"""
csr.execute(sql)
db.commit()
# Once we write the query in the sql variable, we have to always use the cursor to execute it.
# If we don't use the cursor to execute it, then the query will not work.
# Commit is to save the changes done; it is always used at the end of every query.
# Datatypes of the database are a little different; they are text, int, varchar.
# Varchar is used when we want to use text, numbers, and special characters such as an email.
# (30) means the maximum characters we can have in there.


# --------------- Adding data into the table ---------------------
def add():
    # First, we get the details from the textboxes and then use the insert query inside which we will pass the details.
    a = e1.get()
    b = e2.get()
    c = e3.get()
    d = e4.get()
    e = e5.get()
    sql = """INSERT INTO emp(staffnumber, firstname, lastname, gender, dateofjoining) VALUES (?, ?, ?, ?, ?)"""
    csr.execute(sql, (a, b, c, d, e))
    db.commit()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)


# -------------------------------- Get details from database -------------------------------------------
# This allows searching and getting any detail from the database and displaying it on screen.
# For this, we will create an entry box where the ID will be entered for the search. Then use the select query to select the details from the database.
# Fetch all to fetch the details and store them in a variable. Later, use a for loop to display it on screen.
def getdetail():
    a = e6.get()
    csr.execute("SELECT * FROM emp WHERE staffnumber=?", (a,))
    r = csr.fetchall()
    # In r we have details now. Use a for loop on r to display on the screen using a label.
    rr = ""
    for i in r:
        rr += f"{i[0]}\n{i[1]}\n{i[2]}\n{i[3]}\n{i[4]}"  # \n gives a new line so all the info goes to the next line.
    # Now everything is in rr, so give this to label
    ll.config(text=rr)
    db.commit()


# ---------------------------------- Delete data from database --------------------------------
# First, we enter the staff number in e6 to delete details.
def delete1():
    b = e6.get()
    csr.execute("DELETE FROM emp WHERE staffnumber=?", (b,))
    db.commit()


# -------------------------------------- Update data in database -----------------------------------
# Create a second page with the same labels and entry boxes as the first, but use select and fetchall to insert data in them.
# Whatever we want to update we can do and click on the update button.
# Create two functions: one for the second page and one for the update query.
def edit():
    # Update query to use.
    # We will use the update query in this one.
    a1 = e11.get()
    b1 = e12.get()
    c1 = e13.get()
    d1 = e14.get()
    e1 = e15.get()
    staff_id = e6.get()
    sql = """
    UPDATE emp 
    SET staffnumber=?, firstname=?, lastname=?, gender=?, dateofjoining=? 
    WHERE staffnumber=?
    """
    csr.execute(sql, (a1, b1, c1, d1, e1, staff_id))
    db.commit()


def second():
    a = e6.get()  # Retrieve the staff number from the main screen
    if not a:
        ll.config(text="Please enter a Staff Number to update.")
        return

    # Fetch the data for the given staff number
    csr.execute("SELECT * FROM emp WHERE staffnumber=?", (a,))
    r = csr.fetchone()  # Use fetchone since we expect only one record

    if not r:
        ll.config(text="No record found with this Staff Number.")
        return

    # Open a new screen for editing
    screen2 = Toplevel(root)
    screen2.geometry("400x400")
    screen2.title("Edit Record")

    global e11, e12, e13, e14, e15  # Entry fields for the second screen

    # Create and place labels and entry fields
    Label(screen2, text="Staff Number").grid(row=0, column=0)
    e11 = Entry(screen2)
    e11.grid(row=0, column=1)
    e11.insert(0, r[0])  # Populate with current data
    e11.config(state='readonly')  # Make it readonly since staffnumber is the primary key

    Label(screen2, text="First Name").grid(row=1, column=0)
    e12 = Entry(screen2)
    e12.grid(row=1, column=1)
    e12.insert(0, r[1])

    Label(screen2, text="Last Name").grid(row=2, column=0)
    e13 = Entry(screen2)
    e13.grid(row=2, column=1)
    e13.insert(0, r[2])

    Label(screen2, text="Gender").grid(row=3, column=0)
    e14 = Entry(screen2)
    e14.grid(row=3, column=1)
    e14.insert(0, r[3])

    Label(screen2, text="Date of Joining").grid(row=4, column=0)
    e15 = Entry(screen2)
    e15.grid(row=4, column=1)
    e15.insert(0, r[4])

    # Button to save the updated data
    Button(screen2, text="Update", command=edit).grid(row=5, column=1)


# -------------------------------------- Interface -----------------------------------------------------
root = Tk()
root.geometry("600x600")
root.title("Employee Database")

global e1, e2, e3, e4, e5, e6, ll

Label(root, text="Staff Number").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="First Name").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)

Label(root, text="Last Name").grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=2, column=1)

Label(root, text="Gender").grid(row=3, column=0)
e4 = Entry(root)
e4.grid(row=3, column=1)

Label(root, text="Date of Joining").grid(row=4, column=0)
e5 = Entry(root)
e5.grid(row=4, column=1)

Button(root, text="Add Record to Database", width=25, height=1, command=add).grid(row=6, column=1)
Button(root, text="Query the Database", width=25, height=1, command=getdetail).grid(row=7, column=1)
Button(root, text="Update", width=25, height=1, command=second).grid(row=8, column=1)
Button(root, text="Delete", width=25, height=1, command=delete1).grid(row=9, column=1)

e6 = Entry(root)
e6.grid(row=10, column=1)

ll = Label(root)
ll.grid(row=10, column=2)

root.mainloop()
