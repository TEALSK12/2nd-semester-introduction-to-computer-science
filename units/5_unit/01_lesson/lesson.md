
Lesson 5.01: Earsketch Intro
====================================================================================================

**Note:** Unit 5 involves a tool called EarSketch from Georgia Tech. EarSketch is a Digital Audio
Workstation with an embedded scripting environment that supports Python or Javascript. Using
EarSketch, students can create songs by writing Python code. All of the Earsketch activities require
you to use the EarSketch Editor instead of the IDE you have been using so far (_e.g._ Repl.it).


Learning Objectives
----------------------------------------------------------------------------------------------------

Students will be able to...

* Define and identify: **Digital Audio Workstation (DAW)**, **sound tab**, `fitMedia()`,
  `setTempo()`
* Play beats using the above functions
* Loop through items in a list
* Be aware of the scope of variables during iteration 


Materials/Preparation
----------------------------------------------------------------------------------------------------
  - [Do Now]
  - [Lab - Intro to EarSketch]
  - [EarSketch Editor]
  -  Associated Reading in EarSketch
  -  Read through the do now, lesson, and lab so that you are familiar with the requirements and can
     assist students


Pacing Guide
----------------------------------------------------------------------------------------------------
|   Duration | Description |
|-----------:|:------------|
|  5 Minutes | Do Now      |
| 15 Minutes | Lesson      |
| 30 Minutes | Lab         |
|  5 Minutes | Debrief     |


Instructor's Notes
----------------------------------------------------------------------------------------------------

### 1. Do Now
  - Display the Do Now on the board.
  - Students are introduced to EarSketch and the functions `setTempo()` and `fitMedia()`.

### 2. Lesson
  Ask the students what phrases the students wrote down or found most important from the reading.
  - **DAW**: The main tool for producing music on a computer is the Digital Audio Workstation, or
    DAW. A DAW is a piece of computer software for recording, editing, and playing digital audio
    files. Audio files store information that the computer uses to play back music. In the context
    of a DAW, these audio files are called clips. The DAW allows you to edit and combine multiple
    clips simultaneously on a musical timeline, and to see and hear how they line up over time. It
    also makes it easy to synchronize clips with each other. DAWs are used in both professional
    recording studios and in home laptop-based studios. Two popular DAWs used in the music industry
    are Pro Tools and Logic Pro.
  - **Sound Browser - Sounds Tab**: Here, you can browse and search a collection of short pre-made
    audio clips for you to use in your music. 
  - **Sound Browser - Scripts Tab**: A list of your saved EarSketch projects. Each script is a
    separate music project. Click a project title to open it in a new tab (in the code editor
    panel).
  - **Sound Browser - API Tab**: A description of every EarSketch function. We will return to this
    in later lessons.
  - **Digital Audio Workstation (DAW)**: A timeline view of your current song, showing which audio
    clips you have added to the song and when they come in. It lets you hear your song, and also
    visualize its structure.
  - **Code Editor**: A text editor with numbered lines. Type your code here, press "Run", and it
    will turn into music in the DAW. 
  - **Console**
  - `setTempo()`: comes with a default argument of 120, but let's change it to 100. This sets the
    tempo of our project to 100 beats per minute. As you can see, the name of a function tells you
    what it does.
  - `fitMedia()`: to add sound to the DAW. fitMedia() requires four arguments: clip name; track
    number; starting measure; ending measure. In other words, you tell it the name of the audio clip
    you want to add to the DAW, which track to put it on, and which measures to put it between. For
    now, just type in `fitMedia()` without any arguments.

### 3. Lab
  - Practice updating songs by entering different arguments into the `fitMedia()` function. 

### 4. Debrief
  - Talk about any of the phrases or issues the students had. 
  - Take time to review the key terms and functions introduced today
  - Have students read the next part(s) of the guide in EarSketch documentation. 

### Accommodation/Differentiation

Students that are moving quickly can read additional documentation on the EarSketch website in order
to move ahead and expand their skills and understanding.

Some students may need reminders about certain music terminology (tempo, measure, beat, _etc._).


## Forum discussion
[Lesson 5.01: Earsketch Intro (TEALS Discourse Account Required)](https://forums.tealsk12.org/c/2nd-semester-unit-5-earsketch/lesson-5-01-earsketch-intro)


[Do Now]: do_now.md
[Lab - Intro to EarSketch]: lab.md
[EarSketch Editor]: http://earsketch.gatech.edu/earsketch2/
