# Python Scope

- [Local Scope](#local-scope)
- [Function Inside Function](#function-inside-function)
- [Global Scope](#global-scope)
- [Naming](#naming-variables)
- [Global Keyword](#global-keyword)
---

## Local Scope  
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


```py
def myfunc():
  x = 300
  print(x)

myfunc()
```


## Function Inside Function

The variable x is not available outside the function, but it is available for any function inside the function:

### Example
The local variable can be accessed from a function within the function:

```py
def myfunc():
  x = 300
  def myinnerfunc():
    print("value from outer function : ",x)
  myinnerfunc()

myfunc()
```
---

## Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

```py
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
```

## Naming Variables
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):


```py
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
```

---
## Global Keyword

The global keyword makes the variable global.

## Example
If you use the global keyword, the variable belongs to the global scope:

```py
def myfunc():
  global x
  x = 300

myfunc()

print(x)
```


### Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:

```py
x = 300

def myfunc():
  global x
  x = 200 #set new value for global x

myfunc()

print(x)
```