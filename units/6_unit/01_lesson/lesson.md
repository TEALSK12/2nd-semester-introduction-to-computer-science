#Lesson 6.01: Introduction to Dictionaries

##Learning Objectives
Students will be able to...

* Define and identify: **dictionary**, **key**, **value**
* Create dictionaries of key-value pairs
* Access and update items from dictionaries

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading - section 5.1 of Book
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
    * 
2. **Lesson**
	* Ask the students what type they think my_dictionary is. Did anyone run the type() function? 
		* my_dictionary is a dict or a collection of key,value pairs. You use the key to look up the value in the dictionary. What are the keys in this example ('cat', 'dog', 'chair', 'car')? What are the values? Keys and values can be of any type. The syntax is key : value, key: value, ... surrounded by curly brackets. 
	* Ask the students what `my_dictionary['dog']` did? What does this syntax remind them of (lists)?
		* To get the value of a key in the dictionary you use the square brackets.
		* This is very easy for the computer to do.
		* Can also use `my_dictionary.get` which will return None if the value isn't there. 
		* Note: Can pass in a second argument to `get` which act as the default
	* How would you get the value for `chair` or `car`.
	* What happened when you ran `my_dictionary['kittens']`? 
		* This error is common. It means there is no value in the dictionary. You can use `my_dictionary.get` with the if statement
3. **Lab**	
	* Students will create a dictionary translating internet phrases into their meanings
4. **Debrief**
	* Talk about any of the phrases or issues the students had. Did they find it easy to understand the code when they read it.



[Do Now]: do_now.md
[Lab]: lab.md