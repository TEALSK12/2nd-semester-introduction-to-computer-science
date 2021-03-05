# Lab 2.05 - Tic-Tac-Toe

## In your Notebook

Follow the flow of execution in the following programs.  For each one, predict what will happen in your notebook.  Some examples may not show the correct syntax

### Example 1

```python
a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list[0:3])
print(a_list[1:4])
```

#### Example 2

```python
a_list = ['a', 'b', 'c', 'd', 'e']
print(a_list[1:len(a_list) – 3])
```

#### Example 3

```python
a_list = ['a', 'b', 'c', 'd', 'e']
b_list = a_list.remove('b')
print(a_list)
print(b_list)
```

#### Example 4

```python
a_list = ['a', 'b', 'c', 'd', 'e']
b_value = a_list.pop()
print(a_list)
print(b_value)
```

#### Example 5

```python
a_list = ['a', 'b', 'c', 'd', 'e']
b_list = a_list + ['abc']
print(a_list)
print(b_list)
```

#### Example 6

```python
a_list = ['a', 'b', 'c', 'd', 'e']
b_list = a_list.append('f')
print(a_list)
print(b_list)
```

### creating Tic-Tac-Toe using a single list

Create this game using lists and indexes, according to the following rules:

1. The user will pick a location on the board according to the number

        1  |  2  |  3  
        4  |  5  |  6  
        7  |  8  |  9

2. Depending on the position that the user inputs, update the position of the board to be an “X” to reflect that
3. Print the updated board out, but do not worry about making it look pretty
4. You only need to implement one turn of the game for now.