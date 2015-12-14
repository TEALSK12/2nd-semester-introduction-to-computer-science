# Lesson 3.01: Built In Functions

##Learning Objectives
Students will be able to... 
* Define and identify: function, abstraction, arguments, calling, importing, returning
* Call built-in functions, using arguments
* Utilize code other people have written
* Understand printing vs returning

##Materials/Preparation
* [Do Now Handout]
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Notes
1. Lesson
  1. Build Your Own Blocks vs Functions
 	1. Ask students to recall how they built custom blocks
  	2.function: named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function by name. We have already seen one example of a function call
  	3. We have seen functions type, print, etc
  	4. Ask students how they would call.
  		1. Using parethensis
  2. Functions
  	1. Ask students how they would create a random number generator? Luckily somone has already done that: random library (bunch of code written by someone else) with many functions. 
  		1. How to get a random integer: randint(0, 10)
  		2. ask students what they think 0 and 10 are
  		3. arguments: values you give to the function
  		4. have students practice using random, change the arguments and see what happens
  		5. What is the argument to `print` or `type`
  		6. randint gives back a value that you might want to store. this is called returning. If nothing is given back return value is `None`
  	2. Contract
  		1. Functions have a contract, you write down the arguments, their type, and the return type expected 
  		2. Ask students what the contract of `randint` is?
  		3. Since `randint` is written by someone else there is a place where that contract is written out. `Documentation`. Have students go to computer and read the docs for random
 
2. Lab
    1. Practice importing different random functions and using them
    2. 8 ball 
3. Opportunities for more
    1. If students are moving quickly, find another library to import from OR move on to creating their own functions


[Do Now Handout]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/do_now_202.html
