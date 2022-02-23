## Python String

## Table of Contents
- [String](#string)
- [MultiLine Strings](#multiline-strings)
- [Strings Are Arrays](#strings-are-arrays)
- [Loop A String](#looping-through-a-string)
- [String Length](#string-length)

- [String operation](#string-operations)
    - [Slicing String](#slicing-string)
    - [String Concatenation](#string-concatenation)
    - [in as a logical Operators in String](#in-as-a-logical-operator)


---

## **String**
A string is simply a series of characters.

Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings like this:

```
"This is a string."

'This is also a string.'
```

---

## **Multiline Strings**

You can assign a multiline string to a variable by using three quotes:

```py
message ="""
I told my friend, "Python is my favorite language!
The language 'Python' is named after Monty Python, not the snake.
One of Python's strengths is its diverse and supportive community."""
```

---

## **Strings are Arrays**

Strings in Python are arrays of bytes representing unicode characters.

```py
info = "Configuration File";
print(info[2]);
```


## **Looping Through a String**

Since strings are arrays, we can loop through the characters in a string, with a for loop.

```py
info = "Configuration File";
for w in info:
    print(w)
```


## **String Length**

To get the length of a string, use the len() function.

```py
message="HelloWorld"
print(len(message))
```


---
 
## in as a Logical Operator 

Use the keyword `in` to check if a certain phrase or character is present in a string,

```py
txt = "The best thing in the world is love. Show love to each other."
print("love" in txt);
```

More Example with If:
```py

txt = "The best thing in the world is love. Show love to each other."
if "love" in txt:
    print("Love is most important")

```

---

## **String operations**

## Slicing String

You can return a range of characters by using the slice syntax.

Use `color operator`.


the `start index` and `the end index` (up to but not including)
Example:
```py
s = "Python Study";
print(s[0:4]); #Pyth
```

### **Slice From the Start**


By leaving out the start index, the range will start at the first character:

```py
s = "Python Study";
print(s[:7])
```

### **Slice To the End**
By leaving out the end index, the range will go to the end:

```py
s="Hello World from python"
print(s[0:])
```

---

## **String concatenation**

When the  `+`  operator is applied to strings, it means “concatenation”

Example:
```py
s1="Studying Python";
s2=" is a must in 2022";
sms = s + s2;
print(sms)
```

```py
a="Hi";
b="There"
c= a + " " + b;
print(c);
```