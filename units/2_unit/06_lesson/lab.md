# Lab 2.06 - Tic-Tac-Toe

1) For each example below, predict what will be printed. Then run the program and confirm. 

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0:3])
    print(a[1:4])
```
<br>

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[1:len(a) - 3])
```

<br>
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a.remove('b')
    print(a)
    print(b)
```
<br>
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    a[0] = 'haha'
    b = a.pop()
    print(a)
    print(b)
```
<br> 
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a + ['abc']
    print(a)
    print(b)
```
<br>     
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a.append('f')
    print(a)
    print(b)
```
<br> 

2) Remember the tic-tac-toe board we created in class? We are going to start implementing Tic-Tac-Toe using a single list.

* The user picks a location on the board according to the number: 
    ![tic-tac-toe](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrA_MowUM-KZXl1CpkrQhi8W505dM3cxZG1787i9qFz8KefqFkIQ)
* Depending on the position that the user inputs, update the position of the board to reflect that.
* Print the updated board out, but don't wory about making it look pretty.
* Only need to implement one turn of the game
