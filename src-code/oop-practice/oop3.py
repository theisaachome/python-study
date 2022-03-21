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

se1 = SoftwareEnginner("Max",25,6000,"junior full stack");
print(se1.name,se1.age);
se1.work();

designer = Desginer("Lisa",18,7000);
print(designer.name,designer.age,designer.salary);
designer.work();