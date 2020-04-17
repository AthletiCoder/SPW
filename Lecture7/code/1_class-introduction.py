class Employee:
    __empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.__empCount += 1

    def __displayCount(self):
        print("Employee No.:", Employee.__empCount)

    def displayEmployee(self):
        print("Name:",self.name, " Salary:", self.salary)
        self.__displayCount()

emp1 = Employee("Ravi", 50000)
emp1.displayEmployee()
emp2 = Employee("Mahesh", 20000)
print(emp2._Employee__empCount)