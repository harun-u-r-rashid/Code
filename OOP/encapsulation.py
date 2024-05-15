
# This is public encapsulation
class Student:

        roll = 39829832 
        
        def __init__(self,roll):
                self.roll = roll

        def display(self):
                return(self.roll)
        

student = Student(2006015)
print(student.display())

student.roll = 2006016 #Here, trying to change the roll, it's possible because of public encapsulation
print(student.display())



# Private encapsulationo

class Teacher:
        _teacherId = 0
        def __init__(self, teacherID):
                self._teacherId = teacherID

        def display(self):
                return (self._teacherId)
        
teacher = Teacher(50)
print(teacher.display())

teacher._teacherId = 60
print(teacher.display())


class Student:
   def __init__(self, roll):
       self.roll = roll

