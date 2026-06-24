#classes
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def is_passing(self):
        return self.marks>40
    def __str__(self):
        return (f"Name:{self.name}, Age:{self.age}, Marks:{self.marks}")
s1=Student('John',10,90)
print(s1.name,s1.marks)
s2=Student('Alice',12,35)
print(s2.name,s2.marks)
print(s1.is_passing())
print(s2.is_passing())
print(s1)
print(s2)

class Collegestudent(Student):
    def __init__(self,name,age,marks,college,year):
        super().__init__(name,age,marks)
        self.college=college
        self.year=year
    def __str__(self):
        return (f"Name:{self.name}, Age:{self.age}, Marks:{self.marks}, College:{self.college}, Year:{self.year}")

c1=Collegestudent('Bob',20,85,'XYZ College',2)
print(c1.is_passing())
print(c1)

