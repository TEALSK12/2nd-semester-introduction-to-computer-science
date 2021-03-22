# Lab 3.02 - Birthday Song & Random Cards

## Lab Exercise 1

Create a function, `birthday_song`, that prints out the happy birthday song to whatever name is input as an argument. The contract should be:

```python
    # Name: birthday_song
    # Purpose: birthday_song prints out a personalized birthday song
    # Arguments: name, string
    # Returns: none
    def birthday_song(name):
        # your code goes here
```

## Lab Exercise 2

* Create a function that randomly picks 5 cards from a deck
* The cards can repeat

Write out the contract for this function.

```python
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
```

### Bonus

* Practice passing in lists as arguments to a function. E.g., pass in `numbers` and `suits` lists to a modified `pick_5_cards()` function.  Modify the code to use those passed-in lists to make the card selections.

* What is different about passing in lists as arguments?

* Similarly, try returning a list as the return value (output) of a function.  For example, have the `pick_5_cards()` function return a list of selected cards instead of printing anything inside the function.  After calling the function, have the main part of your code print out the list of cards that was returned.

* Read about list aliasing in section 3.4 of the associated reading, and write down what is happening in this case.
