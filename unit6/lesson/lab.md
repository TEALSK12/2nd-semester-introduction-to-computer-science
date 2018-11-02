# Lab 6.01

Write a program that uses a dictionary to offer users the meanings of common internet abbreviations.

The program, `dictionary_lab.py`, that prompts the user to enter an internet abbreviation they would like explained. If the requested abbreviation is in the program's dictionary \(use the `in` keyword with an `if` statement to test this\), then it prints out the definition. If the abbreviation is not in the dictionary, the program prints an apologetic message saying that it could not find a definition.

### Example Output

```text
>>> python3 dictionary_lab.py

What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What would would you like to look up?
```

## Bonus!

Extend the program with any of these features:

* the user can update the definitions \(values\) for existing abbreviations in the dictionary
* the user can add new abbreviations \(keys\) and provide their definitions \(values\).
* the user can delete entries \(key, value pairs\) from the dictionary.
* the user can get the entire dictionary printed to the screen.

Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial about dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) and the [advanced Python documentation about dictionaries](https://docs.python.org/3/library/stdtypes.html#typesmapping).

