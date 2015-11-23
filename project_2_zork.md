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
* a list to keep track of 
input left, right to explore across a floor. If you come across a stairs you can go up or down. If you come across an item you can pick it up. If you come across a monster you can either fight or run back. To win a battle with a monster you must 