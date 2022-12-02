# Lesson 3.03: Return vs Print

## Learning Objectives

Students will be able to...

* Define and identify: **return**, **None**.
* Explain and demonstrate the difference between printing and returning.

## Materials/Preparation

* [3.3 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/3_unit/slidedecks/Intro%20Python%203.03%20TEALS.pptx)
* [Do Now][]
* [Lab - War (Card Game)][] ([docx][]) ([pdf][])
* [Associated Reading](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/3.3)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.
* Video Resources
  * [Parameterized Functions](https://youtu.be/sKW-zdYZNX4)
  * [Parameterized Function Demo](https://youtu.be/LtKAXFRtxhQ)

## Day 1 Pacing

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes  | Debrief     |

## Day 2 Pacing

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 40 Minutes | Lab         |
| 5 Minutes  | Debrief     |

## Instructor's Notes

### 1. Do Now

* Students experiment with a function that returns a value, but they must add a print command to output that value.

### 2. Lesson

* Ask students about what they think the difference between returning and printing is.

#### Student Sharing

* Get a volunteer to describe how they rewrote the code in the Do Now to get a value output.
* Ask a student to write the code on the board.

#### Discussion

* Discuss the concept of the function contract again, explaining that the functions we will work with have both inputs and outputs.

#### Building a Structure Activity

1. One student volunteer represents the `give_card` function.
2. This students holds the deck of cards and stands by the board.
3. On the board display the `give_card` function in code that only **prints** the value of a randomly chosen card.
4. Students 'call' the student and request cards, which then the student follows the instructions and draws ('prints') the card on the board.
5. Display a new `give_card` function that **returns** a card instead.
6. Have students 'call' the function, however this time have the `give_card` student pass out the card when a student calls him/her.
7. Debrief the activity and talk about what was learned.

### 3. Lab

* Students will create a basic calculator.

### 4. Debrief

* Check student progress and completion of the lab, wrap up by taking any final questions.

## Accommodation/Differentiation

The optional bonus functionality mentioned in the lab is to add the additional code to allow players to start a new 'War' game at the end of the current game.  As an extension activity, ask students to research the shuffle function and the functions associated with it.

[Do Now]:do_now.md
[Lab - War (Card Game)]:lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/3_unit/03_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/3_unit/03_lesson/lab.docx
