# Project 6: Guess Who (Hockey Canada Edition)

Hockey is part of Canada's DNA.  Every hockey fan must know their favourite team's mascot.
In Guess Who (Hockey Canada Edition) you’ll be building a text version of a classic board game to guess the mascot character of a Canadian Hockey team.
Dictionaries will be the key to this project.

## Overview

The game should store information on at least 5 different mascots.
Each character should have a name, primary colour, jersey colour, clue about the mascot, clue about the city, some fun fact.

When the game begins, a character should be randomly selected by the computer. The player can ask for 2 pieces of information about the random character, and then has to make a guess as to who was picked.

### Behavior/Commands

* list: list out all the character's names
* Ask for a piece of information by typing these key words
  * colour:  (primary colour of mascot)
    * jersey:  (primary colour of jersey/outfit)
    * animal: (some clue about the animal)
    * city: (some clue about the city)
    * ff: (some fun fact about the mascot)
* guess `name`: guess a character
* help: displays all commands
* quit: exits the game

### Implementation Details

* To store and access the information you’ll need to use dictionaries, which will allow for quick and direct access.
* Research some information about each of the mascot characters:
  * Harvey the Hound (Calgary Flames):  [https://www.nhl.com/flames/fans/harvey](https://www.nhl.com/flames/fans/harvey)
    * Fin the Whale (Vancouver Canucks): [https://www.nhl.com/canucks/fans/fin](https://www.nhl.com/canucks/fans/fin)
    * Youppi! the Giant (Montreal Canadiens): [https://www.nhl.com/canadiens/news/youppi-finds-a-new-home/c-488911](https://www.nhl.com/canadiens/news/youppi-finds-a-new-home/c-488911)
    * Hunter (Edmonton Oilers): [https://www.nhl.com/oilers/fans/hunter](https://www.nhl.com/oilers/fans/hunter)
    * Carlton (Toronto Maple Leafs): [https://toronto-maple-leafs.fandom.com/wiki/Carlton_the_Bear](https://toronto-maple-leafs.fandom.com/wiki/Carlton_the_Bear)
    * Moose (Winnipeg Jets): [https://www.nhl.com/jets/community/mick-e-moose](https://www.nhl.com/jets/community/mick-e-moose)
    * Sparty (Ottawa Senators): [https://www.nhl.com/senators/fans/about-spartacat](https://www.nhl.com/senators/fans/about-spartacat)

---

#### Emphasize with students

#### BC Mathematics 12 Computer Science Big Ideas - Data Representation

Data structures allow us to understand and solve problems efficiently.  

A dictionary is one type of collection data structure.  Unlike the English language dictionary where one word can have several possible definitions/values (eg the word "crane" can mean a bird, or a lifting machine),  in computer science, dictionary keys are unique.  There is only one value for each key.  For example, in our hockey mascot dictionary, there is only one value for the key "colour".  How would you store a collection of mascots?  One way solution is a dictionary of dictionaries.  

---

### Example Output

```python
What would you like to do? list
Fin (Vancouver Canucks):
['black', 'blue', "mammal", 'near waters', 'loves swimming']
Carlton (Toronto Maple Leafs):
['white', 'blue', 'furry', 'near waters', 'drafted 1995']
Hunter (Edmonton Oilers):
['brown', 'orange', 'furry', 'by flatlands', 'born 2012']
Moose (Winnepeg Jets):
['brown', 'blue', 'herbivore', 'by flatlands', 'born 1993']
Harvey the Hound (Calgary Flames):
['gray', 'yellow', '200lbs', 'by mountains', 'wears a cap']
Youppi! the Giant (Montreal Canadiens):
['orange', 'red', 'furry', 'near waters', 'wears a cap']
Sparty (Ottawa Senators):
['orange', 'red', 'furry', 'by a canal', 'born 1992']

What would you like to do? colour
orange
What would you like to do? ff
born 1992
What would you like to do? guess hunter
You missed...  
```

```python
What would you like to do? animal
furry
What would you like to do? jersey
red
What would you like to do? guess youppi!
You scored!  
```

## Grading

### Scheme/Rubric

| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| List command | 5   |
| Mascot characteristics | 10|
| guess command | 5   |
| help command            | 3  |
| quit command       | 2  |
| **Sub total**                                                   | 25  |
| **Technical Correctness**                                    |     |
| Correct use of dictionaries                                     | 15  |
| Correct use of variables and game loop |10|
| Correct use of printing/formatting | 10|  
| **Sub total**                                                   | 35  |
| **Total**                                                       | 60 |
