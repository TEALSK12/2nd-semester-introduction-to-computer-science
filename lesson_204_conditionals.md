# Lesson 2.04: Conditionals

##Learning Objectives
Students will be able to... 
* Define and identify: if, else, elif, conditionals, flow of control 
* Create chaining if statements
* Understand how conditional statements alter flow of control of the program

##Materials/Preperation
* [Do Now Handout]
* [Lab]
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| Duration   | Description |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Note
1. Have students work on the Do Now
2. Lesson
  1. Ask students if they had trouble on the do now? 
    1. What did they feel like the needed? 
    2. In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability. The simplest form is the if statement. The boolean expression after `if` is called the condition. If it is true, then the indented statement gets executed. If not, nothing happens.
    ```
    if x > 0: 
        print("x is positive")
    ```
  2. Write out the syntax of if statement on the board. Point out: the Boolean expression(condition), the colon, and the tabbing. 
  3. Ask students if they recall what else went along with the if statement.(else) 
    1. else is used when there are two possibilities and the condition determines which one gets executed
    2. show the syntax of the else
  4. Describe the elif statment
    1. Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a chained conditional:
    2. Show the syntax of elif
3. Lab
    1. Convert the triangle program written in snap into python 
    2. Write a program that simulates a list index using if statements. 
4. Opportunities for more
    1. If students are moving quickly, this lesson can move onto lists. 

[Do Now Handout]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/do_now_204.html
[Lab]: https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/lab_204.html