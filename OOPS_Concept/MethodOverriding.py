class Emplpoyee:
    def __init__(self):
        self.salary=10000
    def get_salary(self):
        print("New Employee Salary is:",self.salary)

class Manager(Emplpoyee):
    def __init__(self):
        super().__init__()
        self.salary=200000
    def get_salary(self):
        print("Manager Salary is:",self.salary)
class Developer(Emplpoyee):
    def __init__(self):
        super().__init__()
        self.salary=3000
    def get_salary(self):
        print("Developer Salary is:",self.salary)

m=Manager()
m.get_salary()
d=Developer()
d.get_salary()
e=Emplpoyee()
e.get_salary()