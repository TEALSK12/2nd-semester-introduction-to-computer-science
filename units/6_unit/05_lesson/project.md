# Project 6: Guess Who

In Guess Who, you’ll be building a text version of the classic board game. Dictionaries will be the key to this project. [Play a Sample Game.](http://www.miniplay.gr/?view=game&gid=76)

## Overview
The game should store information on at least 5 different characters. Each character should have a name, gender, age, height, and hair color.

When the game begins, a character should be randomly selected by the computer. The player can ask for 2 pieces of information about the random character, and then has to make a guess as to who was picked.

### Behavior/Commands
* list: list out all the character's names
* gender/age/height/hair: asks for a piece of information
* guess <name>: guess a character
* help: displays all commands
* quit: exits the game

### Implementation Details
* To store and access the information you’ll need to use dictionaries, which will allow for quick and direct access.

### Example Output
```
What would you like to do? list
mike: 
['Male', '15', "6'1", 'Blonde']
liv: 
['Female', '25', "5'11", 'Blonde']
lisa: 
['Female', '15', "5'10", 'Red']
linda: 
['Female', '25', "5'7", 'Brown']
bill: 
['Male', '20', "5'5", 'Brown']
What would you like to do? age
20   
What would you like to do? hair             
Brown      
What would you like to do? guess liv                    
You lost...  
```

```
What would you like to do? gender                       
Female                                                                  
What would you like to do? height                                          
5'7
What would you like to do? guess linda                                     
You won!  
```

## Grading 
### Scheme/Rubric
| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| List command | 5   |
| gender/age/height/hair | 10|
| guess command | 5   |
| help command            | 3  |
| quit command       | 2  |
| **Sub total**                                                   | 25  |
| **Technical Correctness   **                                    |     |
| Correct use of dictionaries                                     | 15  |
| Correct use of variables and game loop |10| 
| Correct use of printing/formatting | 10|  
| **Sub total**                                                   | 35  |
| **Total**                                                       | 60 |


