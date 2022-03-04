class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def show(self):
        return f"I am {self.name} and I am {self.age} year old.";

emp = Employee("Aung Aung",20);
print(emp.show());