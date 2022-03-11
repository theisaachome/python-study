# Python Class and Object

## Table of Content

- [Python Class](#python-class)
- [Create Class](#create-class)
- [Create Object](#create-object)
- [The __init__() Function](#the-init-function)
- [Instance Method](#instance-methods)
- [The self Parameter](#the-self-parameter)
- [Python Inheritance](#python-inheritance)
---


## **Python Class** 

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.


## **Create Class**

Create a class named Employee, with a property named name:
```py
class Employee:
    name=" John Doe"
```

## **Create Object**

Create an object named emp, and print the value of name:

```py
emp = Employee();
print(emp.name);
```

---
## **The __init__() Function**

The __init__() function always executed when the class is being initiated.

```py
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
emp = Employee("Aung Aung",20);
```

## Instance Methods

Methods in objects are functions that belong to the object.

```py
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"I am {self.name} and I am {self.age} year old.";

```

---

## **The self Parameter**

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

```py
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # get the properties of age 
    def getAge(self)
        return sefl.age;
```

---

## The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

```py
class Employee:
  pass
```

---
## **Python Inheritance**

**Parent** class is the class being inherited from, also called base class.  

**Child** class is the class that inherits from another class, also called derived class.

### **Example**

Create a class named Person, with firstname and lastname properties, and a printname method:


## Create a Parent Class
```py
class Person:
    def __init__(self,firstName,lastName,address,email) -> None:
        self.firstname=firstName
        self.lastname=lastName
        self.address=address
        self.email=email
    
    def showInfo(self):
        print("Person Information")
        print(f"First Name : {self.firstname}\nLast Name : {self.lastname}\nAddress : {self.address}\nEmail : {self.email}");
    
```
## Create a Child Class
```py
class Employee(Person):
    pass


manager = Employee(firstName="Aung Aung",lastName="Oo",address="Yangon",email="aungaungoo@gmail.com");

manager.showInfo();
```

## Add the __init__() Function

```py
class Teacher(Person):
    def __init__(self, firstName, lastName, address, email,subject):
        super().__init__(firstName, lastName, address, email)
        self.subject=subject
```

---


## Use the super() Function
```py
class Student (Person):
    def __init__(self, firstName, lastName, address, email,studentId,year):
        super().__init__(firstName, lastName, address, email);
        self.studentId = studentId
        self.year = year
```

## Add Properties and Method for a child class


```py
class Student (Person):
    def __init__(self, firstName, lastName, address, email,studentId,year):
        super().__init__(firstName, lastName, address, email);
        self.studentId = studentId
        self.year = year
        
    def takeExame(self):
        print("Student is Taking Exam..")
```
