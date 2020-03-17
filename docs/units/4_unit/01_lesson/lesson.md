# Lesson 4.01: Looping Basics

## Learning Objectives

Students will be able to...

* Define and identify: **for loop**, **item**, **iteration**, **scope**
* Recall looping in Snap! and reapply the concept in Python
* Loop through (traverse) the items in a list
* Be aware of the scope of variables during iteration

## Materials/Preparation

* [Do Now]
* [Lab - de_vowel] ([printable lab document]) ([editable lab document])

* [Associated Reading - section 4.1](https://tealsk12.gitbook.io/intro-cs-2/readings#4-1)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 10 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 5 Minutes | Debrief     |

## Instructor's Notes

### 1. Do Now

* Display the Do Now on the board.
* Students will experience how to use a for loop to efficiently complete a repeated action.

### 2. Lesson

* Go over Part 1 of the Do Now. Ask the students what would happen if the list got much larger?
* If they say they would write down a lot of code, ask how readable that might be, or how long would it take to write, or the greater potential for bugs due to typos.
* Go over part 2 of the Do Now. Ask the students what happened. Ask if they remember something similar from Snap!
* Introduce the **for loop** as a way to deal with issues associated with part 1 of the Do Now.

#### Video Explanation of For Loops

[![For Loops Explanation](https://img.youtube.com/vi/KosrKNJK9Sw/0.jpg)](https://youtu.be/KosrKNJK9Sw)

* From the Code in the Do Now: `for num in list_of_numbers:`
* Emphasize that the body of the for loop is the indented part
* **Iteration**: body of the loop is repeated with different values of the list. Note how the body of the loop is repeated but `num` changes. Consider drawing this out on the board.
* Remind students of the concept of **scope**, showing how `num` changes values with each iteration of the loop.
* Go over Part 3 (many students likely didn't have time to finish). Ask students to write the first line of the loop on the board. Have students brainstorm what the body should be. Come to a group consensus and run the code.  

### 3. Lab

* De-vowel lab: Students will create a function that will take in a sentence and return that sentence without vowels.

### 4. Debrief

* Talk about any issues or challenges the students had with this lab. If there is time, call students up to the board to shown and demonstrate their code/solutions.

## Accommodation/Differentiation

If there is time, go over the bonus question. Explain how a counter is a frequently used tool to keep track of the count of things from outside the loop . Discuss the concept of the counter's scope (counter gets updated in the loop, but doesn't reset automatically at each iteration). Counters can be used with any loop, and are often used with while loops!

## Forum discussion

[Lesson 4.01: Looping Basics (TEALS Discourse Account Required)](https://forums.tealsk12.org/c/unit-4-looping/lesson-4-01-looping-basics)

[Do Now]: do_now.md
[Lab - de_vowel]: lab.md
[printable lab document]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/01_lesson/lab.pdf
[editable lab document]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/01_lesson/lab.docx
