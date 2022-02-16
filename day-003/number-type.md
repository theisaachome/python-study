# Python Numbers

## Table of Content
- [Python Numbers](#python-numbers)
- [Int](#int)
- [Float](#float)
- [Complex](#complex)
- [Type Conversion](#type-conversion)
- [Casting](#casting)

---
## **`Python Numbers`**

There are three numeric types in Python:
- int
- float
- complex

Variables of numeric types are created when you assign a value to them:

```py
# int
intNum = 1  
 # float
floatNum = 2.8 
# complex
complexNum = 1j 
```

---

## **`Int`**

A whole number, positive or negative, without decimals, of unlimited length.

Example:
```py
incomeAmount = 1000;
balanceAmount = 35656222554887711;
totalExpenses = -3255522;
```

---

## **`Float`**

A number, positive or negative, containing one or more decimals.

Example
```py
x = 1.10
y = 1.0
z = -35.59
```

---

## **`Complex`**

Complex numbers are written with a "j" as the imaginary part:

Example
```py
x = 3+5j
y = 5j
z = -5j
```

---

## **`Type Conversion`**

You can convert from one type to another with 
- the int(),
- float(), and
- complex() methods:

Example
```py
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

Convert from int to float:
```
a = float(x)
```
Convert from float to int:
```
b = int(y)
```

Convert from int to complex:
```
c = complex(x)
```

---

## **`Casting`**

Casting in python is  done using constructor functions:

Example
Integers:

x will be 1


```py
x = int(1) 
```
 
 z will be 3

```py
z = int("3")
```

y will be 2
```py 
y = int(2.8)
```
---

Floats:

Example

x will be 1.0
```py
x = float(1) 
```

w will be 4.2
```py
w = float("4.2") 
```

z will be 3.0
```py
z = float("3") 
```

Example
Strings:

x will be 's1'
```py
x = str("s1") 
```

y will be '2'
```py
y = str(2) 
```

z will be '3.0'
```py
z = str(3.0) 
```