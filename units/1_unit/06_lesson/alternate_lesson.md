# Alternatve Project 1: Magic Square
Created by Brian Weinfeld

Using Python, students will use variables, input, and printing to create a Magic Square. You will also practice *designing* a project by planning out your Magic Square before implementing it.

## Overview

Pick a number from 21-65. __42__, you say? OK! Check this out!

```
22 01 12 07
11 08 21 02
05 10 03 24
04 23 06 09
```

If you add up all the numbers in each row, they total 42.

If you add up all the numbers in each column, they total 42.

If you add up all the numbers in each diagonal, they total 42.

It is the same for each of the four corners, and each 2x2 block as well.

This is called a __Magic Square__ and for this project, you are going to create a program that lets users select a number and create a magic square from that number.

## Details

### Behavior

* The program begins by asking the user to input a number from 21 to 65.

    ```
      Welcome to Magic Square
      Enter a number from 21 to 65: 42
      You have entered 42
    ```

* The program should then create and display a magic square for that number.

    ```
      Here is your Magic Square:
      
      22 01 12 07
      11 08 21 02
      05 10 03 24
      04 23 06 09
    ```

### Implementation Details

Believe it or not, Magic Squares are not difficult to make! Watch the following video to see how to make a Magic Square for any given number: https://www.youtube.com/watch?v=aQxCnmhqZko

### Challenge

This section contains additional components you can add to the project. These should only be attemped __after__ the project has been completed.

* What happens if the user enters a number outside the range of 21-65? Try to check for this and print an error message!

* What happens if the user doesn't enter a number at all and enters a word instead? Try to check for this and print an error message!

* Build a Magic Square with a small number like 22. The Magic Square isn't aligned properly and hard to read. Try to fix this!

## Solution

```python
print('Welcome to Magic Square')

magic_number = int(input('Enter a number from 21 to 65: '))
print('You have entered ' + str(magic_number))

print('Here is your Magic Square: ') 
print(str(magic_number-20) + ' 01 12 07')
print('11 08 ' + str(magic_number-21) + ' 02')
print('05 10 03 ' + str(magic_number-18))
print('04 ' + str(magic_number-19) + ' 06 09')

#extensions

print('Welcome to Magic Square')

magic_number = input('Enter a number from 21 to 65: ')
if not magic_number.isdigit():
  print('Please enter a number')
elif not(21 <= int(magic_number) <= 65):
  print('Please enter a number from 21 to 65')
else:
  print('You have entered ' + magic_number)
  magic_number = int(magic_number)

  print('Here is your Magic Square: ')
  print(str(magic_number-20).zfill(2) + ' 01 12 07')
  print('11 08 ' + str(magic_number-21).zfill(2) + ' 02')
  print('05 10 03 ' + str(magic_number-18).zfill(2))
  print('04 ' + str(magic_number-19).zfill(2) + ' 06 09')
 ```

## Grading

TO BE UPDATED

### Scheme/Rubric

| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| Program greets user and explains rules  | 3   |
| Program accurately requests 10 words (1 for word, 1 for correct request)| 20|
| Program prints full Mad Lib | 10   |
| Program exhibits creativity               | 2   |
| **Sub total**                                                   | 35  |
| **Technical Correctness**                                    |     |
| Program utilizes variable names to convey meaning               | 5  |
| Correct order of inputted words                                 | 10  |
| Only 3 print statements                                         | 10  |
| **Sub total**                                                   | 25  |
| **Total**                                                       | 60 |
