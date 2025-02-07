#--------------------------------for loop---------------------------------------
#For loop is used to get the data from data structure(list, tuple, set, dictonaries) one by one quickly. Ig we are creating list, tuple aor naytjing we  are creating it
#so that w ecan use data from it. getting data one by one from it is very time taking. This is the reason we
#use for loop to get all data from it and then we can use that  data Because it is a loop so it will not take much time to get it. 
#Loop means to reoeat anythung again n again. For loop repeatedly does one thing that getting data one by one from list. This is the readson it is called as for loop.
#It goes inside and gets first data,m tehn again go inside gets second data and so on.... in rounds it keeps on getting data. But this happens reallyu fast.
#snytax for for loop : for variablename in (name of list, tuple etc):
#Here variables goes inside list and get all data one by obne 

#create a list and use for loop to get all numbers and print data on screen
import random

list=[1, 2, 3, 4,5, 6, 7, 8, 9, 10]

for i in list :
    #i variable goes inside list and gets one by one all data.  In first round it get1 , second round it gets 2 and so on. 
    print(i)

#use for loop and get all data and check out of whole list which oen is even or which osn is odd

for ii in list:
    #ii variabkes will get data from list. everything we apply on variable craeted as variable is the one who brings everything,
    if ii%2==0:
        print(ii, "is even")
    else:
        print(ii, "is odd")

#create a list of 5 fruits.  apply for loop and to get all data and print it on screen.
list1=["apple", "pear", "grape", "orange", "strawberry"]
for d in list1:
    print(d)

#use for loop to add all numbers in list and print answer on screen
total=0
for i in list:
    total=total+i
print(total)

#----------------------------------break and contine--------------------------------------------
#break completely stops and iyt will not go further. continue stops at one point but again loop restarts  
#use loop on list1, print all fruits except
#to skip one or more data from list we can use continue. it stop at one data and should not go further use break.
for i1 in list1:
    if i1=="pear":
        continue # this means loop stops at pear and again restarts after that. it skips pear.
    #print is always done after if then continue
    print(i1)

for i1 in list1:
    if i1=="orange": # stops at orange further after orange will also not come
        break
    print(i1)

#range() function in for loop : so when we know we have a list of only numbers wity proper gap  between numbers like 2 or anything. not random numbers. then do't create list
#we directly use for loop on range() this saves time

#create a list of numbers first 10 numbers which are divsible by 3
#use for loop on it and print all numbers
#1 method : we craete a list and use for loop on it

list=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for i in list:
    print(i)

#2 Method : use for loop directly on range()

for i in range(3, 30,3):
 # range(startpoint, endpoint, size)
    print(i) # i will go inside range() and will bring all numbers from it

#--------------------------------------Assignment------------------------------------------------------
#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included). use for loop in range()
#2. Write a Python program to guess a number between 1 and 9.
#Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
#while loop is used
#3. Write a Python program to count the number of even and odd numbers in a series of numbers. for loop is used then insude that if then else
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#4. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
#Expected Output : 0 1 2 4 5. create a list of umbers use for loop use continue 

for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number)


randomnum = random.randint(1,9)
guess = int(input("Guess a number between 1 and 9"))
while guess != randomnum:
    guess = int(input("Guess a number between 1 and 9"))
    continue
else:
    print("congratulations that is the right number")


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
even_count=0
odd_count=1
for num in numbers:
    if num % 2 == 0:
        even_count+1
    elif num % 2 == 1:
        odd_count+1


for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)

