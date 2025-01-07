class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary)
    

Hunain = Employee("Hunain", "999999999999")
print(Hunain.name)
print(Hunain.salary)
Hunain.getSalary()