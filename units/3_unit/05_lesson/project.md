# Project 3: Oregon Trail

Using variables, functions, and Python, students will be using functions, variables. 

## Overview
We will be recreating Oregon Trail! The goal is to travel from NYC to Oregon (2000 miles) by Dec 31st. However the trail is arduous. Each day costs you food and health. You can hunt and rest, but you have to get there before winter! 

## Details 
### Behavior 
* Player starts in NYC on 03/01 with 2,000 miles to go, 500lbs of food, 5 health and Player must get to Oregon by 12/31
* at the beginning of the game, user is asked name
* each turn player is asked what they should choose, player can type in the following: `travel`, `rest`, `hunt`, `status`, `help`, `quit`
* players health randomly decreases 2 times during the month 
* `travel`: moves you randomly btween 30-60 miles and takes 3-7 days
* `rest`: increases health 1 level (up to 5) and takes 2-5 days
* `hunt`: adds 100lbs of food and takes 2-5 days
* `status`: lists food, health, distance traveled, and day
* `help`: lists all the commands
* `quit`: will end the game
### Implementation details 
* create functions for all options a player can take
* create variables for health, food, miles, month, day, days_passed, and more
* create a function add_day which updates the day 
* create a function update_days which uses a while loop to call add_day function

## Grading 
### Scheme/Rubric
| Functional Correctness(Behavior)                                |     |
| --------------------------------------------------------------- |-----|
| `travel`, `rest`, `hunt`                                        | 30  |
| `status`, `help`, and `quit`                                    | 15  |
| Game ends if food runs out, days run out, or health runs out    | 20  |
| Days roll over correctly	                                       | 15  | 
| Helth decreases randomly	                                       | 5   | 
| **Sub total**                                                   | 90  |
| **Technical Correctness   **                                    |     |
| Correctly use functions and contracts                           | 35  |
| Correctly use imported random function                          | 10  |
| Correctly use and update varaiables                             | 10  |
| Correctl add_days and update_days functions                     | 20  |
| **Sub total**                                                   | 75  |
| **Total**                                                       | 165 |


