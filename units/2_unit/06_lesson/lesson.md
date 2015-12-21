# Lesson 2.06: Lists 2

##Learning Objectives
Students will be able to... 

* Define and identify: **slice, append, remove, nested list**
* Slice a list
* Add and remove elements from a list
* Access items from a nested list

##Materials/Preparation
* [Do Now]
* [Lab] - Tic-Tac-Toe
* Associated Reading - section 2.5 of Book
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 10 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes
1. **Do Now**
    * Students may need more time than usual to fully go through this lesson's Do Now.
2. **Lesson**
  * Ask students what doing `a[0:2]` in the Do Now did.
    * Define **slicing**: a list operation that gives back a list starting from the index to the left of the colon and going up to the index to the right of the colon. 
        * Note that slicing doesn't exist in Snap!
    * Ask students what the list would return if you did `a[1:2]`.
    * Explore the differences between `remove` and `pop`, asking for student input. 
    * Ask students what the plus sign and `append` do? 
        * What would happen if you did `append([1, 2, 3])` with the last example in the Do Now?
    * **Nested List**: a list that is contained within another list. Note that it only counts as 1 element.
        * Ask students the length of this nested list.
        * Ask students how would we get the length of the inner list
    * Ask students to write down how they would represent a Tic-Tac-Toe board using lists.
    * Create a Tic-Tac-Toe board with students in class. 
3. **Lab**
    * Students practice slicing, adding, and removing elements from some given lists. 
    * Students create a single move Tic-Tac-Toe game

###Accommodation/Differentiation
If students are moving quickly, start topic of while loop as the game loop. Explore the concept of keeping score for the game.

If students are moving slowly then spend an extra day reviewing lists and completing lab activities. 

There is also an opportunity for a quiz after the game loop lesson and before the project. 
  

[Do Now]:do_now.md
[Lab]:lab.md