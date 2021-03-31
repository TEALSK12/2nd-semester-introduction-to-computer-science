# Do Now 3.04

## Quiz Announcement

We will have a quiz next class covering all of the above topics.

### Discussion

Is there any topic you would like to focus on and cover more of?

### In your notebook

Rank the following from easiest to hardest:

A. Importing built-in functions
B. Using `randint`
C. Abstraction/creating functions
D. Passing `int/str/float/bool` arguments into functions
E. Calling a function
F. List syntax
G. Return vs print

### Type the following into the console

```python
    my_list = ['a', 'b', 'c', 'd']

    # input: a list of strings
    # output: None
    def my_function(list_argument):
        list_argument[0] = 'z'
        print("Inside function: ", my_list)

    print("Before function:", my_list)
    my_function(my_list)
    print("After function:", my_list)
```

1. What did the program output and what is this program doing?

### Bonus

Try writing a similar program but passing in an integer, `my_int`, instead of a list, changing the integer variable inside the function. What happens?

### Do Now, Part 2

In your notebook, without running the following code, predict what its output will be:

```python
    def double_print(input_string):
        for i in range(2):
            print(input_string)
 
    def double_concat(part1, part2):
        concat = part1 + ", " + part2
        double_print(concat)
 
    str1 = "Hello"
    str2 = "world"
    double_concat(str1, str2 + "!")
```