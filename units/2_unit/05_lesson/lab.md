# Lab 2.05 - College Chooser

1. For each example below, predict what will be printed. Next, run the program and confirm what was output. 

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])
```

<br>
```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])
```
<br>
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])
```
    
<br>
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)
```
<br> 

2) Remember the game show program from last lab? Create this game again using lists and indexes. Updated rules below: 

* Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.
* User picks a number.
* Print prize associated with the door user picked. 

3) Create a quiz to help you choose which college you should go to (or another topic of your choice. See Example Below)! The program should ask the user a question and list five possible answers. If the student chooses the first answer, add 1 point to `School[0]`. If they choose the second answer add 1 point to `School[1]`, and so on. At the end print out the schools and the scores for each school. 
* Create a list of 5 options of colleges.
* Create a different list of five 0s, representing the user's votes so far.
* Create 4 questions. Each question should have five different answers. Each answer corresponds to the specific school option.
* At the end print off the 5 different schools and the score the user got for each of those schools. 
* Example: [Buzzfeed's What Should your college major actually be Quiz](http://www.buzzfeed.com/mattbellassai/what-should-your-college-major-actually-be#.kjaWpyrAwn)
###Bonus!
Research nested lists and work through the following: 

```python
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
```
<br>

```python
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
```
<br>

How would you access 'd' from the list `a`? 