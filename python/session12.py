#------------------------Inheritance and polymorphism-------------------
#Inheritance means when child take by default things from parents. 
# in coding lets say one class wants create functions which are already therein different class.
#now one method id second class can create those functions again which will be time taking and make code shorter. second metjod is 
#second lass can take functions from first class this will save time and and make code shorter.

# so in short when one class wants to atke functions from other class then we first need to establish a relationship
#between two classes by teling that one class who gives is parent class and the one who taks is child class.
#then second lass can take things. eg : in real life too if one persons wants to inherit something they need to have relationship between them
#similary here in coding also we establish the parent and child relationship.

#Benefits of inheritance;
#1.reusing the same function fro  other class
#2. saves time.
#3. makes cod shorter.

#First class
class student:
    def __init__(self, name, age, marks):
        #storing variabls tehy strat from self
        self.name=name
        self.age=age
        self.marks=marks
    def marksss(self):
        print("Hello this is good")
    def hello(self):
        print("this is not so good")

#second class, connect with first class by eiting its name in ().this will tell program that baove class is parent class and this is child class.
#nowto take functions variables from first class use super keyword.
#syntax : super().__init__()
#super().functioname()
class teacher(student): # this si how we connect two classes by eriting first classname
    def __init__(self, name, age, marks, roll_no):
        self.roll_no=roll_no
        #call init function from previous class
        super().__init__(name, age, marks)
    def mm(self):
        #call functiom from first class
        super().marksss()
    def hello(self):
        print("this is not so good")
        super().hello()

#object is always created of child class because child has functiond from parent class and has its owsn fubctions as well.
teacher1=teacher("hi", 12, 199, 112)
teacher1.mm()

#---------------------------------------Polymorphsim--------------------
#when two functions have same name in two different classes. those two classews are parent and child classes. one functions in parent and one in child class with same name.
