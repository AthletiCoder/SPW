class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name:",self.name, " Salary:", self.salary)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayPerson(self):
        print("Name:",self.name, " Age:", self.age)

class Manager(Person, Employee):
    def __init__(self, name, salary, age):
        Employee.__init__(self, name, salary)
        Person.__init__(self, name, age)

emp1 = Employee("Ravi", 50000)
emp1.displayEmployee()
person1 = Person("Kailash", 20)
person1.displayPerson()
mngr1 = Manager("Mahesh", 100000, 28)
mngr1.displayEmployee()
mngr1.displayPerson()