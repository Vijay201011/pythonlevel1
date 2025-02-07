#-----------------------------Functionsw-----------------------
#There vare two types o9f functions:
#1. Inbuilt Function: 
#These functions are already there in python we need to call them.eg : input, print, randint, sort, reverse. Functions have one word and () are there.
#Also thse functions do some work for us. We do not have to create them.

#2. User defined functions: 
#These functions are created by us. Functions are also called as methods.

#Reason for creati8ng our own function:

#1. if we look for a function but that type of function is not there in python then we create our own function eg :
# if we ae looking for a cloh which is not there in market we create our own cloth. thi8s is like creating our own function when we dont get the one we are looking for.

#2. Functions is like a group where we store all the code together. when we create our own function we give name to it andbstore block of lines of code.

#3. Let say there is a code which we need to use it 3-4 times. First option is copy, paste. but this is not good idea because
# this will make our code big. Second option west9ore the code somewhere and gve one name to it. and whnevere we want to use it we wil call he function.
#this makes the code shorter. this is reusing the same code again by writing he function name not by copy ad paste.

#syntax to createtheown function:def functioname():
#insidestore wyhatever code we need to store

#syntax to call the function:functioname()
#ceate for loop on list and print answerbon screen. this coe needbto use it 3times
#METHOD 1 : WE WILL COPY PASTE 3 TIMES
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list:
    print(i)

#Nine lines of code it became

#Method 2: create function and store code in that 
def func():
    list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in list:
      print(i)

#call function whnfvere we need to use it
func()
func()
func()

#Example : create a function with the name of even. In that take input from user. check if ts even print its even else print it odd.


def even():
    num=int(input("enter a number"))
    if num % 2 == 0:
        print("it is even")
    else:
        print("it is odd")

#unless we do not call the functio it will not work
even()




