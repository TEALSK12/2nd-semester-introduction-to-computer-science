# Lab 2.06 - Tic-Tac-Toe

## For each example below, in your notebook, predict what will be printed. Then run the program and confirm. 

### Example 1

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0:3])
    print(a[1:4])
```

### Example 2

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[1:len(a) - 3])
```
### Example 3
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a.remove('b')
    print(a)
    print(b)
```
### Example 4
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    a[0] = 'haha'
    b = a.pop()
    print(a)
    print(b)
```
### Example 5
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a + ['abc']
    print(a)
    print(b)
```
### Example 6
    
```python
    a = ['a', 'b', 'c', 'd', 'e']
    b = a.append('f')
    print(a)
    print(b)
```

## Tic Tac Toe (Continued)
### We are going to start implementing Tic-Tac-Toe using a single list.
1. The user picks a location on the board according to the number:
  
  ![tic-tac-toe](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrA_MowUM-KZXl1CpkrQhi8W505dM3cxZG1787i9qFz8KefqFkIQ)
  
2. Depending on the position that the user inputs, update the position of the board to an "X" to reflect that.
3. Print the updated board out, but don't worry about making it look pretty.
4. Only need to implement one turn of the game
