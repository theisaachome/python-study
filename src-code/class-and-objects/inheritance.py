class Person:
    def __init__(self,firstName,lastName,address,email) -> None:
        self.firstname=firstName
        self.lastname=lastName
        self.address=address
        self.email=email
    
    def showInfo(self):
        print("Person Information")
        print(f"First Name : {self.firstname}\nLast Name : {self.lastname}\nAddress : {self.address}\nEmail : {self.email}");
    

class Employee(Person):
    pass

manager = Employee(firstName="Aung Aung",lastName="Oo",address="Yangon",email="aungaungoo@gmail.com");

manager.showInfo();

# Teacher class 
class Teacher(Person):
    def __init__(self, firstName, lastName, address, email,subject):
        Person.__init__(firstName, lastName, address, email)
        self.subject=subject

#  Student class

class Student (Person):
    def __init__(self, firstName, lastName, address, email,studentId,year):
        super().__init__(firstName, lastName, address, email);
        self.studentId = studentId
        self.year = year
    
    def takeExame(self):
        print("Student is Taking Exam..")