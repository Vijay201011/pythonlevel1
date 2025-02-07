#-------------------------------Operators----------------------------------
#1. Arthmetic Operator: +, -, *, /, %(modulus) divides two numbers and gives remainder.
#2. Logical operator: or(either), and(both), not. These three are mianly used whne we given condition
#3. Comparison operator:<, >, <=, >=, ==(equal), =(only used to give variable value).
#4. Assignment operator : +=, -=, *=, /=. this means if we want to give some value to variable by adding, subtracting, multiplying, dividing number to it.

a=4
#now add 3 to a
a+=3
#3 is added to 4 so a is 7
print(a)
a*=10
print(a)
a=100
print(a)
#-------------------------------input-------------------------------------
#input() takes answer from user.it ask question from user. so we always use input () in variablke so that we can store that answer somewhere. input always
#takes input from user in text form. so if we are going to do any mathematical thing on input() the convert it into integer.
#int(). use int() before input().
#--------------------------Conditions-----------------------------------
#Conditions means if we do one thing the  something happens else something else hapens.
#syntax :if condition :
#            next part
#        else:
#            next part
#next part has spaceing/indentation. else begins from same point as if

#create a program take input from user. if no is greater than 18 the print its gretarer else print its smaller.

number1=int(input("Enter the number"))
if number1>18:
    print("its greater")
else:
    print("its smaller")

#Note : whenver we have two conditions we use : or or and
#create a program, take input from user. to check if score in between 90 and 100 print good scoree else not good score.
number2=int(input("enter a number"))
if number2>90 and number2<100:
    print("Good grade")
else:
    print("its not good grade")

#---------------------------------Multiple---------------------------
#if condition:
#   part
#elif condition:
#   part
#elif condition:
#   part
#else:
#   part

#elif is used to connect multiple conditions

#createa a program take input from user his favourite subject. if subject is equak to math the print great elif subject is equal to science print its good else print its bad.

subject=input("Enter your favourite subject")

if subject=="math":
    print("great")
elif subject=="science":
    print("its good")
else:
    print("its bad")


#Note : = sign means assuignning right side to variable. == sign means equal in condition we always use ==
    
team=input("Enter the code")

if team=="1999":
    print("There is a traitor in team B. Find him without letting the team know because it could be anyone")
elif team=='2422':
    print("The president is in danger. Keep a watch over him secretly")
elif team=='1832':
    print("There is a traitor in team A. He is off guard for now because of wrong information. This is the best chance to catch him")
elif team=='3943':
    print("Assasinate the minister.")
else: 
    print("Incorrect code")





















































































































