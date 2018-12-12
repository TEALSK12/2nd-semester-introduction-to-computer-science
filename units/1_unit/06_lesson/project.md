# Project 1: Mad Libs

Using Python, students will use variables, input, and printing to create a Mad Lib. You will also practice *designing* a project by planning out your Mad Lib before implementing it.  Part of the project is to use your creativity to design your own unique story.

## Overview
Mad Libs are a fun way to tell a story. The story is pre-written except for a few missing words.  The story is hidden from the user.  The user is asked a series of questions in order to fill in the missing words before seeing the story. Then the story is read off with the user's words mixed in!

## Details
### Behavior
* The program will print out the title of the Mad Libs story, as well as a short explanation of game play    
    ```
    A Day in NYC: a Mad Lib.
    Welcome! You are about to play a fantastic word game. 
    I will ask you for nouns, verbs, adjectives, proper nouns and adverbs. 
    Using those words I will create an unexpected story for you!
    ```
* The program should then prompt the user to enter in nouns, verbs, adjectives, proper nouns, and adverbs
![Example running](mad_libs_screen_shot.png)
* After all the words have been entered. The program will print out the story.  You will need to create a story of your own choosing.  Keep it clean and fun.  Here is an example of a day in New York City.
```
A Day in NYC: It was a beautiful day in New York City. 
Our hero Ariana Grande was on a walk from the Standard to Duane Reade. 
Ariana Grande was walking rather quickly because he/she had lived in New York for a few months.
All of a sudden a slimey donut appeared out of nowhere!!! 
Ariana Grande decided to prance foolishly instead of dealing with the situation.
Thrown off from Duane Reade, Ariana Grande decides to go to Times Square instead.
What a beautiful day in New York. 
```

### Implementation Details
Plan out your story on pencil and paper first, before you start implementing the program.
* Create your story
* Select the missing words
* Determine each words part of speech
* Create introduction
* Create questions
* Divide story into print statements

As mentioned above the program must request words from the user. The following **must** be included in the program: 
* 10 different words inputted
* Variable names should correspond to the part of speech requested and part of the story they belong to (e.g. `noun1`, `verb2`, etc)
* You may only use 3 print statements to tell your story

## Grading 
### Scheme/Rubric
| **Functional Correctness(Behavior)**                                |     |
| --------------------------------------------------------------- |-----|
| Program greets user and explains rules  | 3   |
| Program accurately requests 10 words (1 for word, 1 for correct request)| 20|
| Program prints full Mad Lib | 10   |
| Program exhibits creativity               | 2   |
| **Sub total**                                                   | 35  |
| **Technical Correctness   **                                    |     |
| Program utilizes variable names to convey meaning               | 5  |
| Correct order of inputted words                                 | 10  |
| Only 3 print statements                                         | 10  |
| **Sub total**                                                   | 25  |
| **Total**                                                       | 60 |


