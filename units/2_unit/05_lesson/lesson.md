# Lesson 2.05: Lists

## Learning Objectives
Students will be able to... 
* Define and identify: **list, item, index, integer**
* Be able to access items from a list using the index
* Create lists of different types
* Use the length function

## Materials/Preparation
* [Do Now]
* [Lab - College Chooser]
* Solution (access protected resources by clicking on "Additional Curriculum Materials" on the [TEALS Dashboard])
* Associated Reading - section 2.4 of Book
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes

1. **Do Now**
    * Students follow instructions to create lists and use the `len` function. 
2. **Lesson**
  * Ask students to recall what a list is, and how lists were used in Snap!
    * A **list** is a sequence of values. In a list, they can be any type. The values in a list are called elements or **items**.
    * In Python, to create a list you must enclose items in square brackets.
    * Emphasize that you can have lists of any type (int, float, string, etc). You can even have lists within lists (more on that later...)
    * Remind students of lists in Snap! 

    ![lists in snap](http://bjc.edc.org/bjc-r/img/3-lists/wordlists.png)
  * Ask students what `len` does when they used it in the Do Now. 
  * Ask students how they tried to print the first item from a list. Was this what they were expecting? 
    * **index**: a map from the position in the list to the element stored there. 
    * 0-index: lists are 0 indexed. So the first element in the list is at the 0-index
    * Out-of-bounds: what happened when you tried to index into a list that was too long?
    * Snap Equivalent: ![snap indexing](http://bjc.edc.org/bjc-r/img/3-lists/gs5how_many.png)
    * Ask students how they would access the last item in a list of unknown length. (Use the length function!) 
        * Ask students to write on the board how they got the last element of a list. Ask another student to write how they would get the second to last element of the list and so on. 
    * After accessing any list element you can change it. Take a moment to demonstrate this syntax before starting the lab. 
    * Video Explanation of Lists

    [![Video Explanation of Lists](https://img.youtube.com/vi/wO6lG82RbhM/0.jpg)](https://youtu.be/wO6lG82RbhM?t=67)
       
3. **Lab**
    * Practice accessing and updating items in a list
    * Implement program from last lab using lists
    * Create a quiz program
4. **Debrief**
    * Check student progress and completion of the lab, wrap up by taking any final questions.

### Accommodation/Differentiation
If students are moving quickly, you can introduce the topic of nested lists. Start off with a simple nested list like `['a', 'b', 'c', [1, 2, 3]]`. Ask the students to guess the length. Ask the students to guess how they would access the item '1' from that list! 

## Forum discussion
[Lesson 2.05: Lists (TEALS Discourse Account Required)](https://forums.tealsk12.org/c/2nd-semester-unit-2/lesson-2-05-lists)
  
[Do Now]:do_now.md
[Lab - College Chooser]:lab.md
[TEALS Dashboard]:http:/www.tealsk12.org/dashboard
