# Lesson 2.02: Booleans & Expressions

## Learning Objectives

Students will be able to...

* Define and identify: **Boolean, expression, composition, True, False**.
* Evaluate a Boolean expression.
* Compose Boolean expressions using `and`, `or`, `not`, `<`, `>`, and `==`.

## Materials/Preparation

* [2.02 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/slidedecks/Intro%20Python%202.02%20TEALS.pptx)
* [Do Now][]
* [Lab - Can I or Can't I?][] ([docx][]) ([pdf][])
* [Associated Readings 2.2](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/2.2)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes

### 1. Do Now

* Project the Do Now on the board.
* Circulate around the class to check that students are working and understand the instructions.

### 2. Lesson

#### Discussion

* Ask students what values they saw in part 1 of the Do Now (answer should be `True` or `False`).

#### Instruction

* A **Boolean expression** is an expression that evaluates to either `True` or `False`.
* Ask Students about the difference between `=` and `==`.
* `=` is for assignment of value.
* `==` builds a Boolean expression and is a way to compare two values.
* Give students additional time to finish completing part 2 of the Do Now, if needed.
* Have a student write up the expression they used to update the `can_get_license` code.
* Discuss with students part 3 and 4 of the Do Now and how `or` is used two different ways.  A Boolean value `or` a string value is most often a mistake, not intended syntax. Reinforce with students that `animal == 'cat' or 'dog'` in Python will not produce the result that might be expected.

#### Poll students -

* How many Boolean expressions are used?

For example, Part 3 shows one assignment, and then a composite expression made up of two simple Boolean expressions.

#### Instruction Part 2

* Define **composition**: Using an expression as part of a larger expression, or a statement as part of a larger statement. You can use parentheses to compose expressions as well.
* Parentheses: If you want certain things to be evaluated together, use parentheses.

### 3. Lab

* Evaluate expressions with `and`, `or`, and `not`.
* Given written out rules, students will convert them into Boolean expressions.
* Create a large expression using variables that describes you.

### 4. Debrief

* Check student progress and completion of the lab, wrap up by taking any final questions.

## Accommodation/Differentiation

If students are moving quickly, use this opportunity to go over truth tables (or ask them to research De Morgan's Law).

[Do Now]:do_now.md
[Lab - Can I or Can't I?]:lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/02_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/02_lesson/lab.docx
