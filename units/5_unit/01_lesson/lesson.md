#Lesson 5.01: Earsketch Intro 

##Learning Objectives
Students will be able to...

* Define and identify: **Digital Audio Workstation (DAW)**, **sound tab**, `fitMedia()`, `setTempo()`
* Playing beats using the functions
* Loop through items in a list
* Be aware of the scope of variables during iteration 

##Materials/Preparation
* [Do Now]
* [Lab]
*  Associated Reading in EarSketch
*  Read through the Do Now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Debrief     |

## Instructor's Notes

1. **Do Now**
    * Display the Do Now on the board
2. **Lesson**
	* Ask what phrases the students wrote down or remembered from the reading. 
		* **DAW**: The main tool for producing music on a computer is the Digital Audio Workstation, or DAW. A DAW is a piece of computer software for recording, editing, and playing digital audio files. Audio files store information that the computer uses to play back music. In the context of a DAW, these audio files are called clips. The DAW allows you to edit and combine multiple clips simultaneously on a musical timeline, and to see and hear how they line up over time. It also makes it easy to synchronize clips with each other. DAWs are used in both professional recording studios and in home laptop-based studios. Two popular DAWs are Pro Tools and Logic Pro.
		* **Sound Browser - Sounds Tab**: Here, you can browse and search a collection of short pre-made audio clips for you to use in your music. 
		* **Sound Browser - Scripts Tab**: A list of your saved EarSketch projects. Each script is a separate music project. Click a project title to open it in a new tab (in the code editor panel).
		* **Sound Browser - API Tab**: A description of every EarSketch function. We will learn more about this later.
		* **Digital Audio Workstation (DAW)**: A timeline view of your current song, showing which audio clips you have added to the song and when they come in. It lets you hear your song, and also visualize its structure.
		* **Code Editor**: A text editor with numbered lines. Type your code here, press "Run", and it will turn into music in the DAW. 
		* **console**
		* **setTempo()** comes with a default argument of 120, but let's change it to 100. This sets the tempo of our project to 100 beats per minute. As you can see, the name of a function tells you what it does.
		* **fitMedia()** to add sound to the DAW. fitMedia() requires four arguments: clip name; track number; starting measure; ending measure. In other words, you tell it the name of the audio clip you want to add to the DAW, which track to put it on, and which measures to put it between. For now, just type in fitMedia() without any arguments.
3. **Lab**
	* Practice updating the songs 
4. **Debrief**
	* Talk about any of the phrases or issues the students had. Did they find it easy to understand the code when they read it.
	* Have students read the next part(s) of the guide in EarSketch documentation. 



[Do Now]: do_now.md
[Lab]: lab.md