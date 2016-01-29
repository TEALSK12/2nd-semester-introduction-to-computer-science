# Lesson: User Defined Types

##Learning Objectives
Students will be able to... 
* Define and identify: **class**, **instance**, **object**, **attributes**
* Create a class and instantiate 
* Add attributes to an instance
* Use attributes and class

##Materials/Preparation
* [Do Now]
* [Example]
* [Lab]
* Associated Reading - section 6.1 of Book
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Discussion  |

## Instructor's Note

1. **Do Now**
    * Display the Do Now on the board.
2. **Lesson**
	* Discuss the Do Now:
		* Ask the students what data type they thought would be helpful. They probably noticed that this was going to be difficult to do concisely without some other data type.
		* Acknowledge that we need something that says "I am type Pet, which has three different attributes". 
	* **Class**: a user-defined type. 
		* On board write syntax for creating a class: `class Pet(object):`
		* **Object** : the basis of object-oriented programming (OOP). Objects correspond to a real world thing that has certain attributes associated with it.
		* Instantiated: you can create **instances** of a class by using `Pet()` (`my_pet_1` is an instance of the `Pet` class). If you check the type of an instance it will be `Pet`.
		* Instances are mutable, they can be changed or updated.
	* Show [Example] on board to demonstrate the `Pet` class.
	 	* Ask students what the difference is between this and the do now.
	 	* Have the students identify where the class is created. 
	 	* Next have the students identify where the class is instantiated.
		* Ask students what they think `pet.full_name` will do.
			* This is a good time to explain the concept of an attribute.
			* **Attribute**: values assigned to an instance.
	* Note that you can also create functions that take in classes and use their attributes.
3. **Lab**	
	* Students will create RGB colors using class.
	* Create a function to merge two colors.  
	* Check up their colors on a rgb website 
4. **Debrief**
	* Talk about any of the phrases or issues the students had. Did they find it easy to understand the code when they read it.

  
[Do Now]:do_now.md
[Lab]:lab.md
[Example]:example.md