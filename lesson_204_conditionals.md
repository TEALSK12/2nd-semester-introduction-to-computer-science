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
  2. Write out the syntax of the if statement on the board point out the boolean expression called the condition, the colon, and the tabbing. 
  3. Ask students if the recall what else went along with the if statement.(else) 
    1. else is used when there are two possibilities and the condition determines which one gets executed
    2. describe the syntax of the else
  4. Describe the elif statment
    1. Sometimes there are more than two possibilities and we need more than two branches. One way to express a computation like that is a chained conditional:
1. Ask Students about the difference between `=` and `==`. 
    1. = is a setter for variables 
    2. == builds a boolean expression
  2. Show Students boolean expressons in SNAP. 
    ![Snap boolean Expressions](snap_boolean_expressions.png)
    Ask the students to recall what and, or and not did.
  3. Give a little bit of time for the students to do finish complementing part 2 of the assignment 
  4. Have a student write up the expression they used to update the `can_get_license` code.
    1.Poll students- how many boolean expressions are used? Answers here can vary but ~7 (age >= 16, age <18, driving_with_permit >=6, and expression, age > 18, or expression, whole expression) 
    2. Define composition: Using an expression as part of a larger expression, or a statement as part of a larger statement. You can use parenthesis to compose expressions as well
  5. Parenthesis: In SNAP! to compose many expressions they were nested together. In snap you can just put them one after another. However if you want certain things to evaluated together use parenthesis
3. Lab
    2. Evaluate expressions with `and`, `or`, and `not`
    2. Given written out rules, and turn them into Boolean Expressions
    3. Create a large expression using variables that describes you. 
4. Opportunities for more
    1. If students are moving quickly, opportunity to go over truth tables (or ask them to think about De Morgan's Law) 
  

[Do Now Handout]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/do_now_204.html
[Lab]: https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/lab_204.html