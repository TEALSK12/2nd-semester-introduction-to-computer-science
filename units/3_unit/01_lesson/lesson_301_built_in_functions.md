# Lesson 3.01: Built-In Functions

##Learning Objectives
Students will be able to... 
* Define and identify: **function, abstraction, arguments, calling, importing, returning**
* Call the built-in `randint` function, using arguments
* Utilize code other people have written
* Understand the difference between printing and returning

##Materials/Preparation
* [Do Now]
* [Lab]
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes
1. **Do Now**
    * Give students 3-4 minutes to follow the instructions on the Do Now page.
    * Debrief the answers to the questions on the Do Now by calling on students to respond.
2. **Lesson**
    * Build Your Own Blocks vs Functions
 	    * Ask students to recall how they built custom blocks in Snap!
 	    * *Function*: named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “*call*” the function by name. We have already seen one example of a function call
        * Explain that we have already gotten used to calling functions like `type()` and `print()`
    * Ask students how they would create a random number generator. 
        * Luckily someone has already done that: random library (essentially a bunch of code written by someone else) with many functions. 
        * How to get a random integer: randint(0, 10)
            * Identify the 0 and 10 in this example as *arguments*, or values passed into the function.
  		    * Ask students what the argument is when we use `print` or `type`
  		    * `randint` gives back a value that you might want to store - this is called *returning*. If nothing is given back, the return value is `None`
    * Contract
        * Functions have a contract, you write down the arguments, their type, and the return type expected 
            * Ask students what the contract of `randint` is?
            * Since `randint` is written by someone else there is a place where that contract is written out. `Documentation`. Have students go to computer and read the docs for random.
 
3. **Lab**
    * Practice importing different random functions and using them
    * 8 ball 

4. **Debrief**
    * Check student progress and completion of the lab, wrap up by taking any final questions. 

###Accommodation/Differentiation
If students are moving quickly, find another library to import from OR allow students to move on to creating their own functions


[Do Now]:do_now_301.md
[Lab]:lab_301.md