

class School:
        def __init__(self, name):
                self.name = name
        
        def work(self):
                pass


class Student(School): #Here, Teacher class inherits from the School class
        def work(self):
                return "Learn and be attentive in the classroom"
        

class Teacher(School): #Here, Studen class also inherits the School class
        def work(self):
                return "Teach the students in the class" 


student = Student("Harun")
teacher = Teacher("Phitron")

print(student.name)
print(student.work())
print(teacher.name)
print(teacher.work())
