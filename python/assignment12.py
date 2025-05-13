class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        
    
    def average_marks(self):
        mark=int(input("what mark did you get?"))
        mar=int(input("what other mark did you get?"))
        total=(mark+mar)/2
        print(total)
        
    

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        
        super().__init__(name, school)
        self.salary = salary
    def hello(self):
        super().average_marks()
student1=WorkingStudent("vijay", "notts",5000)
student1.hello()
    
   



