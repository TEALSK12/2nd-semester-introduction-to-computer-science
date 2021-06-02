# Project 4: Tic-Tac-Toe

Using Python, students will create a Tic-Tac-Toe game. This project has two parts:

1. designing the game so that two users can play Tic-Tac-Toe against one another; and
2. creating a Tic-Tac-Toe checker that will check the board to see if `Xs` or `Os` have won the game.

## Overview

[Tic-Tac-Toe](http://www.merriam-webster.com/dictionary/tic-tac-toe) is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries to be the first to fill a row, column, or diagonal of squares with either X's or O's. We will be writing an interactive Tic-Tac-Toe program. At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game.

### Behavior

* The program will prompt the user to enter their name and their opponent's name.
* Whoever enters their name first will be playing as X's, and the other player will be O's.
* The program will print an empty game board as a starting point.
* The players will take turns inputting the row and column where they would like to place their mark.
* If that spot is invalid or already taken, the program will ask again for a valid spot.
* At the end of each player's turn the program will
  * check if that player has won.
  * print the updated game board.
* If there are no more spots open and nobody has won the game, the program will print `Tie game!`.

### Implementation details

* Use variables to store the user names for personalized prompts.
* Create a game board represented as a list of lists, size 3 by 3.
***Note: This is a change from our earlier implementations of Tic-Tac-Toe. Why do you think this might be better?***
* Check for a winner horizontally, vertically, and on both diagonals.
* Do not allow a user to overwrite a spot on the board where a play has already been made.
