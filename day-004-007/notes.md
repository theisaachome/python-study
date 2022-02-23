# Python Booleans

## Table of Contents

- [Boolean Values](#boolean-values)
- [Evaluate Values and Variables](#evaluate-values-and-variables)
---

### **Boolean Values**

To know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

Booleans represent one of two values: True or False.

```py
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

A condition in an if statement, Python returns True or False:

Example:
```py
teamAScore=200;
teamBScore=380;

if(teamAScore>teamBScore):
    print("Team A Score more than team B");
else:
    print("Team B Score More than Team A");
```

---
### **Evaluate Values and Variables**


Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.

```py
print(bool("Isaachome"))
print(bool(15))
```