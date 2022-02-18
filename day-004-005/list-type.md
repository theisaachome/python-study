# **`Python List`**

## Table of Contents
- [List](#list)
    - [Ordered](#ordered)
    - [Changeable](#changeable)
    - [Allow Duplicates](#allow-duplicates)
    - [List Constructor](#constructor)
- [Access List Item](#access-list-item)
    - [Nagative Index](#negative-indexing)
    - [In the keyword](#in-the-keyword)
- [Change List Items](#change-list-items)
    - [Change a range of Item Values](#change-a-range-of-item-values)
- [Add List Items](#)

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

---

## **`Access List Item`**

List items are indexed and they can be  accessed them by referring to the index number:

Example
```py
students =["Aung Aunng","Zaw Zaw","Maw Maw","Thaw Thaw","Aung Aung"];
print(students[1]);
```

## **`Negative Indexing`**

Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

```py

students =["Aung Aunng","Zaw Zaw","Maw Maw"];
#Maw Maw
print(students[-1]); 
```

## **`Range of Indexes`**

Get a range of indexes by specifying where to `start` and where to `end` the range.

`start index` 
- the index of where to start
`end index`:
- the total count of the element of the list not the index.


Example:
```py
students =["Thidar","Zaw Zaw","Maw Maw","Thaw Thaw","Aung Aung"];
print(students[1:4]);
```


When specifying a range, the return value will be a new list with the specified items.

```py
newList = students[1:3];
print(newList)
```


---
## **`in` The keyword**

To determine if a specified item is present `in` a list use the in keyword:

```py
search="Luke"
employee = ["John","James","Mark","Luke"];
if search in employee:
    print(employee[employee.index(search)] + " is here in the office today.");
else:
    print("Sorry  He is not here.");
```

---
## **`Change List Items`**

### Change Item Value

To change the value of a specific item, refer to the index number:

Example
```py
emails=["aung@email.com","zaw@gmail.com","naw@gmail.com"];
print(emails);
emails[0]="aung@gmail.com";
print(emails);
```

## **`Change a Range of Item Values`**

To change the value of items within a specific range:

- define a list with the new values, and 

- refer to the range of index numbers where you want to insert the new values:

Example:
```py
toBuyItems=["apple", "banana", "cherry", "orange", "kiwi", "mango"];
toBuyItems[1:3] = ["blackcurrant", "watermelon"];
print(toBuyItems)
```

Replacing  two new values:
```py
toBuyItems = ["apple", "banana", "cherry"]
toBuyItems[1:2] = ["blackcurrant", "watermelon"]
print(toBuyItems)
```

---

## **`Add List Items`**

### **`Append Items`**
To add an item to the end of the list, use the append() method:

```py
emails.append("new@gmail.com");
print(emails);
```


### **`Insert Items`**
To insert an item at a specified index,use the insert() method:

```py
toBuyItems = ["apple", "banana", "cherry"]
toBuyItems.insert(1, "orange")
print(toBuyItems)
```

---

## **`Extend List`**

### Extend List

To append elements from another list to the current list, use the extend() method.

Example
```py
listOne = ["apple", "banana", "cherry"]
listTwo = ["mango", "pineapple", "papaya"]
listOne.extend(listTwo)
print(listOne)
```