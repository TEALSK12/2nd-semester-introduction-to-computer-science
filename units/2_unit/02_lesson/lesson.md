#Lesson 2.02: Data Types & Casting

##Learning Objectives
Students will be able to... 
* Define and identify: **type, string, casting, floating point number (float), integer**
* Describe different representations of data in Python 
* Convert from one data type to another data type

##Materials/Preparation
* [Do Now]
* [Lab - Casting]
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes
1. **Do Now** 
  * Project the Do Now on the board, circulate around the class to check that students are working and understand the instructions. 
2. **Lesson**
  * Ask students to define **type**. Talk about types as a way to represent data (give examples of strings, ints, and floats).
  * Ask students what they thought typing the command str(123) does. 
    * Define this process of changing data types as **casting**. 
  * Ask students what they did to cast string into an integer. 
    * Define the int function if the students were unable to guess it from the do now.
  * Take a few minutes to have students write down how they would produce the following output:
    ```
    > 
    Give me a number you want to multiply by 2: 4
    8
    => None
    ```
  * Call on students to write their answers on the board. 
  * Discuss what would happen if the user types in 1.5 instead of 4. 
    * If input is a float, can cast with float(num)
  * `type`: ask students what they think `type('a')` would output.  
    * Why might you want to use `type`?
3. **Lab**
    * Practice predicting what casting will do to inputs. 
    * Create a halving program as well as program that halves to whole numbers. 

###Accommodation/Differentiation
If students are moving quickly, it is possible to introduce the concepts of booleans here. Discuss how students would represent binary (0's and 1's). In practice these translate to True and False. Convert numbers to boolean, and booleans to numbers.
  

[Do Now]:do_now.md
[Lab - Casting]:lab.md