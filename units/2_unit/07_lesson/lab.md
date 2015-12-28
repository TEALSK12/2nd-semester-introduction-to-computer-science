# Lab 2.07 - Tic-Tac-Toe 

1. For each example below, predict what will be printed. Next, run the program and confirm.

```python
    a = 0
    while a< 100: 
        print(a)
```
| **Predicted Output** | **Actual Output** |
| --- | --- |
|<br> |<br> | 

```python
    a = 0
    while a < 100: 
        a = a + 1
        print(a)
```
| **Predicted Output** | **Actual Output** |
| --- | --- |
|<br> |<br> | 
    
```python
    a = input("Would you like to quit: ")
    while a != "y": 
        a = input("Would you like to quit: ")
```
| **Predicted Output** | **Actual Output** |
| --- | --- |
|<br> |<br> | 

2. Remember the Tic-Tac-Toe game we started to create last week? We are going to keep implementing the game.
    * Allow users to keep playing (max 9 times) 
    * Use variables to decide whose turn it is, and greet them as Xs or Os 
    * User picks a location on the board according to the number: 
    ![tic-tac-toe](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrA_MowUM-KZXl1CpkrQhi8W505dM3cxZG1787i9qFz8KefqFkIQ)
    * depending on the position user gave,  update the position of the board to reflect that
    * print the board out 

###Extra Credit: 
Create a variable-sized board. So instead of a classic 3 x 3 board, create a way for the user specify the size of the board they want to play with. 