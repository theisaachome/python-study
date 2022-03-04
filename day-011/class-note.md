# Python Class and Object

## Table of Content

- [Python Class](#python-class)
- [Create Class](#create-class)
- [Create Object](#create-object)
- [The __init__() Function](#the-init-function)
- [Instance Method](#instance-methods)
- [The self Parameter](#the-self-parameter)
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