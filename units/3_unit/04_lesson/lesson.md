# Lesson 3.04: Debuging and Scope

##Learning Objectives
Students will be able to... 
* Define and identify: **scope, aliasing, stack trace**
* Understand that changing a list in a function updates the list outside of the function
* Understand that updating variables in a function does not affect the variable outside of the function. 
* Draw a simple stack trace

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading - section 3.4 of Book
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Debrief  |

## Instructor's Notes
1. **Do Now**
2. **Lesson**
    * Ask students if they had trouble on the do now? 
        * what happened to the list? 
        * Explain concept of *aliasing*. Draw out the var pointing to a list. Passing the location of a list, not the actual value so the list can be changed. 
   2. Scope of functions
   	1. Variables in functions are the arguments and the ones you define in the function. Variables from outside the function can be used, but they can't be set. Normally hold values that don't change. 
   	2. Explain the Stack Diagrams used by the book (this is in this seciontes associated reading)
   	3. Point out the error messages that will occur if you use a variable out of it's scope
   3. Debugging
   	1. Help students follow their program to understand how the code is working
   	2. Use of print statements to let you know where in the code you are
3. Lab/Review
    1. Covers topics from past two units students are struggling with 
    2. There is also a worksheet  
4. Opportunities for more
    1. If students are moving quickly, they can look at the project spec

[Do Now]:do_now.md
[Lab]:lab.md