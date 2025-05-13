class employee:

    salary=0
    bonus=0
    timings="9 to 5"
    def __init__(self,name,age,salary,ID):
        self.name=name  
        self.age=age
        self.salary=salary
        self.ID=ID  
        self.position="salesman"
    def increase_salary(self):
        self.salary=self.salary+1000
        print("New salary is", self.salary)
    def promote(self):
        self.position="manager"
        print("New position is", self.position)
    def ontime(self):
        timings=int(input("What time did you come to work today"))
        if timings<=9:
            print("You are on time")
        else:
            print("late")

employee1=employee("vijay",14,1000,1)
employee1.increase_salary()
employee1.promote()
employee1.ontime()


          


        