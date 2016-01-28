# Lab 6.04 - Dictionaries Looping

In this lab we will use our code from the word count lab (Lab 6.02) to create a program that will return the top 5 most used words in a document. 

The program, `most_frequent_lab.py`, will print out the top 5 most frequently occurring words in a paragraph. It should print out the word and the number of times used. 

1. Take your old lab code and turn it into a function that takes in a list of words and returns a dictionary of word frequencies.
2. Write a different function, `find_max_value`, that will loop through the dictionary and keep track of the top value in that dictionary and return the key of the max value.
3. Print out the key/value of the highest value.
4. Remove that key from the dictionary. 
5. Repeat steps 2-4 four more times: Call `find_max_value`, print out the key/value pair, and remove the key.

If there is a tie, choose just one of the tied items to print. 

### Example

```
>>> python3 most_frequent_lab.py
cats, 3
are, 2
kittens, 1
cool, 1
pet, 1
```

## Bonus!
This process of finding the max element, printing it, and removing it from the dictionary is a way to sort items. Write a function that will return a sorted list of all the words from most frequent to least frequent. 

Change the code to find the least frequent words. 