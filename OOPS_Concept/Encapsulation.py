class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.__marks=marks
    
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self, marks):
        self.__marks = marks
    @marks.deleter
    def marks(self):
        del self.__marks

student1=Student(1,"John",90)
print(student1.marks)
student1.marks = 80
# Output: 1 John 90
print(student1.marks)
# Output: 1 John 80
del student1.marks
try:
    print(student1.marks)
except AttributeError as e:
    print(e)
# Output: AttributeError: 'Student' object has no attribute '_Student__marks'
