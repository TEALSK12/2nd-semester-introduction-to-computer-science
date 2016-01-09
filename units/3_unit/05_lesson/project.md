# Project 3: Oregon Trail

Using variables, functions, and conditionals in Python, students will create an Oregon Trail game. 

## Overview
We will be recreating Oregon Trail! The goal is to travel from NYC to Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each day costs you food and health. You can hunt and rest, but you have to get there before winter! 

## Details 
### Behavior 
* Player starts in NYC on 03/01 with 2,000 miles to go, 500lbs of food, and 5 health. 
* The player must get to Oregon by 12/31
* At the beginning of the game, user is asked their name.
* Each turn, the player is asked what action they choose, where the player can type in the following: `travel`, `rest`, `hunt`, `status`, `help`, `quit`
* The player's health randomly decreases 2 times during the month. 
* The player eats 5lbs of food a day.
* `travel`: moves you randomly between 30-60 miles and takes 3-7 days (random).
* `rest`: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).
* `hunt`: adds 100 lbs of food and takes 2-5 days (random).
* `status`: lists food, health, distance traveled, and day.
* `help`: lists all the commands.
* `quit`: will end the game.

### Implementation details 
* Create functions for all options a player can take
* Use globals to keep track of player health, food pounds, miles to go, current day, current month
* Create a function add_day which updates the day 
* Use global list to keep track of which months have 31 days and use this in the add_day function (i.e.: MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12])
* Create a function update_days which uses a while loop to call add_day function

## Grading 
### Scheme/Rubric
| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| `travel`, `rest`, `hunt`                                        | 15  |
| `status`, `help`, and `quit`                                    | 5  |
| Game ends if food runs out, days run out, or health runs out    | 10  |
| Days roll over correctly	                                      | 10  | 
| Food decreases every day                                        | 5  | 
| Health decreases randomly	                                      | 5   | 
| **Sub total**                                                   | 50  |
| **Technical Correctness   **                                    |     |
| Correctly use functions and contracts                           | 20  |
| Correctly use imported random function                          | 5  |
| Correctly use global varaiables                                 | 5  |
| Correctly use and update varaiables                             | 5  |
| Correctly add_days and update_days functions                    | 15  |
| **Sub total**                                                   | 50  |
| **Total**                                                       | 100 |


## Extra Credit
1.  Make the rate of food consumption be a function of activity. So if a player hunts for a turn they take up more food, but if they rest they take up less food. 
2. Create a random event that occurs randomly once a month, like a river crossing or a dysentery, that will take up a range of 1-10 food, 1-10 days and 0-1 health. 
