# Lesson 4.03: Nested For Loops

## Learning Objectives

Students will be able to...

* Define and identify: **nested for loops**, **stack trace**.
* Use nested loops via a function and a `for` loop.
* Use nested `for` loops via an outer loop containing an inner loop.
* Use a stack trace to understand and demonstrate the flow of nested `for` loops.

## Materials/Preparation

* [4.03 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/slidedecks/Intro%20Python%204.03%20TEALS.pptx)
* [Do Now][]
* [Lab - Nested For Loops][] ([docx][]) ([pdf][])
* [Lab - Caesar Cipher][] ([docx][https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/03_lesson/lab_caesar.docx]) ([pdf][https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/03_lesson/lab_caesar.pdf])
* Read through the Do Now, lesson, and lab so that you are familiar with the requirements and can assist students.
* Video Explanation of nested `for` Loops.
  * [Nested Loops](https://youtu.be/fyP4SXpkYG4)

### Day 1 Pacing

| **Duration** | **Description** |
| ----------   | -----------     |
| 5 Minutes    | Do Now          |
| 10 Minutes   | Lesson          |
| 35 Minutes   | Lab             |
| 5 Minutes    | Debrief         |

### Day 2 Pacing

| **Duration** | **Description** |
| ----------   | -----------     |
| 5 Minutes    | Do Now          |
| 10 Minutes   | Review          |
| 35 Minutes   | Lab             |
| 5 Minutes    | Debrief         |

## Instructor's Notes

### 1. Do Now

* Display the Do Now on the board.
* Students use nested `for` loops to create a square star pattern.

### Lesson

#### Go over part 1 of the Do Now

* Discuss the output of the program - were the students able to guess the output without typing it?
* Go over how to read `for` loops if students are struggling.
* Make sure students are understanding loops and string concatenation.
* If students continue to struggle, take 5 minutes to go over the loop syntax and practice.

#### Go over part 2 of the Do Now

* Ask a student to write the `print_star_square` function on the board.
* Define **nested for loop**:  a loop within another loop.
* For each iteration of the outer loop, the inner loop is iterated through completely.
* Draw a diagram (**stack trace**) of the `for` loop.
* Ask students to draw the nested part of the state diagram (should be inside the outer loop but look the same as the outer loop)

#### Go over part 3 of the Do Now

* If students were unable to finish this, give them 5 minutes to practice in groups before calling them back to go over this part.
* Ask a couple of students to write on the board how they did this.
* Ask them how treating the loop as its own function made it easier or harder.
* Ideally this should make it easier as a way of abstracting knowledge of looping.

### 3. Lab

* The pattern lab asks students to write functions that produce different outputs using nested `for` loops.
* The Caesar cipher lab asks students to write a simple letter rotation function which enciphers letter-by-letter, necessitating nested `for` loops.

### 4. Debrief

* Inform students that there will be a Unit 4 Quiz after Lesson 4.04.
* Go over common questions the students had.
* On the second day, if time allows, go over the bonus lab problem and discuss how students solved the problem.

### Accommodation/Differentiation

* If students need extra time for lab, there is another day in the schedule for that.
* This topic is often confusing for students new to the concept, so build in time for frequent individual checks for understanding.
* **Bonus Lab Problem** This is a bit more difficult and should provide a challenge for students who are moving more quickly.

[Do Now]: do_now.md
[Lab - Nested For Loops]: lab.md
[Lab - Caesar Cipher]: lab_caesar.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/03_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/03_lesson/lab.docx
