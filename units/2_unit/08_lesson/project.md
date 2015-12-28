# Project 2: Zork - Text Monster Game

Using Python, students will be using casting, Boolean expressions, lists and while loops to create a text-based adventure game!

## Overview
This game will take place in a three story dungeon. The user will have to traverse through the levels and find a way to fight monsters. On each move the user has seven possible actions: `left`, `right`, `up`, `down`, `grab`, `fight`, `help`. If the move is invalid (not one of these options), the game should let the user know. Otherwise, the game will execute the user's move. The goal of the game is to reach the prize blocked by a boss monster. 

## Details 
### Behavior 
* The game has three floors, each floor is made up of 5 rooms. A room can have: a sword, a monster, magic stones, up-stairs, down-stairs or nothing
* on their move a user can try to move to the left room or right room. If there is no room the game should handle this. The user can also move upstairs or downstairs if the room contains an up-staircase or a down-staircase. 
* on their move a user can pick up swords or magic stones if they walk into a room with them. The sword or stones are no longer in the room once grabbed
* monsters: guard rooms. Users can use a sword to defeat the monster. if they have no sword they can run away. Sword and monsters disappear after fighting. 
* boss monster requires a sword and a magic stone to defeat it
### Implementation details 
* there should be a representation of the game using nested lists
* a list to keep track of the user's items, at the beggining of the game it's empty 
* 3 different monsters placed throughout the game which require a sword to win
* a boss monster which requires magic stones and a sword to defeat
* can only go up if there is an up-staircase, and only go down if there is down-staircase
* your program should not allow a player to run past the monster, go up or down or past bounds of the game. 

### Design Considerations
#### Game Board
The game board is the basis of the game. It will be helpful to design a nested list to represent the terrain. 
``` 
floor_1 = ['nothing', 'nothing', 'stairs up']
floor_2 = ['nothing', 'nothing', 'stairs up']
floor_3 = ['prize', 'nothing', 'nothing']
```
The above code has each floor being it's own lists. Feel free to use a different implementation, but this should work for our purposes. 

#### User Position
It will be useful to keep track of the user's position through a variable. 
``` 
user_room = 0
user_floor = floor_1 
``` 
This would put the user at the position of the first room of the first floor
#### Validating User Input
You will need to check the input of the user to make sure they requested a valid move: 
```
if user_input == "down":
    current_room = user_floor[user_room]
    if current_room != "stairs down": 
        print("Can't go downstairs, there are no stairs")
```

## Grading 
### Scheme/Rubric
| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| Game has three floors                                           | 5   |
| User can move `left` or `right`, but not beyond the rooms       | 10  |
| User can only move `up` or `down` at an appropriate staircase   | 5   |
| `Grab` adds an item to the users pocket                         | 5   |
|  User pocket can hold 3 items                                   | 2   |
| `Help` lists all possible commands                              | 2   |
| Monsters either disappear if user has a sword or defeat the user| 5   |
| Sword can only be used once                                     | 6   | 
| Boss monster needs sword and magic stones to be defeated        | 5   |
| Prize is blocked by boss monster                                | 5   |
| **Sub total**                                                   | 50  |
| **Technical Correctness   **                                    |     |
| Correctly use nested lists                                      | 15  |
| Correctly appends items to list of users pocket                 | 15  |
| Correctly uses if statements to check items in a users pockets  | 15  |
| Correctly using `or` statements and `and` statements            | 15  |
| **Sub total**                                                   | 60  |
| **Total**                                                       | 110 |

##Extra Credit
Add the command `run`, which allows a player to run away from a fight with a monster. This should work 40% of the time. (Hint: Research the random library)
