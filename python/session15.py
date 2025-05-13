#--------------------------------------------Libraries---------------------------------------------------------------------
#os and shutil libraries.Libraries are the python files where we have functions stored in them. os and shutil have functions related to
#to operating system means all functions are related to system.
#basics operations like create folder, open file, make chnages to file, copy from one file to another, move from one file to another etc...
#rename the file, deleting teh file..
#but python gives us to perform all these file related function through functions of library withe coding.
#parctical use : let say if you want to create one software and want to add create file, copy, paste feature in that then we can use this.
import os 
import shutil


#to open a file and read
"""file="demo.txt"
f=open(file, "r") # open will open the file and r will read and get teh details 
print(f.read())

#how to make changes to the file
f1=open(file, "a") # open teh file and w will write the things inside the file, w will replace all pevious data and a will add changes to that data.
print(f1.write("Hello this is Vijay"))"""

#delete
#os.remove("demo.txt")

#copy() and paste()
#shutil.copy("demoo.txt", "demmmo.txt")#source file, detination file

#shutil.move("demoo.txt", "demmmmo.txt")

#-------------------------------------------------Exceptional Handling-----------------------------------------
#Exceptionalding handling means handling exceptional errors which occur. These errors are not syntax error or error in code they are usually occuring on user side due to soem wrong input gven by user or may be somethimg else happened
#on his side the error comes. To hamdle these errors we called as exceptional handling. These are called as exceptional errors because they sometimes occue and sometimes notn they might come and migght not comes because if user has given input perfectly and nothing has hapoened on his side then no error will come
#but if something has happened then might come. 

#We cannot stop these errors from coming as these happen on user side
#Errors : wrong input, zero didvision error, memory issue, internet issue, try to get data from array which is not there, file not found error etc e


# Instead of displayong red error message we can display simple message using try and except thsi is how we handly exceptional error.

#First put the block of code in try which we think might create an error, if nothing happens code will be executed, otherwose if error comes it will go to except where mesage will be there.
#without try and except
"""a=3
b=0
print(a/b)"""

#with try and except
try:
    a=3
    b=0
    print(a/b)

except:
    print("please try again with not 0")



