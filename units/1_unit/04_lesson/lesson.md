# Lesson Plan 1.04: Variables and User Input

## Learning Objectives

Students will be able to...

* Define and identify: **comments,  storing, mutability, variable assignment, input**.
* Assign and swap variables.
* Store user input into a variable.

## Materials/Preparation

* [1.04 Slide Deck](https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/1_unit/slidedecks/Intro%20Python%201.04%20TEALS.pptx)
* [Do Now][]
* [Lab - Magic Genie][]  ([docx][])([pdf][])
* [Associated Readings 1.3](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/1.3)
* Read through the Do Now, Lab, and lesson so that you are familiar with the requirements and can assist students.
* Video Resources:
  * [Numeric Data Types](https://youtu.be/5yhn0MFLcu8)
  * [Numeric Data Types Demo](https://youtu.be/T1j2tfZK7OI)

## Pacing Guide

| **Duration**   |     **Description**    |
| ---------- | ------------------ |
| 5 Minutes  | Do Now             |
| 20 Minutes  | Continue Do Now & Discussion |
| 20 Minutes | Magic Genie Lab|
| 10 Minutes | Debrief/Quiz Prep         |

## Instructor's Notes

### 1. Do Now

* Project the Do Now on the board, circulate around the class to check that students are working and understand the instructions.
* Only allow 5 minutes. additional time may be given if the instructor feels it is necessary.

### 2. Do Now Work & Discussion

* Hold a discussion with students on `input`.
* Discuss answers to the questions written in the Do Now.
* Explain that **comments** are not executed by the interpreter.

#### Discussion

1. What did `input` do?
2. What did the string between the parentheses do?
3. What would changing that string do? (it changes the prompt given to the user)

#### Instruction

* Define **input**: user data given to the app.
* Explain that in Python `input` lets a program take input from the console and use it in the code.

#### Student Sharing

* Call some students up to write their answers on the board.

#### More Instruction

* Practice changing the argument to input function in class. (ex. How would you have the computer ask what month the students were born in?)
* Python 3 is strongly typed.  `input` returns a string.
* Demonstrate by typing in the following:

```python
n = input()
9
type(n)
<class 'str'>
```

* Have students write answers on the board, or call on students to give you answers line by line and you write the code on board or type out.
* Discuss the idea of setting variables to be other values.
* What would happen if you don't store a into c in this program?
* **Mutability**: you can change an existing value.

### 3. Magic Genie Lab

* Make sure students feel comfortable saving things as variables and can print multiple things.
* Troubleshoot with students and try to recognize early which students are struggling.

### 4. Debrief/Quiz Prep

* Discuss any issues that came up in the magic genie program.
* Were there any error messages? What do they mean?
* Did anyone use more than one variable?
* Review concepts so far: **variables, interpreter, console, string, integer, float, run, output, variable swapping**

### Accommodation/Differentiation

Advanced students that are finished early can be paired with students who are struggling. Be careful to give clear guidance about how to effectively help another student, especially emphasizing that helping *never* involves using someone else's keyboard/mouse.

Identify students that may potentially struggle on the quiz and find individual time with them to emphasize key concepts during the magic genie lab.

[Do Now]:do_now.md
[Lab - Magic Genie]:lab.md

[pdf]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/1_unit/04_lesson/lab.pdf
[docx]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/1_unit/04_lesson/lab.docx
[Comments Video]: https://youtu.be/kEuVvUc1Zec
