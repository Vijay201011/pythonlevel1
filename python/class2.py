#numbers we have two types of numbers, integers and decimals.
#Decimals are also called floats.
#Different datatype functions are 
#int(), float(), str(), bool(), 
#These are the functions used to convert from one datatype to another
num=3
num=str(num)
print(num)
#type of function is used to find the type of the function
print(type(num))
num=int(num)
print(num)
print(type(num))
#strings 
#this is a datatype which is written in quotation marks
#---------------------------------Concatination or joining of two text togther---------------
#plus sign is used to join 2 variables or text  together but it should be the same datatype


print("the number is : "+ str(num)) # here we attach text and number together by converting the number into text.

#+,-, /(divides two numbers and gives answrr as quotient), *, %(modulus) didvies two numbers and gives answer as remainder,  //
#will also divide tow numbers but its ignores the value after decimal.

c=8
d=8
print(c%d)#answer is 0
print(c/d) # answer is 1

#-----------------------Concatentaion with , --------------------
#, can also be used to join two text, two variables or one text with one variable. here different data types can be attach
#together unlike + where same data type is needed
#sam answer in bothe cases
print("The remiander of two numbers is "+ str(c%d))
print("The remiander of two numbers is ", (c%d))

maths=70
english=80
science=40
languages=60
history=100
geography=80
religion=90
print(maths+english+science+languages+history+geography+religion)
score=520
print(score/7)
average=(score/7)
print(average)