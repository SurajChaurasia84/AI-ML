# types of constructors in python classes

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Rahul", 9.0)
stu2 = Student("Ravi", 8.4)
stu3 = Student("Shradha", 9.2)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")