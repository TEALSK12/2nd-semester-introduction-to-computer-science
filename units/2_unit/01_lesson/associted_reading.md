## Associated Reading

#Variables, expressions and statements

##Values and types

A value is one of the basic things a program works with, like a letter or a number. The values we have seen so far are `1`, `2`, and `'Hello, World!'`.

These values belong to different types: 2 is an integer, and `'Hello, World!'` is a string, so-called because it contains a “string” of letters. You (and the interpreter) can identify strings because they are enclosed in quotation marks.

If you are not sure what type a value has, the interpreter can tell you.
```
>>> type('Hello, World!')
<type 'str'>
>>> type(17)
<type 'int'>
```
Not surprisingly, strings belong to the type str and integers belong to the type int. Less obviously, numbers with a decimal point belong to a type called float, because these numbers are represented in a format called floating-point.

```
>>> type(3.2)
<type 'float'>
What about values like '17' and '3.2'? They look like numbers, but they are in quotation marks like strings.
>>> type('17')
<type 'str'>
>>> type('3.2')
<type 'str'>
```
They’re strings.
When you type a large integer, you might be tempted to use commas between groups of three digits, as in 1,000,000. This is not a legal integer in Python, but it is legal:
```
>>> 1,000,000
(1, 0, 0)
```
Well, that’s not what we expected at all! Python interprets 1,000,000 as a comma-separated sequence of integers. This is an example we have seen of a semantic error: the code runs without producing an error message, but it doesn’t do the “right” thing.

## Exercises

####Exercise 1  
Assume that we execute the following assignment statements:
```
width = 17
height = 12.0
delimiter = '.'
```
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
* `width/2`
* `width/2.0`
* `height/3`
* `1 + 2 * 5`
* `delimiter * 5`

Use the Python interpreter to check your answers.
#### Exercise 2  
Practice using the Python interpreter as a calculator:

The volume of a sphere with radius r is 4/3 π r3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?