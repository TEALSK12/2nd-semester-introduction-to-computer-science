# Lesson Plan 1.03: Script Mode and Variables

##Learning Objectives
Students will be able to... 
* Define and identify: **script**, **print**, **run**, **output**, **variable**
* Write a simple script and run it in the IDE
* Print values out to the console (both composed values and from variables) 
* Compare script mode vs interactive mode
* Know how to store a value into a variable

## Assessment
* [Lab] with predictions, results, and completed programs

##Materials/Preparation
* [Do Now] - Project on screen
* [Worksheet]
* Associated Reading - section 1.2 of Book
* Read through the Do Now, Lab, and lesson so that you are familiar with the requirements and can assist students.

## Pacing Guide
| **Duration**   |     **Description**    |
| ---------- | ------------------ |
| 5 Minutes  | Do Now             |
| 20 Minutes | Printing Lesson/Lab Part 1   |
| 20 Minutes | Variables Lesson/Lab Part 2   |
| 10 Minutes | Debrief         |

## Instructor's Notes
1. **Do Now**
    * Project the Do Now on the board, circulate around the class to check that students are working and understand the instructions. 
2. **Printing Lesson/Lab Part 1**
	*	Explain that the file is the center section of the screen. Sometimes this is called a *script*.
		* Reminder questions: how do you save/run a file? What happened when you ran the file from the do now?
		* Explain the purpose of the `print` statement, which will print whatever is in between the parentheses to the console.
			* Explain to students that this what appears on the console is called *output*
		* Talk to students about reading a program and the order in which the computer executes statements. 
	* Ask students how they would print the following:
	```
Hello World
Hello World
Hello World
Hello World
Hello World
	```
	* Have students work on Part 1 of the lab for 10 Minutes
3. **Variables Lesson/Lab Part 2**
	* *Variable*: a name that refers to a value
	* An assignment statement creates new variables and gives them values: 
	
	```python
	>>> message = 'And now for something completely different'
	>>> n = 17
	>>> pi = 3.1415926535897932
	```
		* Ask the students what they think the assignment operator is. 
		* Using the example above, ask which are the variables, and which are the values. 
		* Tell students how assignments work from right to left, so the item on the right is assigned to the item on the left. 
	* Have students work on Part 2 of the lab for 10 Minutes
4. **Debrief**
	* Talk about the difference between interactive and script mode. Discuss why you might want to use the interpreted mode: sometimes it can be faster to debug a single line and make sure it works!
	* Talk about differences between SNAP! and Python for declaring variables.

###Accommodation/Differentiation
If students are moving quickly, ask students to come up with a way to print two lines with only one print statement. Allow for students to Google the `\n` character. 

  

[Lab]:lab.md
[Do Now]:do_now.md
