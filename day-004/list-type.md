# **`Python List`**

## Table of Contents
- [List](#list)
    - [Ordered](#ordered)
    - [Changeable](#changeable)
    - [Allow Duplicates](#allow-duplicates)
    - [List Constructor](#constructor)

## **`List`**

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```py
shoppingList = ["apple", "banana", "cherry"]
```

## **`List Items`**

List items are `ordered`, `changeable`, and allow `duplicate` values.

List items are indexed starting from [0].


### **`Ordered`**

The list items have a defined order,
if you add new item to a list , it will be placed at the end of the list  and that order will not change.


### **`Changeable`**

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.



### **Allow Duplicates**
Since lists are indexed, lists can have items with the same value:

```py
students =["Aung Aunng","Zaw Zaw","Maw Maw","Thaw Thaw","Aung Aung"];
```

### **List Length**

To determine how many items a list has, use the len() function:
```py
students =["Aung Aunng","Zaw Zaw","Maw Maw","Thaw Thaw"];
print(len(students))
```

### **`Constructor`**

It is also possible to use the list() constructor when creating a new list.


```py
myList = list(("apple", "banana", "cherry")) 
```