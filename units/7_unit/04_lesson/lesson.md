# Lesson 7.04: Inheritance

##Learning Objectives
Students will be able to... 

* Define and identify: **inheritance**,  **parent class**, **child class**
* Create a class that inherits from anther class
* Overwrite methods of parent class in a child class 

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading - section 6.4 of Book
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes

1. **Do Now**
    * Display the Do Now on the board.
    * Students will explore an example of a new `Dog` class inheriting the methods of the `Pet` class 
2. **Lesson**
	* Discuss the Do Now.
		* **Inheritance**: when you create a new class that is a subclass of the original (ex. the `Dog` class "inherits" the properties/methods of the `Pet` class.) 
		* Ask students: what is the difference between the `Dog` declaration and the `Pet` declaration? 
        * Discuss the error and what was missing in the original code. 
        * When a class inherits from another class, the class it inherits FROM is called the **parent class** and the class that inherits is called the **child class**. 
		* Ask: in the example from the do now, which is the child and which is the parent?
			* Child classes gain access to all the methods of the parent class
				* What does `dog1.make_nosie()` print out? 
			* Child classes can also overwrite their parent classes. Have the students practice overwriting `make_noise` in the `Dog` class so that the dog will print out `bark bark`
3. **Lab**	
	* Given a generic Pokemon class, create three child classes that represent different types of Pokemon.
4. **Debrief**
	* Go over students' questions. Ask what questions the students have and review instance, class, methods, init, str, etc

  
[Do Now]:do_now.md
[Lab]:lab.md