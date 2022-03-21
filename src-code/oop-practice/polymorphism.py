# inheritance


class Employee:
    def __init__(self,name,age,salary):
        self.name = name;
        self.age = age;
        self.salary = salary;
    # instance methodd is inherited too

    def work(self):
        print(f"{self.name} is working...");

class SoftwareEnginner(Employee):
    # override init method
    def __init__(self, name, age,salary,position):
        super().__init__(name, age,salary);
        self.position=position;

    def debug(self):
        print(f"{self.name} is debugging ....");
    
    def work(self):
        print(f"{self.name} is working as {self.position} position...");

class Desginer (Employee):
    def work(self):
        print(f"{self.name} is designing....")

#  employee list

employeeList = [SoftwareEnginner("Max",25,6000,"junior full stack"),
SoftwareEnginner("Moe Pyie Sone",25,5000,"junior full stack") ,
SoftwareEnginner("John",20,7000,"junior full stack"),
Desginer("Lisa",18,7000)];


def motivate_employee(employees):
    for employee in employees:
        employee.work();


motivate_employee(employeeList);