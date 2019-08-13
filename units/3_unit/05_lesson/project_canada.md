# Project 3: Crosscountry Canada

Using variables, functions, and conditionals in Python, students will create a variation of the classic Crosscountry Canada game. 

## Overview
Crosscountry Canada was a text based video game popular in the 90's.  This beloved retro game
was both educational and entertaining.  An online version is available to play here:  https://archive.org/details/msdos_Crosscountry_Canada_1991 .
At the start of the game, the player is given a goal to deliver (by truck) a commodity from one Canadian city to another.
To achieve your goal, the player must reference a city-commodity cross reference, such as https://archive.org/details/msdos_Crosscountry_Canada_1991 . 
The player must also know which commands are recogonized, such as: https://gamefaqs.gamespot.com/pc/566644-cross-country-canada/faqs/30240 .

In this project, we will create a simplified single-player version of the game. 

## Details 
### Behaviour (Suggestions for a Basic Version)
* The player starts in one city (random).
* The player is given a commodity and a destination city (random).
* The player must navigate the truck to a city to pick up a commodity, and deliver it to 
the destination, within 30 days. 
* At the beginning of the game, user is asked their name.
* Each turn, the player is asked what action they choose, where the player can type in one
of the following commands: 

* `travel (East or West)`: moves you randomly between 100-200km and takes 3-7 days (random)
* `rest`: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
* `eat`: eat at a restaurant 1-3 kgs of food  (random).:  
* 'get (commodity name)':  pickup the commodity
* 'fill up':  fills up your gas tank
* `status`: lists city, health, distance traveled, and day.
* `help`: lists all the commands.
* `quit`: will end the game.
* Some possible assumptions:
  - travel is always East or West (most populated regions in Canada are along the southern border).
  - limit the map to have only 7-10 major cities
  - limit each city to have only 1-2 commodities
  * The player's health randomly decreases randomly every few moves. 
  * The player eats 5kgs of food a day.
  * The truck's gas tank is 10,000 Litres
  * The truck can drive 100km with 10 Litres of gas (reference: https://www.nrcan.gc.ca/sites/www.nrcan.gc.ca/files/oee/pdf/transportation/tools/fuelratings/2018%20Fuel%20Consumption%20Guide.pdf)
  

### Implementation details 
* Document the behavior of your game.  This includes the list of commands, and list of city/commodities.
* Show this proposal to your teacher, to make sure that the scope is suitable.

---
#### Emphasize with students...

#### Curriculum Competencies - Applied Technologies

Every project must have a scope.  This is an initial document or plan of what 
your software is supposed to do, or will do.   Before you begin the design and coding
of this game, write down the behavior of your game.   You can use the suggestions
above, or modify it to be more unique.  However, keep your scope simple and clear. 
Resist the urge to overly complicate the game in your scope definition.  Once you
get a version that is working, you can add new commands or features in a future revision!  Software
development is iterative, and scaffolds over time.  

---

* Create functions for all options a player can take
* Use globals to keep track of player health, food, distance to go, current day, etc
* Create a function add_day which updates the day 
* Create a function select_action which uses a while loop to call add_day function

## Grading 
### Scheme/Rubric
| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| `travel`, `rest`, `eat`, 'fill up'                             | 15  |
| `status`, `help`, and `quit`                                    | 5  |
| Game ends if food runs out, days run out, or health runs out    | 10  |
| Days roll over correctly	                                      | 10  | 
| Gas descreases accordingly                                      | 5  | 
| Health decreases randomly	                                      | 5   | 
| **Sub total**                                                   | 50  |
| **Technical Correctness   **                                    |     |
| Correctly use functions and contracts                           | 20  |
| Correctly use imported random function                          | 5  |
| Correctly use global variables                                  | 5  |
| Correctly use and update variables                              | 5  |
| Correctly add_days and select_action functions                  | 15  |
| **Sub total**                                                   | 50  |
| **Total**                                                       | 100 |


## Extra Credit
1.  Make the rate of food consumption be a function of the day of the week.
2.  Make a rate of fuel consumption to be a function of the location/climate/season.  For example, colder regions burn more gas.
3. Create a random event that occurs randomly, like a forest fire roadblock, that will affect health, gas, and time.
