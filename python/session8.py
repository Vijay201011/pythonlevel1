

while True:
    number1=int(input("Enter the first number"))
    number2=int(input("Enter the second number"))
    sign=input("Enter the sign")
#
    if sign=="+":
      print(number1+number2)

    elif sign=="-":
      print(number1-number2)
    
    elif sign=="*":
      print(number1*number2)

    elif sign=="/":
      print(number1/number2)
    elif sign=="over":
       print("Thank you so much for using calculator")
       break
    
    


#-----------------------------------------There are two keywords in while loop---------------------------
#1. break : It is used to break or stop the loop. This is for infinite loop where we don't tell in the beginning that when we need to stop the loop.
#then in that we give one if condition and tell when loop will be stopped. there we use break.

#example 1 : we use True whenever we want to give infinite loop
#no starting point no ending point 

while True:
    print("Hello")#It will keep on printing hello infinite number of times.
    #but if we use if then  and tell this is when we want to stop the loop it will stop we have to use break
    a=input("Enter the name")
    if a=="Sakshi":
        break # this infinite loop stops only when Sakshi input is given otherwise it will keep on printing
    else:
        continue # this means it will keep on asking the user name uness sakshi is entered
   

#2. continue : it stops the loop at condition bt again restarts
#Example : print all numbers till 6 except 3 and 6

a=0
while a<6:
    a=a+1
    
    if a==3 or a==6:
        continue # This means the loop stops at a==3 but restarts again at 4 then again stops at 6.
    print(a)













