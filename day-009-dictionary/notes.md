# Python Dictionary

## Table of Contents

- [Dictionary](#dictionary)
    - [Dictionary Items](#dictionary-items)
    - [Dictionary Length](#dictionary-length)
    - [Dictionary Items Data Types](#dictionary-items---data-types)
- [Access Dictionary Items](#access-dictionary-items)
    - [Get Keys](#get-keys)
    - [Get Values](#get-values)
- [Change Dictionary Items](#change-dictionary-items)
    - [Update Items](#update-dictionary)
    - [Add Items](#add-dictionary-items)
- [Loop Dictionaries](#loop-dictionaries)

---

## Dictionary

- Used to store data values in key:value pairs.

- A collection which is ordered, changeable and do not allow duplicates.


```py
employee = {
    "name":"Aung Aung",
    "email":"aungaung@gmail.com",
    "phone":"09250832041",
    "address":"Yangon",
}
```

---

## Dictionary Items

Dictionary items are presented in `key:value` pairs, and can be referred to by using the key name.

```py
print(employee["address"])
# Yangon
```

## Dictionary Length

To determine how many items a dictionary has, use the `len()` function:

```py
print(len(employee))
```
## Dictionary Items - Data Types

```py
student = {
    "name":'Thaw Thaw',
    "year":2022,
    "isScholarship":False,
    "studies":["Social Science","Communications","Business"]
}
```
---

## Access Dictionary Items

 Access the items of a dictionary by referring to its key name, inside square brackets:

 ```py
year = student['year'];
print("She is studing in ",year);
 ```

A method called get() that will give you the same result:

```py
name = student.get("name");
print("Name : ",name);
```

---

## Get Keys
The `keys()` method will return a list of all the keys in the dictionary.

```py
keys = student.keys();
print(keys);
```

---

## Get Values

The `values()` method will return a list of all the values in the dictionary.


---

## Change Dictionary Items

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

```py
employee["address"]="New York"
```

## Update Dictionary

The update() method will update the dictionary with the items from the given argument.

The argument must be  key:value pairs.

```py
student.update({"major":"Law"})
```

## Add Dictionary Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

```py
account = {
    "name":"Zaw Zaw",
    "email":"zawzaw@gmail.com",
    "password":"password",
    "phone":"09250832041",
    "isDeactivated":False,
}
account["isActive"]=True;
print(account);
```


## Removing Items
There are several methods to remove items from a dictionary:

### The pop() Method
```py
account.pop("password")
```

### The popitem() method
The popitem() method removes the last inserted item

```py
account.popitem();
```

### del keyword

The del keyword removes the item with the specified key name:

```py
del account["password"]
```

The del keyword can also delete the dictionary completely:

```py
del account
```

The clear() method empties the dictionary:

```py
account.clear()
```

----

## Loop Dictionaries

- using for loop

```py
for acc in account:
    print(acc)
```

```py
for key in account:
    print(account[key]);
```

the `values()` method to return values of a dictionary:

```py
for acc in account.values():
    print(acc)
```


 the `keys()` method to return the keys of a dictionary:

 ```py
 for acc in account.keys():
    print(acc);
 ```

Using the items() method:
```py
for acc in account.items():
    print(acc);
```


---
## Copy Dictionary


the copy() method:

```py
phone_brand= {
    "id": "1",
    "name": "Nokia",
    "logo": "www.example/nokia",
}
```
```py

newBrand = phone_brand.copy();
newBrand["year"]=1990;
print(phone_brand);
print(newBrand)
```

 The built-in function dict():

 ```py
secondBrand= dict(newBrand);
print(secondBrand);
 ```

 ---
 ## Nested Dictionaries

```py
 car ={
    "numberOfGear":6,
    "bodyType":"Coupe",
    "numberOfSeater":4,
    "width":"1803 mm",
    "length":"4380 mm",
    "ownner":{
        "name":"Aung Aung",
        "address":"Yangon",
        "email":"aung@gmail.com"
    }
}
```