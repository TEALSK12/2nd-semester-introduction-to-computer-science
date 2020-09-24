# Project 1: Mad Libs (True North Edition)

Using Python, students will use variables, input, and printing to create a Mad Lib. You will also practice *designing* a project by planning out your Mad Lib before implementing it.  
Part of the project is to use your creativity to design your own unique story.

## Overview

Mad Libs are a fun way to tell a story. The story is pre-written except for a few missing words.  The story is hidden from the user.  
The user is asked a series of questions in order to fill in the missing words before seeing the story.
Then the story is read off with the user's words mixed in!

---

### Emphasize with students

#### BC ADST Computer Programming 11 - Connecting and Reflecting

Use this opportunity to create a Mad Lib that tells the stories of our times.
Technology is used to connect people with the things they care about.
The field Digital Media, for example, is where digital artifacts are created to communicate messages to the world.
In a Mad Lib, the user in engaged by providing word input.
This adds a random twist, and possibly some humour, into the story.

Some possible story themes:

* Current events in the world/
* First People's heritage, where learning is embedded in memory, history, and story  (Resource: http://firstnationstories.com/)
* Daily life in your part of the world.
* A camping adventure.
* Amazing race adventure (Refere/nce:  https://en.wikipedia.org/wiki/The_Amazing_Race_Canada)
* Adventure challenge (Reference: https://en.wikipedia.org/wiki/Eco-Challenge)/
* Master chef cooking adventure (Reference: https://en.wikipedia.org/wiki/MasterChef_Canada)/

---

## Details

### Behavior

* The program will print out the title of the Mad Libs story, as well as a short explanation of game play

    ```python
    A Summer Day: a Mad Lib.
    Welcome! You are about to play a fantastic word game.
    I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
    Using those words I will create an unexpected story for you!
    ```

* The program should then prompt the user to enter in nouns, verbs, adjectives, proper nouns, and adverbs

    ```python
    A Summer Day: a Mad Lib
    Instructions. The program will prompt for a type of word to enter. After all words are entered the program will print a story
    Enter a proper noun: Shawn Mendes
    Enter a shop in the neighbourhood: Rocky Point Ice Cream Shop
    Enter another place (city/town): Coquitlam
    Enter an adverb: quickly
    Enter a colour: green
    Enter brand name of a type of shoes: Nike
    Enter a good item: donut
    Enter an adjective: slimy
    Enter an adverb: foolishly
    Enter a verb (past tense): pranced
    Enter a social media: Instagram
    Enter an adjective: interesting

    ```

* After all the words have been entered. The program will print out the story.  
You will need to create a story of your own choosing.  
Keep it clean and fun.  
Tips: Have a mix questions that more general, and more specific.
Here is an example of a day in Coquitlam, BC.

    ```python
    A Summer Day: a Mad Lib
    It was a beautiful day in Coquitlam. Our hero Shawn Mendes went out to explore the great outdoors.
    First, he went to get some essentials from Rocky Point Ice Cream Shop.
    Shawn quickly walked through the shop, in green coloured Nike shoes.
    Suddenly a slimy donut appeared out of nowhere!!!
    Our hero foolishly pranced all the way home, eager to post on Instagram.
    He did not make it to the park.
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

* 10 different words input
* Variable names should correspond to the part of speech requested and part of the story they belong to (e.g. `noun1`, `verb2`, etc.)
* You may only use 3 print statements to tell your story
