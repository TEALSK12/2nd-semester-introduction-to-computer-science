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
* Associated Reading - section 7.2 of Book
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
    * Display the Do Now on the board.
    * Students use the `__init__` method and explore how to initialize new objects with one or more arguments. 
2. **Lesson**
	* Discuss the Do Now.
		* Ask students what the name of the class is. 
		* Ask students where the Pet object is instantiated. 
		* **`__init__`**: 
			* Ask students what they think the `__init__`  does. 
			    * `__init__` is a special function that is called when the class is first initialized. 
			    * If there is a print statement added to the `__init__` method, when would it get printed? 
		* **`self`**: 
			* Ask students what they think `self` is. What does `self.name` do and how does that relate to what `my_pet.name` does? 
			    * `self` is a way of referring to the instance within a function. Previously we had added attributes *after* the class was instantiated, but `self` allows for us to assign those at once in a single method.
3. **Lab**	
	* Students will make a Pet class. Each pet will have an animal type, color, food, noise, and name. 
	* Next students write a function that will take a list of pets and print out their name and the food they like to eat.
4. **Debrief**
    * Check for student understanding and completion of the lab.	
    * Review the two key concepts introduced today (`self` and `__init__`)

###Accommodation/Differentiation

As with the previous lesson, be prepared for some students to struggle with the new vocabulary and concepts being introduced. Reinforce the use of vocabulary such as **instantiate**, **object**, and **attribute** so that students are consistently exposed to how to use these terms.  
  
[Do Now]:do_now.md
[Lab - Pet Class]:lab.md
