class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name:",self.name, " Salary:", self.salary)

class Manager(Employee):
    team = 0
    def __init__(self, name, salary, employeeList):
        self.team = employeeList
        super().__init__(name, salary)

    def displayEmployee(self):
        print(self.team[0])
        super().displayEmployee()

emp1 = Employee("Ravi", 20000)
emp1.displayEmployee()
mngr1 = Manager('Mahesh', 50000, [emp1])
mngr1.displayEmployee()