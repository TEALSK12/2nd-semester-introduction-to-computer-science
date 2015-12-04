# Lesson Plan 1.03: Script Mode and Variables

##Learning Objectives
Students will be able to... 
* Define and identify: **script**, **print**, **run**, **output**, **variable**
* Write a simple script and run it in the IDE
* Print values out to the console (both composed values and from variables) 
* Compare script mode vs interactive mode
* Know how to store a value into a variable

## Assessment
* Worksheet with predictions and results

##Materials/Preparation
* [Do Now] - Project on screen
* [Worksheet]
* Read through the Do Now, Worksheet, and lesson so that you are familiar with the requirements and can assist students.

## Pacing Guide
| **Duration**   |     **Description**    |
| ---------- | ------------------ |
| 5 Minutes  | Do Now             |
| 20 Minutes | Printing Lesson/Worksheet Part 1   |
| 20 Minutes | Variables Lesson/Worksheet Part 2   |
| 10 Minutes | Discussion         |

## Instructor's Note
1. **Do Now**
    * Project the Do Now on the board, circulate around the class to check that students are working and understand the instructions. 
2. **Printing Lesson/Worksheet Part 1**
	*	File is the center section of the screen. Sometimes this is called a script.
		1. How do you save/run a file? Ask students what happened when they ran the file from the do now.
		2. Need to use `print` statement. Prints whatever is in between the parenthesis to the console
			1. This is called output
		3. When text appears on console its called output 
		4. What happened when you used multi-lines?
			1. Talk to students about how to read a program. 
	2. Ask students how they would print the following:
	```
Hello World
Hello World
Hello World
Hello World
Hello World
	```
	3. Have students work on printing practice on the worksheet
3. Variables
	1. variable: a name that refers to a value
	2. an assignment statement creates new variables and gives them values: 
	
	```python
	>>> message = 'And now for something completely different'
	>>> n = 17
	>>> pi = 3.1415926535897932
	```
		1. ask the students what they think the assignment operator is. What are the variables, what are the values? 
		2. assignments work from right to left. so item on the right is assigned to item on the left. 
3. Debrief
	1. Talk about the difference between interactive and script mode. Why might you want to use the interpreted mode (can be faster to debug a single line and make sure it works)
	2. Talk about differences between SNAP! and Python for declaring variables.
4. Opportunities for more
    1. If students are moving quickly, have students practice higher order-of-operations problems. Ask students to come up with a way to print two lines with only one print statement. Allow for students to Google the `\n` character. 
  

[Worksheet]:https://teals-introcs.gitbooks.io/2nd-semester-introduction-to-computer-science-pri/content/units/1_unit/03_lesson/lab_103.html
[Do Now]: do_now.md
