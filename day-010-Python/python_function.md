# Python Functions

## Table of Content
- [Functions](#functions)
- [Create Function](#create-function)
- [Arguments](#arguments)
- [Arbitrary Arguments](#arbitrary-arguments-args)
- [Keyword Arugments](#keyword-arguments)
- [Default Parameter Value](#default-parameter-value)
- [Return values](#return-values)
---

## **Functions**
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

---

## **Create Function**

```py
def greet():
    print("Hello from function block");

greet()
```

---

## Arguments

```py
def sayHi(name):
    print("Hi ",name);

sayHi("Isaac Home");
```

---

## Arbitrary Arguments, *args

If the number of arguments is unknown, add a * before the parameter name:

```py
def showColors (*colors):
    print("My Favourite Color is : ",colors[2]);

showColors("red","Green","black")
```

---

## Keyword Arguments

You can also send arguments with the key = value syntax.

```py
def showEmployeeInfo(name,address, email):
    print("**** Employee Information ****")
    print("Name " + name + "\nAddress : " + address + "\nEmail : " + email);

showEmployeeInfo(name="Isaachome",address="Yangon",email="isaachome@example.com");
```

---

## Arbitrary Keyword Arguments, **kwargs

If the number of keyword arguments is unknown, add a double ** before the parameter name:

```py
def login(**kid):
  print("Email :" + kid["lname"])

my_function(email = "test@gmail.com", password = "******")
```

---

## Default Parameter Value

```py

def showStatus(status="Offline"):
    print("She is " + status );

showStatus("Online");
showStatus();
```

## Return Values

```py
def my_function(x):
  return 5 * x

print(my_function(3))
```