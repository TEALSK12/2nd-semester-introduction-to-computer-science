# Project 2: Zork

Using Python students will be using casting, Boolean expressions, lists and while loops to create a text based adventure game.

## Overview
This game will take place in a three story dungeon. The user will have to traverse through the levels and find a way to fight monsters. The goal is to reach the prize blocked by a large monster. 

## Details 
### Behavior 
* the game has three floors, each floor is made up of 5 rooms. A room can have: a sword, a monster, magic stones, up-stairs, down-stairs or nothing
* left, right move the user to the left or to the right room, an up-stairs can move the user to the next level up, a downstairs can move the user down a level. 
* users can pick up swords or magic stones if they walk across them. They are no longer in the room once grabbed
* monsters can be defeated if the user has a sword, both the moster and the sword are removed from the 
* boss monster requires a sword and a magic stone to defeat it
* 
### Implementation details 

input left, right to explore across a floor. If you come across a stairs you can go up or down. If you come across an item you can pick it up. If you come across a monster you can either fight or run back. To win a battle with a monster you must 