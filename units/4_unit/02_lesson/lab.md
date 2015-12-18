# Lab 4.02 - Getting Loopy

## Part 1
Write a function `fruit_pluralizer`. It will take in a list of fruit and return nothing. The function should update the values of the list so that the values are plural. If the fruit name ends in a 'y' remove the 'y' and add 'ies', otherwise add an 's'.

1. Create the function contract for `fruit_pluralizer`. 
2. Provide a few examples that confirm `fruit_pluralizer` works as expected.
	* Include examples with 'berry'
	* What if the list is empty?
	* What if the fruit ends in 's'?
	
### Example
Example of the file: 

```python
# contract goes here
def fruit_pluralizer(list_of_strings): 
	# your code goes here
fruit_list = ['apple', 'berry', 'melon']
print("Single Fruit: " + str(fruit_list))
fruit_pluralizer(fruit_list)
print("No longer single Fruit: " + str(fruit_list))
# examples go here
```

Example Running the code: 

```python
>>> python3 fruit_pluralizer_lab.py
Single Fruit: ['apple', 'berry', 'melon']
No longer single Fruit: ['apples', 'berries', 'melons']

```

### Hint
Remember that you can index into string and get the length of a string. So use that to get the last letter of a word. 

## Part 2
Create a function my_reverse which will return a reversed string.

1. Create the function contract for my_reverse
2. provide a few examples to confirm that my_reverse works
	* an empty string
	* a string of even length
	* a string of odd length greater than 1
	* a string of length 1 

### Example
Example of the file: 

```python
# contract goes here
def my_reverse(string_to_reverse): 
	# your code goes here
reversed = my_reverse("apples")
print(reversed)
# examples go here
```

Example Running the code: 

```
>>> python3 my_reverse_lab.py
selppa
```
### Hint
To get the last element:`(len(my_list) -1) -  0`

To get the second to last element: `(len(my_list)-1 ) - 1`

To get the third to last element: `(len(my_list)-1) - 2`


### Bonus!
Create a function `reverse_strings_in_list`. This function will input a list of strings you want to reverse. The function will reverse the strings in the list by calling the `my_reverse` function in a loop.