#-----------------------------Loops-----------------------------------
#While Loop is used to repeat the code over and over again. 
# 4 important things which we need in while loop :
#1. Starting point : when the loop begins - create variable and store start value in that.
#2. End point : whne the loop will end - Here we say that if our variable is less then equak to some value  the our code will repeat once the condition becomes false
#eg : a<=20 means till the time a is les tahn equal to 20 the loop goes on whne it becomes greater tahn 20 then loop stops.
#3. code need to repeat again n again.
#4. increament or decreament (counting). we increase the variable so that it recahes to end point.

#syntax for while loop : 
#give value in variable
#while end point:
#code to repeat
#increament

#print all numbers from 1 to 31

#start point
a=1

#end point
while a<=30:
    #code to repeat
    print(a)
    #increament
    a+=1


#print all numbers divisible by 11 till 120

b=0
while b<=120:
    print(b)
    b+=11



#print hello 10 times on screen start from 1
c=1
while c<=10:
    print("hello")
    c=c+1

#print all numbers which are divisible by 3 till 20
d=3
while d<=20:
    print(d)
    d+=3

#print factorial of 10. 

#Fcatorial means we multiple the given number with previousnumber and we do it till 1 and after multipying  we get an answer.
#while loop can be used where it multiplyes with pevious number

#start point 
e=1
f=1
while e<=10:
    f=f*e #f=1*1=1
    e=e+1 #f=1*2=2, f=2*3=6, f=6*4=24....
print(f)


#we can also use if the in while loop
#print number which is divisible by both 3 and 5 till 30

s=0
while s<=30:
    if s%3==0 and s%5==0:
        print(s)
    s=s+1

#------------------------Assignment----------------------
#create while loop, strat point 100, ending point 200. print all numbers which are divisible by 3
#create w hile loop,print numbers which are divisible by 3 and 9 till 300.

p=100
while p<=200:
    if p%3==0:
        print(p)
    p=p+1


f=0
while f<=300:
    if f%3==0 and f%9==0:
        print(f)
    f=f+1
