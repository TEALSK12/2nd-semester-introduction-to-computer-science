# Lesson 4.04: Nested Lists & Looping

## Learning Objectives

Students will be able to...

* Define and identify: **nested list**.
* Use nested for loops to traverse through nested lists.

## Materials/Preparation

* [4.04 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/slidedecks/Intro%20Python%204.04%20TEALS.pptx)
* [Do Now][]
* [Lab - Shopping List](lab.md) ([docx][]) ([pdf][])
* Read through the Do Now, lesson, and lab so that you are familiar with the requirements and can assist students.
* Explanation video of Nested Lists.
  * [Nested Loops](https://youtu.be/fyP4SXpkYG4)

### Day 1 Pacing

| **Duration** | **Description** |
| ----------   | -----------     |
| 5 Minutes    | Do Now (Part 1) |
| 10 Minutes   | Lesson          |
| 35 Minutes   | Lab (Part 1)    |
| 5 Minutes    | Debrief         |

### Day 2 Pacing

| **Duration** | **Description** |
| ----------   | -----------     |
| 5 Minutes    | Do Now (Part 2) |
| 10 Minutes   | Lesson          |
| 35 Minutes   | Lab (Part 2)    |
| 5 Minutes    | Debrief         |

## Instructor's Notes

### 1. Do Now (Day 1)

* Display the Do Now on the board.
* Make sure students only work on the first part of the Do Now, as the second part will be for the next lesson.

### 2. Lesson (Day 1)

#### Go over the first problem of the Do Now

* Ask students what type `my_building` is.
* Discuss **nested lists** as lists that have each element as a list. Ask students to think of some other data that might fit into a **nested list**. What about a game of Tic-Tac-Toe or chess?
* Go into depth a bit more on nested lists.
* Ask the students  how they would access different parts of the `my_building` example.
* Write down the syntax of `[][]`.
* In the `my_building` example the first bracket gets you the floor and the second gets you the room.

#### Practice

* Have students practice writing their own nested lists, or work in pairs with one student writing one nested lists and the other student writing another.

#### Go over the second problem in the Do Now

* Ask the students what happened when they iterated over `my_building`.
* As an extension, ask the students how they would print out each `b` apartment.

### 3. Lab (Day 1)

* Students will practice accessing items from lists of lists by creating a schedule program and accessing/updating elements.

### 4. Debrief (Day 1)

* Make sure that all students are able to access elements from a list of lists.

### 5. Lesson (Day 2)

#### Go over the 1st problem of the Do Now

* This should be a review of looping.
  * If students are having trouble, take extra time to review looping syntax and procedures.

#### Go over the 2nd problem of the Do Now

* Ask students to write on the board what they did. Discuss how you would write this without the extra function.
* Go over how to write this program, using student responses.
* As extensions to this discussion, have students consider how they would alter the program to not print out the middle floor. Or how would they alter it to not print out any apartment a's?

### 6. Lab (Day 2)

* Students will create functions that loop through lists of lists.

### 7. Debrief (Day 2)

* Ask students if there was any difficulty looping through lists of lists.
* Remind students there will be a quiz next class covering everything up to (and including) nested lists.

## Accommodation/Differentiation

Students may struggle with the concept of nested lists. Be prepared to have additional analogies to help students understand the usefulness of the concept.

* Example: What if you keep a weekly to-do list? The days of the week would be the first list, and then each item that you hope to accomplish under each day is the list within the list.

[Do Now]: do_now.md
[Lab - Daily Schedule]: lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/04_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/4_unit/04_lesson/lab.docx
