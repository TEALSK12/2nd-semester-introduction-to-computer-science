# Lab 3.03 - War (Card Game)

1) Create a program that lets a user play the card game ['War'](http://www.pagat.com/war/war.html). 

Your game should: 

* Start with a given shuffled deck variable.
* Ask for player1 and player2's names.
* Have a function `player_turn`, with the contract shown below:

```python
#player_turn: takes in a player name, player_name, and draws/removes a card from the deck, prints "user drew card x", and returns the value 
#input: player_name, string 
#output: string
```
* Have a function `compare_scores` that takes in the two strings representing the cards drawn and compares the card values. Make sure to write the contract for `compare_scores`!
* Include a while loop that keeps the game running until there are no cards in the deck.
* Keep track of the score.
* Declare the name of the winner and final score at the end of the game.


###Bonus!
Instead of closing the program. Create a way for the user to play again.