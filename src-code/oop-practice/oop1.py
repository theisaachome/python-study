# create class


class SoftwareEngineer:

    # class Attributes
    alias = "Keybraod Magician";
    
    # call this method on every new instance created 
    #  it is  use to instanciate 
    def __init__(self,name,age,level,salary):
        #  instance attributed 
        #  instance fields
        self.name = name;
        self.age = age;
        self.level = level;
        self.salary = salary;
        


# create instance

se1 = SoftwareEngineer("Max",20,"junior",5000);
se2 = SoftwareEngineer("Lisa",21,"Senior",7000);
print(se1.name,se1.age);
# access class attribute
print(se1.alias);
print(SoftwareEngineer.alias);


# Recap

# Create new class (blueprint)
#  instance or object from class
#  object attribute
#  class attribute
#  accessing the attribute via object and class