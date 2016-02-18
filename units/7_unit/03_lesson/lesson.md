# Lesson 7.03: Methods

##Learning Objectives
Students will be able to... 
* Define and identify: **method**, **`__str__`**, **`__add__`**, **operator overloading**
* Create a class with an `__init__` method
* Understand and use the `self` argument
* Instantiate a class with an argument

##Materials/Preparation
* [Do Now]
* [Lab - Kangaroo Class]
* Associated Reading - section 6.3 of Book
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
    * Students will find that when they try to print the two different Time objects, it produces output that's not particularly useful or readable.
    * Students will also discover that adding objects doesn't work...yet!
2. **Lesson**
	* Discuss the Do Now.
		* **method**: a function inside of a class. 
		* The first argument is always `self`. 
		* Ask students what method we have already seen and used previously. (`init`)
		* Ask students how they would distinguish between the two time variables.
		* **`__str__`**: Need a method called `__str__`. This will get called when you print an object, and it returns a string that is easy to read and understand.
			* Have the students practice writing `__str__` for the `Time` class for 5 minutes.
			* Have a student write up their string method on the board. 
		* **`__add__`**: add is another method that gets called when the plus sign is used. It takes in another two time objects and returns a time object that is the sum of both. 
			* Overwriting add is called **operator overloading** because you are re-writing the code used to make the + work.
			* Work together with students to come up with the add time algorithm.
3. **Lab**	
	* Have students finish up the time adding method.
	* Have students work on kanga roo lab.
4. **Debrief**
	* Go over students' questions. Ask what an instance is versus an object vs a class. Ask difference between method and attribute.

###Accommodation/Differentiation

Students that are moving quickly should work on the bonus assignment in the lab or assist a partner that is struggling. 

[Do Now]:do_now.md
[Lab - Kangaroo Class]:lab.md