#Lesson 4.01: Looping Basics

##Learning Objectives
Students will be able to...

* Define and identify: **for loop**, **item**, **iteration**, **scope**
* Recall looping in Snap! and reapply the concept in Python 
* Loop through (traverse) the items in a list
* Be aware of the scope of variables during iteration 

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading - section 4.1 of Book
*  Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief     |

## Instructor's Notes

1. **Do Now**
    * Display the Do Now on the board.
2. **Lesson**
	* Go over Part 1 of the Do Now. Ask the students what would happen if the list got much larger? (if they say they would write down a lot of code. ask how readable that might be. how long would it take to write. what bugs might come up from typos.)
	* Go over part 2 of the Do Now. Ask the students what happened. Ask if they remember something similar from SNAP! And ask how the code would change if they added a 100 items to the list 
	* Introduce **for loop** as a way to deal with issues of part 1. 
		* Syntax: `for num in list_of_numbers:`. body of for loop is the indented part
		* *Iteration*: body of the loop is repeated with different values of the list. Note how the body of loop is repeated but `num` changes. Consider drawing this out on the board. 
		* Remind students of the concept of *scope*, showing how `num` changes values with each iteration of the loop. 
	* Go Over Part 3 (students probably didn't finish). Ask students to write the first line of the loop on the board. Brainstorm what the body should be. Call on students. If struggling write up `multi_fruit.append(single_fruit[0] + 's')` from part 1 into the body of the  and ask a student to change it. Use print statements to show debugging. 
3. **Lab**
	* Count the vowels lab: Students will be given a sentence that they will need to print without vowels. 
4. **Debrief**
	* Talk about any issues. The students had. This is similar to the lab, but with building up a string so there might be some issues with adding back the spaces
	* Go over the bonus question. Explain a counter is frequently used to keep track of count of things from outside the loop . Discuss concept of counter's scope (counter get's updated in the loop, but doesn't reset automatically at each iteration). Counters can be used with any loop. Often used with while loops!



[Do Now]: do_now.md
[Lab]: lab.md