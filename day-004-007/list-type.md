# **Python List**

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
- [Add List Items](#add-list-items)
    - [Append Items](#append-items)
    - [Insert Items](#insert-items)
    - [Extend List](#extend-list)
- [Remove List Items](#remove-list-items)
    - [Remove Method](#remove-method)
    - [Pop Method](#pop-method)
    - [del keywordd](#del-keyword)
    - [clear method](#clear-method)
- [Looping List](#looping-list)
    - [for loop](#for-loop)
    - [loop index](#loop-through-the-index-numbers)
    - [while loop](#using-a-while-loop)
    - [list Comprehension](#looping-using-list-comprehension)
- [List Comprehension](#list-comprehension)
- [Sort List](#sort-lists)
    - [reverse sort](#sort-descending)
- [Copy List](#copy-lists)


## **List**

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```py
shoppingList = ["apple", "banana", "cherry"]
```

## **List Items**

List items are `ordered`, `changeable`, and allow `duplicate` values.

List items are indexed starting from [0].


### **Ordered**

The list items have a defined order,
if you add new item to a list , it will be placed at the end of the list  and that order will not change.


### **Changeable**

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

### **Constructor**

It is also possible to use the list() constructor when creating a new list.


```py
myList = list(("apple", "banana", "cherry")) 
```

---

## **Access List Item`**

List items are indexed and they can be  accessed them by referring to the index number:

Example
```py
students =["Aung Aunng","Zaw Zaw","Maw Maw","Thaw Thaw","Aung Aung"];
print(students[1]);
```

## **Negative Indexing**

Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

```py

students =["Aung Aunng","Zaw Zaw","Maw Maw"];
#Maw Maw
print(students[-1]); 
```

## **Range of Indexes**

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
## **Change List Items**

### Change Item Value

To change the value of a specific item, refer to the index number:

Example
```py
emails=["aung@email.com","zaw@gmail.com","naw@gmail.com"];
print(emails);
emails[0]="aung@gmail.com";
print(emails);
```

## **Change a Range of Item Values**

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

## **Add List Items**

### **Append Items**

To add an item to the end of the list, use the append() method:

```py
emails.append("new@gmail.com");

print(emails);
```


### **Insert Items**
To insert an item at a specified index,use the insert() method:

```py
toBuyItems = ["apple", "banana", "cherry"]

toBuyItems.insert(1, "orange")

print(toBuyItems)
```

---

## **Extend List**

### Extend List

To append elements from another list to the current list, use the extend() method.

Example
```py
listOne = ["apple", "banana", "cherry"]

listTwo = ["mango", "pineapple", "papaya"]
listOne.extend(listTwo)
print(listOne)
```

---
## **`Remove List Items`**


### **`remove method`**
The remove() method removes the specified item.

Example
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
print(myContact);
myContact.remove("John Cena");
print(myContact);
```

### **`pop method`**
The pop() method removes the specified index.

Example
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
myContact.pop(2);
```

If you do not specify the index, the `pop()` method removes the last item.

Example
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
myContact.pop(); #John Wick is removed
```


### `del` keyword

The del keyword also removes the specified index:

Example
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
del myContact[1];
```

The del keyword can also delete the list completely.

Example
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
del myContact;
```

Empties the list.The list still remains, but it has no content.
```py
myContact = ["John Cena","The Rock","John Petrucci","John Wick"];
del myContact[:];
```


### clear method
The clear() method empties the list.

The list still remains, but it has no content.

```py

onlineStudents = ["Aung Gyi","Kyaw Gyi","Zaw Gyi","Maw maw"];
onlineStudents.clear();

print(onlineStudents);
```

----
## **`Looping list`**


### **`for loop`**
loop through the list items by using a for loop:

Example:
```py
cities = ["Yanong","NewYork","Liverpool"];
for city in cities:
    print(city);
```


### **Loop Through the Index Numbers**

loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

```py
names = ["Khant Zaw","Kyaw Hsu Thway","Min Lwin","Kyaw Lwin","Myo Myit Aung"];
for i in range(len(names)):
    print(names[i])

```

### Using a While Loop

Loop through the list items by using a while loop.

Use the `len()` function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.

```py
names = ["Khant Zaw","Kyaw Hsu Thway","Min Lwin","Kyaw Lwin","Myo Myit Aung"];

i=0;
while i < len(names):
    print(names[i]);
    i=i+1;

```

### Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

Example
```py
# only at python 3
[print(x) for x in names];
```

---
## **List Comprehension**

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

The Syntax
```py
newlist = [expression for item in iterable if condition == True]
```
The return value is a new list, leaving the old list unchanged.


Example
```py
names = ["Liverpool","ManU","Man City","Everton","Spurs"];
newList = [x for x in names if "a" in x];
print(newList);
```

---

## **`Sort Lists`**

Sort List Alphanumerically
List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

Example
```py
dataList = ["Egg","Facebook","Gozilla","Horse","Apple","Ball","Cat","Dog"];
dataList.sort();
print(dataList);
```

## **`Sort Descending`**
To sort descending, use the keyword argument reverse = True:

```py
dataList = ["Egg","Facebook","Gozilla","Horse","Apple","Ball","Cat","Dog"];
dataList.sort(reverse=True);
print(dataList);
```


---

## **`Copy Lists`**

```py
rawList = [100, 50, 65, 82, 23]
dataNum = rawList.copy();
```