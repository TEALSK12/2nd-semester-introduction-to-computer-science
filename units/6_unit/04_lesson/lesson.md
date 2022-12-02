# Lesson 6.04: Dictionaries Looping

## Learning Objectives

Students will be able to...

* Use loops to traverse through key/value pairs in a dictionary.

## Materials/Preparation

* [6.04 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/slidedecks/Intro%20Python%206.04%20TEALS.pptx)
* [Do Now][]
* [Lab - Dictionaries Looping][] ([docx][]) ([pdf][])
* [Associated Reading](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/6.4)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief     |

## Instructor's Notes

### 1. Do Now

* Display the Do Now on the board.
* Students apply the `.keys()` method and investigate the type produced.

### 2. Lesson

#### Discuss part 1 of the Do Now

* Ask students what type was returned.  

#### Discuss part 2 of the Do Now

* Ask for a small number of students to write their solution on the board.
* Discuss that it is possible to do just `for key in my_dictionary:`, but behind the scenes this is similar to calling the `.keys()` function.
* Before Python 3.5-3.7, unlike lists, dictionaries had no guaranteed order:  looping through a dictionary might produce items in a different order from the order in which the items were originally added. In Python 3.7+, dictionaries do preserve order.

### 3. Lab

* Students will rewrite their word count lab (Lab 6.02) to return the top 5 most frequently occurring words.

### 4. Debrief

* Take a moment to discuss any common areas of confusion or challenge that came up during the lab.
* Talk about how `in` works for dictionaries for the bonus.

## Accommodation/Differentiation

Students that are moving quickly can explore sorting additionally in the bonus activity.
Some students may need a second class period to complete this lab.

[Do Now]: do_now.md
[Lab - Dictionaries Looping]: lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/04_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/04_lesson/lab.docx