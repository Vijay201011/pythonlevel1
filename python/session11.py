#oops - object oriented programming
#it is a programming based on objects 
#these objects are similar to the real life objects which have some properties and functionalities
#when we create an object in coding, these objects also have some properties 
# that means the characteristic and the way they look and the functionality
# eg we are creating a game and we need to create players and enemies, they can be created with the help of objects
# the benefit of creating with the help of objects in that those players and enemies will have properties and functionalities of the object
#We have to give the functionalities later to the enemies and players so if it comes along with it, its a good thing



#class
#class is a blueprint or design of the object like in real life
#before creating any object, the designing is done where decide what functionality and characteristics we want to give
#similarly in coding as well, before creating the object, the designing is done and designing here is called as class
#inside which we decide the properties (variables) and  functionalities 
# first class is created and then object is created
#we can also say class is where we group all of the variables and functions together.
# class is bigger than functions
# eg 
# a school - which has lots of classes inside it and every class has lots of students
#school > lot of classes > lots of students
# similarly in coding, 
#one class > lot of functions > every function has a code
#syntax to create a class
#benefits of having a class 
#1. it helps to group all of the variables and functions together
#2. we are able to re use the same function from the class by calling it for different objects
#3. code becomes very organised
#class class name:
#syntax to create an object
#object name = class name()
#create one student class with properties, name, age, class.
#create a function to calculate the marks of student 
#create one more function to calculate the time for the student
class student:
    #in class, we put all of the variables in an inbuilt function called as init function
    # we use self keyword before creating a variable
    # the reason of making a self keyword is so that we can show that it is not a normal variable
    #it is a variable used to define properties
    def __init__(self, name,age,class1):
        self.name=name  
        self.age = age
        self.class1=class1
#actual values are given when object is created because if we give the values here in the class itself,
#all of the variables will have the same properties
#every time we create an object it changes the value
    def marks(self):
        m=int(input("enter a number"))
        b=int(input("enter another number"))
        total = m+b
        print(total)
    def time(self):
        y=int(input("what time did you come to school today"))
        if y<9:
            print("on time")
        else:
            print("not on time")
student1 = student("vijay",14,9)
student1.marks()
student1.time()
student2 = student("gerdg",11,7)
student2.marks()
student2.time()
#attributes means variables we create in the init function