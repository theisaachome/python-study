# Python Iterator

## Table of Content

- [Iterator](#iterator)
- [Iterator vs Iterable](#iterator-vs-iterable)

- [Loop through an iterator]
---

## Iterator
In Python, an iterator is an object which implements the iterator protocol, which consist of the methods `__iter__()` and `__next__()`.

---

## Iterator vs Iterable

Lists, tuples, dictionaries, and sets are all iterable objects.   
They are iterable containers which you can get an iterator from.

All these objects have a `iter()` method which is used to get an iterator:

### Example
```py
fruits = ("apple", "banana", "cherry");

myIterator = iter(fruits);

print(next(myIterator));
print(next(myIterator));
print(next(myIterator));
```
---

Even strings are iterable objects, and can return an iterator:

```py
name = "Egg";
myEggIterator = iter(name);

print(next(myEggIterator));
print(next(myEggIterator));
print(next(myEggIterator));
```

---

## Looping Through an Iterator

```py
fruits = ("apple", "banana", "cherry");
for f in fruits:
    print(f);
```


## Create an iterator
```py
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
```