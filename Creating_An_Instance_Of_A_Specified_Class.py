#Creating an Instance of a Specified Class

class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name

student=Student(123,'Raj','XII')

print(student.__dict__)
        
