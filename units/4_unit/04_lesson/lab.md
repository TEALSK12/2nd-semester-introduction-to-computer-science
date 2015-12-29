# Lab 4.04

## Part 1
The goal of this lab is to practice using and accessing items from lists of lists. 

You will be given a nested list, `schedule`, where the first list represents morning activities, the second list represents afternoon activities, and the third list represents evening activities. 

This program will allow the user to ask or update what activities you do in the morning, afternoon, or evening. The user can request you `print all` the activities at that time, or request a specific activity.

###Schedule 

```python
schedule = [
['brush teeth', 'eat', 'check email'],
['eat', 'do work', 'check instagram'],
['eat', 'watch youtube', 'brush teeth']
]
```

### User Inputs
* `update`
	* The program will ask which time (morning, afternoon, evening) the user wants to update and will also request which position it should update.
* `print` 
	*  The program will ask which time (morning, afternoon, evening) the user wants to print from and afterwards will request which position it should print.
* `print all`
	* The program will ask which time (morning, afternoon, evening) the user wants to print and will print all of the activities associated with that time. 	
	
###Functions
* `update_activity`
    * Takes in an integer representing the index of the time, an integer representing the index of the activity to update, and a string representing the new activity to add to that time.
* `print_all`
    * Takes an int representing the index of the time to print.


* Feel free to add more functions as you see fit

### Example

```
>>>What would you like to do? print all
Which time would you like to print? evening
eat dinner, watch youtube, brush teeth
```


## Part 2 

In this part of the lab you will go through your schedule program and perform a few different calculations. 

1. Create a function, `all_in_one`, that will put all the activities into a single list using a for loop. 
2. Create a function, `count_meals`, which will go through all items of the list and keep a count of how many times `'eat'` occurs. 
3. In order to make the schedule more rigorous, write a function, `study_more`, that adds `'study'` to each of the lists. 
4. Dentists recommend we floss our teeth twice daily. Write a function `dentists_agree`, that will go through every element of schedule and update `'brush teeth'` to be `'brush and floss teeth'`.

###Bonus: 
Write a function to reverse the order of the lists and activities in `schedule`. 

The list should look like the following when printed: 

```python
schedule = [
['brush teeth', 'watch youtube', 'eat'],
['check instagram', 'do work', 'check instagram'],
['check email', 'eat', 'brush teeth']
]
```