# Do Now 6.02

1.Type and run the following code in the interpreter: 

```python
my_dictionary = {
'kittens': 'cute animals'
}
my_dictionary['kittens'] = 'p. cute'
print(my_dictionary)
```
Write down what the 2nd line does.


2.Type and run the following code in the interpreter: 

```python
my_dictionary = {}
my_dictionary['puppies'] = 'baby dogs'
print(my_dictionary)
```
Write down what the second line does. 

3.Type and run the following code in the interpreter: 

```python
my_dictionary = {
'kittens': 'cute animals',
'puppies': 'baby dogs'
}
my_dictionary.pop('kittens')
print(my_dictionary)
my_dictionary.pop('bunnies')
my_dictionary.pop('bunnies', None)
```
Write down what the second line does. Write down what is different between `my_dictionary.pop('bunnies')` and `my_dictionary.pop('bunnies', None)`?