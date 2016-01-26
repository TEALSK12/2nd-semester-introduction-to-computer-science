#Lesson 6.01: Introduction to Dictionaries

##Learning Objectives
Students will be able to...

* Define and identify: **dictionary**, **key**, **value**
* Create dictionaries of key-value pairs
* Access and update items from dictionaries

##Materials/Preparation
* [Do Now]
* [Lab] - Dictionaries & Memes
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
    * Students will copy and edit code involving creating a dictionary and accessing items from that dictionary.
2. **Lesson**
	* Ask the students what type they think `my_dictionary` is. 
	    * Did anyone run the `type()` function to find out? 
		* `my_dictionary` is a **dictionary** or a collection of **key-value** pairs. You use the key to look up the value in the dictionary. 
		    * Ask: what are the keys in the example from the Do Now? What are the associated values? 
        * Keys and values can be of any type. The syntax is: `{key : value, key : value, ...}` 
	* Ask the students what `my_dictionary['dog']` did, and if this syntax reminds them of anything (lists!).
		* To get the value associated with a key in a dictionary you use square brackets.
		* You can also use `my_dictionary.get()`, which will return `None` if the value isn't there. 
		    * *Note*: You can pass in a second argument to `get` which takes the place of the `None` default.
	* How would you get the value for `chair` or `car`.
	* What happened when you ran `my_dictionary['kittens']`? 
		* This error is common. It means there is no value in the dictionary. You can use `my_dictionary.get` with the if statement
3. **Lab**	
	* Students will create a dictionary translating common internet phrases into their meanings.
4. **Debrief**
	* Review what was covered in today's lesson and check for understanding of the three concepts covered: **dictionaries, keys,** and **values**.

###Accommodation/Differentiation


[Do Now]: do_now.md
[Lab]: lab.md