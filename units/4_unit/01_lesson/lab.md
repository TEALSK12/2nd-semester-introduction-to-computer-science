# Lab 4.01 - de_vowel

## Remove the Vowels
Create a function, `de_vowel`, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 

1. Create the function contract for `de_vowel`. 
2. Write `de_vowel` using a for each loop 
3. provide a few examples that confirm de_vowel works as expected
	* what if the string is all vowels
	* what if there are no vowels
	* what if there is a mix of vowels and non-vowels and spaces
	
### Example
Example of the file: 

```python
# contract goes here
def de_vowel(a_string): 
	# your code goes here
no_vowels = de_vowel("This sentence has no vowels")
print(no_vowels)
# examples go here
```

Example Running the code: 

```python
>>> python3 de_vowel_lab.py
Ths sntnc hs n vwls
```

### Bonus!
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function `count_vowels`. 

`count_vowels` takes in a string and returns an int representing the number of vowels in the string. 
