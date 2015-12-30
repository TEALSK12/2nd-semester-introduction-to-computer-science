# Project 4: Tic-Tac-Toe

Using Python, students will create a complete Tic-Tac-Toe game. This project has two parts: 
1. Designing the game so that two users can play Tic-Tac-Toe against one another.
2. Creating a Tic-Tac-Toe checker which will check the board to see if Xs or Os have won the game. 

## Overview
[Tic-Tac-Toe](http://www.merriam-webster.com/dictionary/tic-tac-toe) is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries to be the first to fill a row, column, or diagonal of squares with either X's or O's. We will be writing an interactive Tic-Tac-Toe program. At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game. 

### Behavior
* The program will prompt the user to enter their name and their opponents name. 
* Whoever enters their name first will be playing as X's, and the other player will be O's. 
* The players will take turns inputing the row and column they would like to place their mark. 
* If that spot is already taken the program will ask for the spot again. 
* The program will report which player has won.
* If there are no more spots open and nobody has won the game, the program will print `Tie game!`.

### Implementation Details
* variables to store the user names for customized prompts
* a game board represented as a list of lists size 3 by 3
* check for a winner horizontally, vertically and both diagonals
* user cannot overwrite a spot on the board

## Grading 
### Scheme/Rubric
| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| Program prompts user for name | 2   |
| Program marks board where user requested| 10|
| Program won't overwrite value on board | 5   |
| Program reports who won or if there was a tie             | 15  |
| Program ends after win, loss, or tie       | 3  |
| **Sub total**                                                   | 35  |
| **Technical Correctness   **                                    |     |
| Correct use of game loop                                        | 5  |
| Correctly indexes into lists of lists to store board            | 5  |
| Correctly check board for mark                                  | 5  |
| Check for winners on all three horizontals and verticals        | 20  |
| Checks for winners on both diagonals                            | 10  |
| **Sub total**                                                   | 45  |
| **Total**                                                       | 80 |


