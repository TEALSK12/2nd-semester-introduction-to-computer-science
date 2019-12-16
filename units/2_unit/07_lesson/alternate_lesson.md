# Alternate Project 2: TODO List
Created By Brian Weinfeld

Using Python, students will create an interactive TODO list that allows users to add and remove tasks from a list.

## Overview

One of the most common tasks we use computers for is to store and track data. Perhaps the most simple form of this task is the TODO list.
A TODO list is simply a list of tasks that the user wants to track. They can add tasks to the list, remove them when they are complete and
examine the list as they progress. Have you ever used a Notes app on your phone?

For this project, you are going to recreate the functionality of a simple TODO list app.

## Details

### Behavior

* The program offers the user 4 options. **add** will add elements to the TODO list. **remove** will remove elements from the list. 
**list** will display the entire list and **exit** will exit the program Let's examine **add** and **remove** in more detail.

* After a user selects **add** they should then be prompted for the item they want added to the list. Be sure to check before
you add the item to the list. You don't want to add the item twice!

* After a user select **remove** they should then be prompted for the item they want removed from the list. Be sure to check before
removing the item from the list. You should let the user know if they are trying to remove an item that isn't in the list!

```
Welcome to your TODO list
What would you like to do? (add, remove, list, exit) list
[]

What would you like to do? (add, remove, list, exit) add
What would you like to add to your list? go to gym
Successfully added
What would you like to do? (add, remove, list, exit) list
['go to gym']

What would you like to do? (add, remove, list, exit) add
What would you like to add to your list? buy food
Successfully added
What would you like to do? (add, remove, list, exit) list
['go to gym', 'buy food']

What would you like to do? (add, remove, list, exit) add
What would you like to add to your list? go to gym
This is already on your list!
What would you like to do? (add, remove, list, exit) list
['go to gym', 'buy food']

What would you like to do? (add, remove, list, exit) remove
What would you like to remove? go to gym
Sucessfully removed
What would you like to do? (add, remove, list, exit) list
['buy food']

What would you like to do? (add, remove, list, exit) remove
What would you like to remove? clean bedroom
This is not in the list!
What would you like to do? (add, remove, list, exit) list
['buy food']

What would you like to do? (add, remove, list, exit) exit
Goodbye
```

### Challenge

This section contains additional components you can add to the project.
These should only be attemped **after** the project has been completed.

* It is a bit inconvenient to have to type two commands to add or remove an element from the list. Modify the program so that tasks 
can be added to the TODO list with a single command **add go to gym** or removed **remove go to gym**. 

```
Welcome to your TODO list
What would you like to do? (add, remove, undo, list, exit) add go to gym
Successfully added
What would you like to do? (add, remove, undo, list, exit) list
['go to gym']

What would you like to do? (add, remove, undo, list, exit) add clean bedroom
Successfully added
What would you like to do? (add, remove, undo, list, exit) list
['go to gym', 'clean bedroom']

What would you like to do? (add, remove, undo, list, exit) remove bedroom
This is not in the list!
What would you like to do? (add, remove, undo, list, exit) remove clean bedroom
Sucessfully removed
What would you like to do? (add, remove, undo, list, exit) list
['go to gym']
```

* The most common task in a TODO list is to immediately remove the most recently added element to the list. This is often because
the user made a mistake in adding the element to the list in the first place. Add an **undo** option to the program that will remove
the most recently added item. If the item is no long in the list, print an error.

```
Welcome to your TODO list
What would you like to do? (add, remove, undo, list, exit) add go to gym
Successfully added
What would you like to do? (add, remove, undo, list, exit) add clean bedroom
Successfully added
What would you like to do? (add, remove, undo, list, exit) list
['go to gym', 'clean bedroom']

What would you like to do? (add, remove, undo, list, exit) undo
Successfully undid last add.
What would you like to do? (add, remove, undo, list, exit) list
['go to gym']

What would you like to do? (add, remove, undo, list, exit) undo
Cannot undo. You already removed this item
What would you like to do? (add, remove, undo, list, exit) list
['go to gym']
```

## Solution

```python
print('Welcome to your TODO list')
data = []
while True:
  command = input('What would you like to do? (add, remove, list, exit) ')
  if command == 'add':
    to_add = input('What would you like to add to your list? ')
    if to_add not in data:
      data.append(to_add)
      print('Successfully added')
    else:
      print('This is already on your list!')
  elif command == 'remove':
    to_remove = input('What would you like to remove? ')
    if to_remove not in data:
      print('This is not in the list!')
    else:
      del data[data.index(to_remove)]
      print('Sucessfully removed')
  elif command == 'list':
    print(data)
  elif command == 'exit':
    print('Goodbye')
    break
  else:
    print('Sorry, I did not understand that')

# extensions

print('Welcome to your TODO list')
data = []
last = None
while True:
  command = input('What would you like to do? (add, remove, undo, list, exit) ')
  if command.startswith('add'):
    to_add = command.split(' ', 1)[1]
    if to_add not in data:
      data.append(to_add)
      last = to_add
      print('Successfully added')
    else:
      print('This is already on your list!')
  elif command.startswith('remove'):
    to_remove = command.split(' ', 1)[1]
    if to_remove not in data:
      print('This is not in the list!')
    else:
      del data[data.index(to_remove)]
      print('Sucessfully removed')
  elif command == 'undo':
    if last not in data:
      print('Cannot undo. You already removed this item')
    else:
      del data[data.index(last)]
      print('Successfully undid last add.')
  elif command == 'list':
    print(data)
  elif command == 'exit':
    print('Goodbye')
    break
  else:
    print('Sorry, I did not understand that')
```

## Grading

TO BE UPDATED

### Scheme/Rubric

| Functional Correctness (Behavior)                               |     |
| --------------------------------------------------------------- |-----|
| Game has three floors                                           | 5   |
| User can move `left` or `right`, but not beyond the rooms       | 10  |
| User can only move `up` or `down` at an appropriate staircase   | 5   |
| `Grab` adds an item to the users collected items                | 5   |
| User can only collect 3 items                                   | 2   |
| `Help` lists all possible commands                              | 2   |
| Monsters either disappear if user has a sword or defeat the user| 5   |
| A sword can only be used once and then it disappears            | 6   |
| Boss monster needs sword and magic stones to be defeated        | 5   |
| Prize is blocked by boss monster                                | 5   |
| **Sub total**                                                   | 50  |
| **Technical Correctness**                                       |     |
| Correctly use of lists                                          | 15  |
| Correctly appends items to list of users collected items        | 15  |
| Correctly uses if statements to check items in user's possession | 15  |
| Correctly using `or` statements and `and` statements            | 15  |
| **Sub total**                                                   | 60  |
| **Total**                                                       | 110 |

## Extra Credit

* Add the command `run`, which allows a player to run past a monster instead of fighting. This should work 40% of the time. (Hint: Research the random library.)
* Implement the board using nested lists (each item of the list is a list.)
