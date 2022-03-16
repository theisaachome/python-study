# function in class


# why use function in class


class SoftwareEngineer:

    def __init__(self,name,age,level,salary):
            self.name = name;
            self.age = age;
            self.level = level;
            self.salary = salary;
    
    def code(self):
        print(f"{self.name} is writing code .....");
    def code_in_language(self,language):
        print(f"{self.name} is writing code in {language}");

    def information(self):
        information = f"Name : {self.name} \nAge : {self.age}\nLevel : {self.level}\nSalary{self.salary}";
        return information;

    # toString() method at java
    def __str__(self) -> str:
        information = f"Name : {self.name} \nAge : {self.age}\nLevel : {self.level}\nSalary{self.salary}";
        return information;

    # over write eq method
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.age==other.age;

    # without self parameter we can not use on instance 
    # we can only use in Class level method
    # to identify this method is from class we use decorator
    @staticmethod
    def entry_salary(age):
        if age < 25 :
            return 5000;
        if age < 30 :
            return 7000;
        return 9000;
    
        

# create object of software engineer

se1 = SoftwareEngineer("Max",20,"junior",5000);
se2 = SoftwareEngineer("Lisa",21,"Senior",7000);
se3 = SoftwareEngineer("Lisa",21,"Senior",7000);

# print(se1.information)
print(se1);
se1.code_in_language("Python");

# comparing memory adddress
print(se2==se3);
#  since the method belong to instance and it will get error 
#  bcos it demands 2 arguemnt which is exmaple(self,age)

# se1.entry_salary(24);
# to the entry_salary() from class level method
print(SoftwareEngineer.entry_salary(28));