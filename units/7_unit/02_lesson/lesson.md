# Lesson 7.02: User-Defined Types, Part 2

##Learning Objectives
Students will be able to... 
* Define and identify: **self**, **`__init__`**
* Create a class with an init method
* Understand and use the `self` argument 
* Instantiate a class with arguments

##Materials/Preparation
* [Do Now]
* [Lab - Pet Class]
* Associated Reading - section 6.2 of Book
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Note

1. **Do Now**
    * Display the Do Now on the board.
    * Students use the `__init__` method and explore how to initialize new objects with one or more arguments. 
2. **Lesson**
	* Discuss the Do Now
		* Ask the students what the name of the class is. (Pet)
		* Ask the students where the code is instantiated. 
		* **`__init__`**: 
			* Ask students what they think the `__init__`  does 
			* `__init__` is a special function that is called when the class is first initialized. 
			* If there is a print statement added to the `__init__` method, when would it get printed? 
		* **self**: 
			* Ask students what they think self is. What does self.name do and how does that related to what my_pet.name does? 
			* self is a way of referring to the instance within a function. So previously we had added attributes after the class was instantiated, but self allows for us to assign those at once in a single method
3. **Lab**	
	* Students will make a pet class. Each pet will have a type, breed, color, food, noise, and name. 
	* Write a function that will take a list of pets and print out their name and the food they like to eat
4. **Debrief**
	* Talk about the init 

  
[Do Now]:do_now.md
[Lab - Pet Class]:lab.md