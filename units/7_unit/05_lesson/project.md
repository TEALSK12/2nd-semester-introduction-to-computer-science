[# Project: Pokemon

In this project we will be creating a basic implementation of pokemon battle.

##Overview
You will create a hand of 3 pokemon. Once you create your hand. You will simulate game play of a battle. The opponent will have a pokemon chosen randomly and you will battle.

At the start of the game, the program will list out possible pokemon. You will then select the 3 pokemon you want in your hand. 

The game will then ask you which pokemon you want to use for battle. 

Each turn the program will display stars on the pokemon you are playing, and ask you what you would like to do. Fight, heal, change pokemon or run away. The opponent will fight or heal randomly.

If you defeat your enemy's pokemon you win the game. If they defeat you, you lose the game . 

### Behaviour
#### Game Play
* Choose 3 Pokemon: At the beginning of the game the program will list out the pokemon to choose from. Options are the following, HP stands for the health points the pokemon has and AP says the max value of attack 
	* Grass Type: 
		* Bulbasoar: 60HP, 40AP
		* Bellsprout: 40HP, 60AP
		* Oddish: 50HP, 50AP
	* Fire Type: 
		* Charmainder: 25HP, 70AP
		* Ninetails: 30HP, 50AP
		* Ponyta: 40HP, 60AP
	* Water Type:
		* Squirtle: 80HP, 20AP
		* Psyduck: 70HP, 40AP
		* Polywag: 50HP, 50AP
* Choose Pokemon to use in fight
* Generate Computer's Hand and randomly select a pokemon to start
* On each turn the player or computer can either fight, heal, or switch pokemon
* At the end of the turns the game should print out stats, and check if either side has lost the game 
* A player has lost if all their pokemon are out of HP
* Hand: lists of pokemon the player has
* All Stats: Lists the stats (HP, AP, Name) of all pokemon in the hand 

#### Player 

** Hand **
* Print out all the pokemon the player has in their hand

** All Stats **
* Prints out the: HP, AP, Name of all the pokemon in the hand

** Stats **
* Prints out the: HP, AP, Name of the pokemon selected to fight

** Moves **
* Prints out all the possible attacks

**Attack**

* User Choose an attack
* Damage the computers pokemon
* Damage on an attack is 3/4 of the time the attack power and 1/4 of the time the pokemons AP
* Attacks fail a certain percentage of the time. Each attack has an accuracy

**Heal**

* Cannot attack for two turns
* Pokemon is healed by 20 HP 

**Switch** 

* Lose turn, but use a different pokemon

#### Computer 
Computer will select between the three options. 2/3 the time they should file. 1/6 of the time they should heal and 1/6 of the time they should switch pokemon. 
**Attack**
* Randomly select an attack
* Damage the computers pokemon
* Same attack power and accuracy as player
**Heal**
* Cannot attack for two turns
* Pokemon is healed by 20 HP 
**Switch** 
* Lose turn, but use a different pokemon

#### Grass Type 
All grass type have the following attacks: 
	* Leaf Storm: 130 Power, 90% accurate
	* Mega Drain: 50 Power, 100% accurate
	* Razor Leaf: 55 Power, 95% accurate
Grass Type is 1.5x stronger against Water Type.

#### Fire Type 
All fire type have the following attacks: 
	* Ember: 60 Power, 100% accurate
	* Fire Punch: 85 Power, 80% accurate
	* Flame Wheel: 70 Power, 90% accurate 
Fire Type is 1.5x stronger against Grass. 

#### Water Type 
All fire type have the following attacks: 
	* Bubble: 40 Power, 100% accurate
	* Hydro Pump: 185 Power, 30% accurate
	* Surf: 70 Power, 90% accurate 
Water Type is 1.5x stronger against Fire Types. 

### Implementation Details
* Use classes to create a base class for pokemon. Keep track of HP, Max AP, and type. Each pokemon has an attack method, and an stats method which prints out all the stats. 
* Design classes for Fire, Grass, Water Types
* Each pokemon should be an instance 
* Player's and Computer's pokemon should be stored using a list

## Grading 
### Scheme/Rubric
| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| Players can choose pokemon hand | 15   |
| Computer randomly picks hand | 5|
| Player can choose pokemon to battle  | 5   |
| Stats, Move, and  All stats print properly           | 10  |
| Attack command decreases HP properly      | 10 |
| **Sub total**                                                   | 35  |
| **Technical Correctness   **                                    |     |
| Correct use of classes                                  | 10  |
| Correct use of inheritance                                  | 10  |
| Correct use of instances                                  | 10  |
| Correct use of variables and game loop |10| 
| Correct use of printing/formatting | 10|  
| **Sub total**                                                   | 50  |
| **Total**                                                       | 85 |