# Python Sets

## Table of Content
- [Set](#set)
    - [Constructor](#the-set-constructor)

- [Access Items](#access-items)
- [Add Items](#add-items)
- [Remove Item](#remove-item)
---


## Set

Sets are used to store multiple items in a single variable.  
A set is a collection which is unordered, unchangeable*, and unindexed.

```py
computer = {"Apple","Dell","Lenovo"};
```
### Duplicates Not Allowed

```py
computer = {"Apple","Dell","Lenovo","Dell"};
```

### The set() Constructor

- note the double round-brackets
```py
example = set(("apple", "banana", "cherry")) 
```

---

## Access Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop,

```py
for laptop  in computer:
    print(laptop);
```


 or ask if a specified value is present in a set, by using the in keyword.

 ```py
examples = set(("Item 1" ,"Item 2" ,"Item 3"))
print("Item 1" in examples);
 ```

 ---

 ## Add Items

 To add one item to a set use the add() method.

 ```py

examples.add("Cat");
 ```

 ---

## Remove Item
To remove an item in a set, use the remove(), or the discard() method.

```py
example = {"apple", "banana", "cherry"}

example.remove("banana")

```

```py
example = {"apple", "banana", "cherry"}

example.discard("banana")
```