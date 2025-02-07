#----------------------Strings------------------------
#Strings ae those alphabets which are written in " ". it can be words, numbers, special chracter it can be aanything.
#Strings have index value which means position numbers is given to each and every alphabet starts from 0,.
#the alpabts which comes 1st has 0 index value which means 0 position no, followed by 1, 2,  and so on..........

name="vijay123"
print(name)
#v is at 0 index value, i at 1, j at 2 and so on....automatic position are gven to them.

#----------------------To get certain alpahbets or data-------------
# index value of data we need to write
# to get any data we write : variablename[index value]
print(name[1])

#--------------------------Slicing-------------------------------
#This means deleting the items or data from left side or right side.
# to delete from left size write how many numbers we need to delete from left before : eg 
# 3:

print(name[3:])

#to delete from right side :  write the numbers of items we need to keep it : eg :
# :4 means 4 items will keep from left side rest will be deleted.

print(name[:4])

#-----------------------------String functions--------------------------
#Reverse
print(name[::-1])

#1. capitalize() - this makes the first letter of the sentence capital
print(name.capitalize())
#2. find() - searches for a particular word or alphabet
a=name.find("a")
print(a)#it will print the position number of a.
#3. islower() and isupper() chcks all letters are uppercase or lowercase
a=name.islower()
print(a) #because checks so output isinntrue or false
a=name.islower()
print(a)

#4. lower() and upper() : converts into lowercase and uppercase()
print(name.lower())
print(name.upper())

#5. replace() ; It replaces the word given in order word or alphabet
print(name.replace("i", "p"))

#6. 
#sorted - this is used to sort the list alphabetically or numberwise. 
a="sakshi"
print(sorted(a))



namee="Vijay"
sport="Football"
age="14"
weight="55"

print("my name is Vijay and backwards it is")
print(namee[::-1])
print("my favourite sport is football and the first 4 letters are ")
print(sport[:4])
print("I am 14 years old and weigh 55kg, and the numbers put together is")
print(age+weight)