# __init__ method in python classes

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

stu1 = Student("Rahul", 9.0)
stu2 = Student("Ravi", 8.4)
stu3 = Student("Shradha", 9.2)

print(stu1.cgpa)
print(stu2.name)
print(stu3.name)