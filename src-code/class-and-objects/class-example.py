

class MyClass:
    x = 5;

# create object

p1 = MyClass();

print(p1.x);

class Employee:
    def __init__(self,name,age,email) :
        self.name= name;
        self.age = age;
        self.email = email;

    def showInfo(self):
        print("\nName : " + self.name + 
              "\nAge : "  + self.age + 
              "\nEmail : " + self.email);
    

emp = Employee(name="Isaac Home",age="23",email="isaachome@gmail.com");

emp.showInfo();

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)


person = Person("John Person",30);

# person.myfunc();