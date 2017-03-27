# Lab 3.03 - War (Card Game)

1) Create a program that lets a user play a **simplified** version of the card game ['War'](http://www.pagat.com/war/war.html).  In this version, the users will share a single deck of cards and cards will not be added back to the deck after they have been played.

Your game should:

* Start with a given shuffled deck variable (shuffle function comes from python's random library, more details below)
* Ask for player1 and player2's names.
* Have a function `player_turn`, with the contract shown below:

```python
# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck, prints "user drew card x", and returns the value
# input: player_name as string, deck as list
# returns: integer
```
* Have a function `compare_scores` that takes in the two integers representing the cards drawn and compares the card values. Make sure to write the contract for `compare_scores`!
* For simplicity Jacks will be represented as 11, Queens will be represented as 12, Kings will be represented as 13, and Aces will be represented as 14
* For simplicity the suit does not matter
* Include a while loop that keeps the game running until there are no cards in the deck.
* If there is a tie, there is "war".  Take the next two cards an whoever wins that gets all four cards (including the previous tied cards).  If there is another tie, continue taking the next two cards until there a winner.  The winner takes all the "war" cards.
* Keep track of the score.
* Player who won the most number of cards wins.
* Declare the name of the winner and final score at the end of the game.

### Deck Shuffling

While seemingly simple-- shuffling a deck is a somewhat complicated problem. Luckily, Python's random library has a built in shuffle algorithm. Feel free to read the documentation, but we have provided a simple wrapper function that will return to you a shuffled deck of cards.

```python

import random

# shuffled_deck: will return a shuffled deck to the user
#input:
#output: a list representing a shuffled deck
def shuffled_deck():
	basic_deck = list(range(2, 15)) * 4
	random.shuffle(basic_deck)
	return basic_deck
```

###Bonus!
Instead of closing the program when the deck is empty, create a way for the user to play again.
