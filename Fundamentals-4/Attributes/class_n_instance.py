class Student:
    college_name = "ABC Classes" #class

    def __init__(self, name, gpa): #instance
        self.name = name
        self.gpa = gpa

stu1 = Student("John", 3.5)

print(stu1.name)
print(Student.college_name)

        