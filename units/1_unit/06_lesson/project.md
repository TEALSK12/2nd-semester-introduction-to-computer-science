# Project 1: Mad Libs

Using Python, students will use variables, input, and printing to create a Mad Lib. You will also practice *designing* a project by planning out your Mad Lib before implementing it.  Part of the project is to use your creativity to design your own unique story.

## Overview

Mad Libs are a fun way to tell a story. The story is pre-written except for a few missing words.  The story is hidden from the user.  The user is asked a series of questions in order to fill in the missing words before seeing the story. Then the story is read off with the user's words mixed in!

## Details

### Behavior

* The program will print out the title of the Mad Libs story, as well as a short explanation of game play

    ```python
    A Day in NYC: a Mad Lib.
    Welcome! You are about to play a fantastic word game.
    I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
    Using those words I will create an unexpected story for you!
    ```

* The program should then prompt the user to enter in nouns, verbs, adjectives, proper nouns, and adverbs

    ```python
    Day in New York City: A Mad Lib
    Instructions. The program will prompt for a type of word to enter. After all words are entered the program will print a story
    Enter a proper noun: Ariana Grande
    Enter a place: The Standard
    Enter another place: Duane Reade
    Enter an adverb: quickly
    Enter a noun: donut
    Enter an adjective: slimy
    Enter an adverb: foolishly
    Enter a verb: prance
    Enter a place: Times Square
    Enter an adjective: beautiful
    It was a beautiful day in New York City Our hero Ariana Grande was on a walk from the Standard Duane Reade.Ariana rather than quickly because he/she lived in New York for a few months. Suddenly a slimy donut appeared out of nowhere!!!

    ```

* After all the words have been entered. The program will print out the story.  You will need to create a story of your own choosing.  Keep it clean and fun.  Here is an example of a day in New York City.

    ```python
    A Day in NYC: It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because he/she had lived in New York for a few months. Suddenly, a slimy donut appeared out of nowhere!!! Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade, Ariana Grande decides to go to Times Square instead. What a beautiful day in New York.
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
* Variable names should correspond to the part of speech requested and part of the story they belong to (e.g. `noun1`, `verb2`, etc)
* You may only use 3 print statements to tell your story
