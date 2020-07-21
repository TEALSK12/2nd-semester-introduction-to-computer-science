# Project 1: Mad Libs (True North Edition)

Using Python, students will use variables, input, and printing to create a Mad Lib. You will also practice *designing* a project by planning out your Mad Lib before implementing it.  
Part of the project is to use your creativity to design your own unique story.

## Overview

Mad Libs are a fun way to tell a story. The story is pre-written except for a few missing words.  The story is hidden from the user.  
The user is asked a series of questions in order to fill in the missing words before seeing the story. 
Then the story is read off with the user's words mixed in!   

---

### Emphasize with students ...

#### Curriculum Competencies - Connecting and reflecting

Use this opportunity to create a Mad Lib that tells the stories of our times. 
Technology is used to connect people with the things they care about.
The field Digital Media, for example, is where digital artifacts are created to communicate messages to the world. 
In a Mad Lib, the user in engaged by providing word input. 
This adds a random twist, and possibly some humour, into the story. 

Some possible story themes:
* Current events in the world
* COVID-19 related daily life
* First People's heritage, where learning is embedded in memory, history, and story
* Daily life in your part of the world 
* Amazing race adventure
* Master chef cooking adventure

---

## Details

### Behavior

* The program will print out the title of the Mad Libs story, as well as a short explanation of game play

    ```python
    A Day in Quarantine: a Mad Lib.
    Welcome! You are about to play a fantastic word game.
    I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
    Using those words I will create an unexpected story for you!
    ```

* The program should then prompt the user to enter in nouns, verbs, adjectives, proper nouns, and adverbs

    ```python
    Day in Quarantine: A Mad Lib
    Instructions. The program will prompt for a type of word to enter. After all words are entered the program will print a story
    Enter a proper noun: Shawn Mendes
    Enter a shop in the neighbourhood: Rocky Point Ice Cream Shop
    Enter another place (city/town): Coquitlam
    Enter an adverb: quickly
    Enter a colour: cyan
    Enter brand name of a type of shoes: Nike
    Enter a good item: donut
    Enter an adjective: slimy
    Enter an adverb: foolishly
    Enter a verb (past tense): pranced
    Enter a social media: instagram
    Enter an adjective: interesting

    ```

* After all the words have been entered. The program will print out the story.  
You will need to create a story of your own choosing.  
Keep it clean and fun.  
Tips: Have a mix questions that more general, and more specific. 
Here is an example of a day in Coquitlam, BC.

    ```python    
    A Day in Quarantine:  
    It was a beautiful day in Coquitlam. Our hero Shawn Mendes was not allowed to leave the house.
    The only place our hero went to for groceries was Rocky Point Ice Cream Shop. 
    Today was shopping day.  Shawn quickly walked out with a cyan face mask, and Nike shoes. 
    Suddenly a slimy donut appeared out of nowhere!!!
    Our hero foolishly pranced all the way home to post on instagram.
    It was an interesting day indeed. 
    ```

### Implementation Details

Plan out your story on pencil and paper first, before you start implementing the program.

1. Create your story
2. Select the missing words
3. Determine each words part of speech
4. Create introduction
5. Create questions
6. Divide story into print statements

As mentioned above the program must request words from the user. The following **must** be included in the program:

* 10 different words inputted
* Variable names should correspond to the part of speech requested and part of the story they belong to (e.g. `noun1`, `verb2`, etc.)
* You may only use 3 print statements to tell your story
