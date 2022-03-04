class Student:
    def __init__(self,name,year,email,address):
        self.name=name;
        self.year = year;
        self.email =email;
        self.address = address;
    
    def showInfo(self):
        print("**** Student Information ****")
        print(" Student name : " + self.name+
            "\n Year : " + self.year + 
            "\n Email : " + self.email + 
            "\n Address : " + self.address +
            "\n");
    

students = list((
    Student("Aung Aung","2nd year","aungaunng@gmail.com","Yangon"),
    Student("Maung Maung","3rd year","maungmaung@gmail.com","Mdy"),
    Student("Thida","1st year","thida@gmail.com","Mdy"),)
);

for student in students:
    student.showInfo();