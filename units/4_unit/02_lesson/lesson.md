# Lesson 4.02: For Loops Using Range

## Learning Objectives

Students will be able to...

* Define and identify: **range**.
* Use the `range` and `len` function to to update lists via for loops.

## Materials/Preparation

* [4.02 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/slidedecks/Intro%20Python%204.02%20TEALS.pptx)
* [Do Now][]
* [Lab - Getting Loopy][] ([docx][]) ([pdf][])
* [Associated Reading](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/4.2)
* Read through the Do Now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide

| **Duration** | **Description** |
| ----------   | -----------     |
| 5 Minutes    | Do Now          |
| 10 Minutes   | Lesson          |
| 35 Minutes   | Lab             |
| 5 Minutes    | Debrief         |

## Instructor's Notes

### 1. Do Now

* Display the Do Now on the board.
* Students experiment with and are introduced to the `range` function.

### 2. Lesson

#### Part 1 of the Do Now

* Ask students what the `range` function did.
* Remind them that there are reference docs online.
* Show the docs for the range function. Note that it can take in a third value that is optional.
* Work together with the students to write a `for` loop using the `range` function.

#### Part 2 of the Do Now

* Ask the students what happened
* Ask the students why these values might be helpful
* They are a list of the indices!

#### Part 3 of the Do Now (many students likely didn't finish)

* Ask students to write the first line of the loop on the board
* Work together as a class to come to a solution that is demonstrated for all to see.

#### Debugging Loops

In the sample "Function Contains Two Errors" code, we expect the return value `True`, but we get an IndexError instead.

Suggest printing the values of the indices immediately before the line where the error appears (right after while statement). 

First error: the index of the last character is `3`, so the initial value for `j` should be different:
`j = len(word2)-1`.

Second error: we need to include the character at index 0, so we need to change the `while` condition:
`while j >= 0:`

### 3. Lab

* Students re-write the fruit pluralize program from yesterday's do now, but without creating a new list.
* Students write a function that reverses the letters in a string.

### 4. Debrief

* Talk about any issues the students had with the lab today.
* Discuss how lists are mutable, so you don't have to return a new value. Instead, the list is just updated as the loop runs.

#### Video explanation on Python Lists being Mutable

[![Mutable Python Lists](https://img.youtube.com/vi/_y3PqL4lIzw/0.jpg)](https://youtu.be/_y3PqL4lIzw?t=181)

## Accommodation/Differentiation

* If students are having a hard time with the fruit pluralize, consider altering the fruit program to not allow fruit that ends in y.
* Some students may have issues with grabbing the last item of a string, consider providing tips or scaffolding for students that are struggling with this.
* Go over the bonus question if any students got to it. Discuss having a function inside of the loop and how that operated.

[Do Now]: do_now.md
[Lab - Getting Loopy]: lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/02_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/02_lesson/lab.docx
