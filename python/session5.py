#------------------Tuple---------------------------
#Tuple can store lot of data like list. It also has index value like list means every data is given a position number  starts from zero, one and so n.....
#Tuple is immutable that means we cannot add or delete data from tuple. but in list we ca
# Use tuple only when we do not wantto add or delete from tuple.() is used.as mcuh as data we can store. unlimited.
#Example :
tp=(1, 2, 3, 4, 4, 5,6, "Hello", "Hi")
print(tp)

#Index value is used to get data, ad, delete data etc.
#get no 6 from tuple
print(tp[6])
#it does not have apopend(), pop() functions.

#---------------------------Functions of tuple-------------------
#min(), max(), sum()
tp=(23, 20, 100)
print(max(tp))
print(min(tp))
print(sum(tp))

#-------------------------Set--------------------------------
#Set also stores lot of data like list n tuple. Here we can add or delete anytime. But data will be stored randomly.
#No fixed position or index value is tehre. {} is used.

set={1,2, 3,4,5, 6,7,8, 9, 10}
print(set)


#----------------------Dictonary---------------------------------
#Dictonary alos means where we can store lot of data all together like list, tuple, set.
#Here we store values but we also store the meaning of the data. This meaning can also be calledb as variable.
#syntax for creating dictonary:
#dict={
#"key1": value,
#key2:value
#}

#meaning is called as key. Stores va;ue and meaning(key)

dict={
    "name":"Sakshi",
    "Age":100,
    "class":20


}

print(dict)
#----------------------------No index valueit only has, to get data from dictonaryt we use keyname-----------------
#get sakshi data from dictonary
print(dict["name"])

#get 20 data fro dictonary
print(dict['name'])

#to get all index value
print(dict['Age'])
print(dict['Age'])

#allvalues(): to get all data.
#2. keys - to get all keys

print(dict.values())
print(dict.keys())


#Example:

a = ("1", "2", "3", {"name": 20, "age": [1, 2, 3, 10, 14]})
#print 14
#in these cases count the no of brackets and accordinly to that give give index value and key.
print(a[3]["age"][4])

word="hello"

print(word[::-1])

print(word[4])
print(word[4:])
list3=[1,2,[3,4,'hello']]
list3[2][2]='goodbye'
print(list3)


list4=[2,4,3,5,1]
print(sorted(list4))


d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}

print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]["nest_key"][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])



