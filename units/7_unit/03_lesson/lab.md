# Lab 7.03 - Kangaroo Class

1. Finish writing the `__add__` method for the time class. 

2. This exercise is a cautionary tale about one of the most common, and difficult to find, errors in Python. Write a definition for a class named Kangaroo with the following methods:
	1. An __init__ method that initializes an attribute named pouch_contents to an empty list.
	2. A method named put_in_pouch that takes an object of any type and adds it to pouch_contents.
	3. A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch.

Test your code by creating two Kangaroo objects, assigning them to variables named kanga and roo, and then adding roo to the contents of kanga’s pouch

## Extra Credit: 
If you have extra time, research `isinstance` function to write a method, `is_friend` that will take in another pet and return `True` if the two pets are friends are not. If they are both dogs they are friends. If the instance is a dog and the other pet is a cat, they are friends. If the instance is a cat and the other is a dog they are not friends. If they are both cats they are not friends. 