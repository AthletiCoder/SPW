class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name:",self.name, " Salary:", self.salary)

class Manager(Employee):
    pass

emp1 = Employee("Ravi", 50000)
emp1.displayEmployee()

mngr1 = Manager('Mahesh', 20000)
mngr1.displayEmployee()