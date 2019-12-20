# Alternate Project 4: Tic-Tac-Toe
Modified by Brian Weinfeld

Using loops and variables, you will create a Tic-Tac-Toe game. This project has two parts

1. Creating functions which will support the main game loop.
2. Designing the game loop so that two users can play Tic-Tac-Toe against one another.

## Overview

[Tic-Tac-Toe](http://www.merriam-webster.com/dictionary/tic-tac-toe) is a game in which one player draws X's and another player draws O's inside a set of nine squares and each player tries to be the first to fill a row, column, or diagonal of squares with either X's or O's. We will be writing an interactive Tic-Tac-Toe program. At the end of each turn the computer will check to see if X's have won the game or if the O's have won the game.

### Behavior

* The gameboard should be stored in a list of lists. Each of the internal lists represents one row of the gameboard. If the element in the list is the empty string (the empty string is ''), then the spot is unoccupied. If the element in the list is an 'X' or an 'O', then it is occupied by that player.

* Complete the below method which nicely prints the gameboard.

```python
def print_gameboard(gameboard):
  # finish
```

* Complete the below method which determines whether a player has won or not. Return 'X' or 'O' if either of those players have won and None if neither player has won.

```python
def check_winner(gameboard):
  # finish
```
* Complete the below method which determines whether the game has tied (all the spaces are filled and no player has 3 in a row). Return True if the game is tied and False if it has not.

```python
def check_tied(gameboard):
  # finish
```
* Complete the below method which allows a player to make a move. Prompt the user by their name for a row and column and place their symbol in the indicated spot. If they select an illegal spot, prompt them for a new selection.

```python
def make_move(gameboard, name, symbol):
  # finish
```

After completing and testing the above functions, complete the following steps to create the main game loop.

* Prompt the 'X' player and 'O' player for their names. You can use these names to prompt each player for their move.
* The players will take turns making moves utilizing the make_move function
* At the end of each player's turn the program will:
  * check if that player has won using the check_winner function.
  * print the updated game board using the print_gameboard function.
* If there are no more spots open and nobody has won the game, the program will print `Tie game!`. Check this using the check_tied function.
* After the game is over, prompt the players if they would like to play again or quit.

## Challenge

* Going first is a big advantage in this game. Modify your game loop so that if the users indicate they want to play again, the players swap who goes first. The players should keep their symbol ('X' or 'O') but the symbol that goes first should swap. Every time the players replay the game, the player who goes first should swap.

* Modify the gameloop so that instead of two human players, either (or both) of the players can be computers. The computer's names can be some variation on "Computer 1". Modify the make_move function so that computer can make an automatic selection. To begin, simply have the computer randomly select an available empty space for their move.

## Super Challenge

The super challenge will require knowledge that has not been taught yet. You will need to do additional research on your own. Good luck!

* Continue to build on the above challenge by giving the computer some basic game logic. If the other player is about to win (ie: they have two in a row), then the computer should always select the blocking move. What can of logic can you give the computer for its turn if it doesn't have to make a blocking move?

## Solution

```python

```
