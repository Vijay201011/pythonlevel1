#----------------------------Data Structure-----------------------
#We can store multiple data in variable by converting to list, tuple, set, dictonaries.

#-----------------------List-----------------------------
#List helps to store lot of data. we ue []. List are mutable that means we can cange the list anytime 
#by adding or deleting the data. w ecan put any data like int, strings, float etc.
#We can store as much as data we can.
#syntax : listname=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

list1=[1, 2, 3, 4, 10, 16]
#get data at 2 index value
print(list1[2])

#----------------------------Index value--------------------------------
#Index value means position number given to every alphabets.Tis begins from zero. 
#thta means who seo ever comes first has 0 index value followed by 1, 2, 3, 4, 5, 6, 7, 8, 10
#----------------------------------Why index value-------------------------
#the index value are given so that to access the data.
#if we want to access data of spefic value then we always use index value.

#--------------------------------List Functions--------------------------------
#1. Sort - This is used to sort the list alphabetically and in number order
list1=[4, 3, 2, 1, 5]
list1.sort()
print(list1)
#2. Reverse - it reverses the list
list1=[1, 2, 3, 4, 5]
list1.reverse()
print(list1)
#3. Append and Pop - Append is used to add items to the list and pop is used to delete it
list1=[1, 2, 3, 4]
list1.append(5)

list1.pop()
print(list1)
#it deletes the data from the right side
#4. Insert - adding the data at a specific position
list1.insert(2,"3")
print(list1)
#5 Remove - remove is used to remove data from any specific position
list1.remove(3)
print(list1)
#6 Count - count the number of times the specific element appears in the list
l=list1.count(1)
print(l)
#7 Index - this function returns the index of the given data
print(list1.index(1))

#


#------------------------------------------------------------------------
#
print("hi", 3)
#8. min, max and sum() if lis has only numbers
#--------------------------Concatenation and merging of data.-------------------

list2=[1, 2, 3, 4,5, 6]
list4=[1, 2, 3, 4,5, 6]
list5=[11, 12,1, 3, 14,15, 16]
resultlist=list4+list5
print(resultlist)
print(max(list2))
print(min(list2))
print(sum(list2))


