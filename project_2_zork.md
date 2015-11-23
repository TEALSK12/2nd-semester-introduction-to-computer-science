# Project 2: Zork

Using Python students will be using casting, Boolean expressions, lists and while loops to create a text based adventure game.

## Overview
This game will take place in a three story dungeon. The user will have to traverse through the levels and find a way to fight monsters. The goal is to reach the prize blocked by a large monster. 

## Details 
### Behavior 
* the game has three floors, each floor is made up of 5 rooms. A room can have: a sword, a monster, magic stones, up-stairs, down-stairs or nothing
* a user can move to the left room or right room. The user can also move upstairs or downstairs if the room contains an up-staircase or a down-staircase. 
* users can pick up swords or magic stones if they walk into a room with them. The sword or stones are no longer in the room once grabbed
* monsters can be defeated if the user has a sword, both the monster and the sword are removed from the room. otherwise the monster defeats the user and the game ends. 
* boss monster requires a sword and a magic stone to defeat it
### Implementation details 
* there should be a representation of the game using nested lists
* a list to keep track of the user's items, at the beggining of the game it's empty 
* 3 different monsters placed throughout the game which require a sword to win
* a boss monster which requires magic stones and a sword to defeat
* can only go up if there is an up-staircase, and only go down if there is down-staircase

## Grading 
### Scheme/Rubric
| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| Game has three floors                                           | 5   |
| User can move `left` or `right`, but not beyond the rooms       | 10  |
| User can only move `up` or `down` at an appropriate staircase   | 5   |
| `Grab` adds an item to the users pocket                         | 5   |
|  User pocket can only hold 3 items                              | 2   |
| `Help` lists all possible commands                              | 2   |
| Monsters either disappear if user has a sword or defeat the user| 5   |
| Sword can only be used once                                     | 6   | 
| Boss monster needs sword and magic stones to be defeated        | 1:2 |
| Prize is blocked by boss monster                                | 1:2 |
| **Sub total**                                                   | 1:2|
| **Technical Correctness   **                                    | |
| Correctly use nested lists                                      | cats|
| Correctly appends items to list of users pocket                 | cats|
| Correctly uses if statements to check items in a users pockets  | 1:2 |
| Correctly using `or` statements and `and` statements            | 1:2 |
| **Sub total**                                                   | 1:2|
| **Total**                                                       | 1:2|


