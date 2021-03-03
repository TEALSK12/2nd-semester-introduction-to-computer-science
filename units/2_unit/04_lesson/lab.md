# Lab 2.04 - food chooser

## 1. In your notebook

For each example below, predict what will be printed. Run the program and write down the output in your notebook.

### Example 1

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])
```

### Example 2

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])
```

### Example 3

```python
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])
```

### Example 4

```python
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)
```

## 2. Create a game again using lists and indexes

* Declare 10 prizes (prize0, prize1, prize2 at the top of your file)
* Store them all in a list.
* User picks a number.
* Print prize associated with the door user picked.

## 3. Create a quiz

Create a food quiz using lists and indexes.

1. List of 6 different foods.
2. Ask the user 8 vague questions to find out what their favorite food is using the list.
3. Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

[Starter code here](Starter_food_chooser.py)

## Bonus

* Use the score list to print out the user's second favorite food as well as the favorite.
* Tied scores can be handled in any reasonable way -- e.g., print the tied-score food item earliest on the list as the "favorite", and the next item as the "second favorite".
* Alternatively, check for the existence of a tie, and acknowledge that situation when it happens by printing a separate message.
