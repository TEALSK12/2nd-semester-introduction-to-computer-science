# Lesson 2.06: Lists 2

##Learning Objectives
Students will be able to... 
* Define and identify: slice, item, index, integer
* Be able to access items from a list using index
* Create lists of different types
* Use the length function

##Materials/Preperation
* [Do Now Handout]
* [Lab]
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| Duration   | Description |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Note
1. Lesson
  1. Ask students what a list is? 
    1. a list is a sequence of values. In a list, they can be any type. The values in a list are called elements or sometimes items.
    2. to create a list enclose items in square brackets
    3. Ask students what values items in a list can be? Answer any type! You can even have lists within lists (more on that later...)
  2. Ask students what len does? 
  3. Ask students how they tried to print the first item from a list? Was this what they were expecting? 
    1. index: a map from the position in the list to the element stored there. 
    2. 0-index: lists are 0 indexed. So the first element in the list is at the 0-index
    3. out-of-bounds: what happened when you tried to index into a list that was too long?
  2. Break for students to practice creating lists. Ask them how they would get the last item in a list. (Hint use the length function!) 
  3. Ask students to write on the board how they got the last element of a list. Ask another student to write how they would get the second to last element of the list and so on. 
  4. After accessing this element you can change it. Practice this in class. 
2. Lab
    1. Practice accessing and updating items in a list
    2. Implement program from last lab using lists
    3. Create a quiz program
3. Opportunities for more
    1. If students are moving quickly, start topic of nested lists. Start of with a simple nested list like `['a', 'b', 'c', [1, 2, 3]]`. Ask the students to guess the length. Ask the students to guess how they would access the item '1' from that list! 
  

[Do Now Handout]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/do_now_206.html
[Lab]: https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/lab_206.html