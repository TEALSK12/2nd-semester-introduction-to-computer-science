# Lab 2.07

1. Predict what will be printed. Then run the program and confirm. 
    *  
    *  ```
        a = 0
        while a< 100: 
            print(a)```
    <br>
    *  
    *  ```
        a = 0
        while a < 100: 
            a = a + 1
            print(a)```
    <br>
    
    *  
    *  ```
        a = input("Would you like to quit: ")
        while a != "y": 
            a = input("Would you like to quit: ")
    ```
    <br>

2. Remember the tic-tac-toe game we started to create last week? We are going to keep implementing the game.
    * Allow users to keep playing (max 9 times) 
    * Use variables to decide whose turn it is, and greet them as Xs or Os 
    * User picks a location on the board according to the number: 
    ![tic-tac-toe](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRrA_MowUM-KZXl1CpkrQhi8W505dM3cxZG1787i9qFz8KefqFkIQ)
    * depending on the position user gave,  update the position of the board to reflect that
    * print the board out 
