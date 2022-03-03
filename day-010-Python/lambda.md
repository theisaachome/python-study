# Python Lambda


A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

## Syntax
```
lambda arguments : expression
```

The expression is executed and the result is returned:

```py
l = lambda a : a + 10
print(l(5))
```

## Multiply argument 

```py
l = lambda a, b : a * b
print(l(5, 6))
```

---

## Why  Lambda Functions?

```py
def myfunc(n):
  return lambda a : a * n
```

```py
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```