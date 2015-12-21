# Lesson 2.06: Lists 2

##Learning Objectives
Students will be able to... 

* Define and identify: **slice, append, remove, nested list**
* Slice a list
* Add and remove elements from a list
* Access items from a nested list

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading - section 2.5 of Book
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Notes
1. Lesson
  1. Ask students what doing `a[0:2]` did? 
    1. slicing: a list operation that gives back a list starting from the index to the left of the colon and going up to the index to the right of the colon. 
        * Note that slicing doesn't exist in SNAP
    2. Ask what the list would return if you did `a[1:2]`?
    3. What does `remove` do? What does `pop` do? What were the differences. 
    4. Ask students what the plus sign does? What does append do? What would happen if you did `append([1, 2, 3])`?
    5. Nested List: a list that is contained within another list. Only counts as 1 element
        1. Ask Students the length of this nested list? 
        2. Ask students how would we get the length of the inner list
    6. Asks students to write down how they would represent a tic-tac-toe board using lists. Create a tic-tac-toe board with students in class. 
2. Lab
    1. Have students practice slicing, adding, removing elements from some given lists. 
    2. Tic-Tac-toe single move
3. Opportunities for more
    1. If students are moving quickly, start topic of while loop as the game loop 
    2. Keeping score for game
    3. If students are moving slowly then spend an extra day reviewing. Also opportunity for a quiz after the game loop lesson and before the project. 
  

[Do Now]:do_now.md
[Lab]:lab.md