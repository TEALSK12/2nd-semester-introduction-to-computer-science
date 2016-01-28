# Lab 6.03 - Dictionaries Storing Lists

In this lab we will create a dictionary to-do list. Each key in the dictionary will be a day of the week. Each associated value will a be a list of items. 

The program `daily_to_do_list_lab.py` will prompt the user what they want to do: 'add' or 'get'. If the user types in 'get', the program will ask which day and return the to-do list for that day. If the user writes 'add', the program will ask which day and what item should be added.

At the start of the program the dictionary should be totally empty. Items should only occur once in the to-do list for any given day. 

### Example

```
>>>python3 daily_to_do_list_lab.py
What would you like to do? 
add
What day? 
Friday
What would you like to add to Friday's to-do list? 
practice clarinet
What would you like to do? 
get
What day? 
Friday
You have to practice clarinet. 
What would you like to do. 
```

## Bonus!
It's a bit tedious for the user to have to type in three different lines to add an item to a to-do list. Use `split` to allow the user to input `add Friday watch tv and relax`. 

Create a variation of the program that doesn't allow any duplicates across any of the days. Make sure when you add a to-do item that it doesn't exist in the to-do lists of any of the days before adding. 