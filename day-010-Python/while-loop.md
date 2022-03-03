# Python While Loops


## While loop
```py
i = 1
while i < 6:
  print(i)
  i += 1
```


## The break Statement


```py
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```


## The continue Statement

```py
i = 0;
while i < 6:
    i += 1;
    if(i ==3):
        continue
    print(i);
```

## The Else Statement

```py
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
```

## For Loop

```py
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

## The range() Function

```py
for x in range(6):
  print(x)
```

```py
for x in range(2,8):
    print(x);
```