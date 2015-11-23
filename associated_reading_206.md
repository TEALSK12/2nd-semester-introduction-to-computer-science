# Associated Reading 2.06

# List operations
The + operator concatenates lists:
```
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print c
[1, 2, 3, 4, 5, 6]
```

Similarly, the * operator repeats a list a given number of times:
```
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```
The first example repeats [0] four times. The second example repeats the list [1, 2, 3] three times.
10.5  List slices

The slice operator also works on lists:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c', 'd']
>>> t[3:]
['d', 'e', 'f']
If you omit the first index, the slice starts at the beginning. If you omit the second, the slice goes to the end. So if you omit both, the slice is a copy of the whole list.
>>> t[:]
['a', 'b', 'c', 'd', 'e', 'f']
Since lists are mutable, it is often useful to make a copy before performing operations that fold, spindle or mutilate lists.
A slice operator on the left side of an assignment can update multiple elements:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3] = ['x', 'y']
>>> print t
['a', 'x', 'y', 'd', 'e', 'f']
10.6  List methods

Python provides methods that operate on lists. For example, append adds a new element to the end of a list:

>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print t
['a', 'b', 'c', 'd']
extend takes a list as an argument and appends all of the elements:
>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print t1
['a', 'b', 'c', 'd', 'e']
This example leaves t2 unmodified.
sort arranges the elements of the list from low to high:

>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> print t
['a', 'b', 'c', 'd', 'e']
List methods are all void; they modify the list and return None. If you accidentally write t = t.sort(), you will be disappointed with the result.

10.8  Deleting elements

There are several ways to delete elements from a list. If you know the index of the element you want, you can use pop:

>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print t
['a', 'c']
>>> print x
b
pop modifies the list and returns the element that was removed. If you don’t provide an index, it deletes and returns the last element.
If you don’t need the removed value, you can use the del operator:

>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print t
['a', 'c']
If you know the element you want to remove (but not the index), you can use remove:
>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']
The return value from remove is None.
To remove more than one element, you can use del with a slice index:

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> del t[1:5]
>>> print t
['a', 'f']
As usual, the slice selects all the elements up to, but not including, the second index.
Exercise 4  
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
Exercise 5  
Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.