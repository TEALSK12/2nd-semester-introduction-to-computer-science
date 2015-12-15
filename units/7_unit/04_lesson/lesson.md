# Lesson: Inheritance

##Learning Objectives
Students will be able to... 

* Define and identify: **inheritance**,  **parent class**, **child class**
* Create a class that inherits from anther class
* Overwrite methods of parent class in child class 

##Materials/Preparation
* [Do Now]
* [Lab]
* [Associated Reading] - 6.4
* Read through the handout, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Discussion  |

## Instructor's Note

1. **Do Now**
    * Display the Do Now on the board.
2. **Lesson**
	* Discuss Do Now
		* **inheritance**: what is different between the Dog declaration than the Pet declaration? What does the class think it means to have Pet instead of Object. What happens when you initialize Pet, and what about Dog? 
			* What is missing from the do now? When a class inherits from another class the class it inherits from is called the **parent class** and the class that inherits is called the **child class**. 
			* In the do now which is the child and which is the parent. 
			* Child classes also gain access to all methods of Parent class
				* What does `dog1.make_nosie()` print out? 
			* Child classes can also overwrite their parent classes. Have the students practice overwriting make_noise so that the dog will print out `bark bark`
3. **Lab**	
	* Given a generic Pokemon class, create a few child classes that represent different types
4. **Debrief**
	* Go over students' questions. Ask what questions the students have and review instance, class, methods, init, str, etc

  
[Do Now]:do_now.md
[Lab]:lab.md