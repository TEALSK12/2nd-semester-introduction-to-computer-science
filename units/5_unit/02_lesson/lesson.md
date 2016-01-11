#Lesson 5.02: EarSketch Music

##Learning Objectives
Students will be able to...

* Define and identify: **rhythm**, **beat**, **tempo**, **measures**, **setEffect()**, **makeBeat()**
* Play beats using the functions
* Loop through items in a list
* Be aware of the scope of variables during iteration 

##Materials/Preparation
* [Do Now]
* [Lab]
* Associated Reading in EarSketch
*  Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students

## Pacing Guide
| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 10 Minutes | Debrief     |

## Instructor's Notes

1. **Do Now**
    * Students should be given time to read unit 2 of the EarSketch documentation.
    * Students are expected to write down key terms as they read.
2. **Lesson**
	* Ask what phrases and terminology the students wrote down or remembered from the reading. 
		* **Rhythm**: describing how the music moves through time.
		* A **beat** is the basic unit of time in music. If you have ever clapped along to a song, you were probably clapping on each beat. So how long does a beat last? The length depends on the overall speed of the song, called the tempo. **Tempo** is measured in beats per minute (bpm). If we are clapping at 60 bpm, then each beat lasts one second. At 120 bpm, each beat takes half a second. The higher the bpm, the faster the song, the shorter the duration of each beat.
		* Beats are grouped into **measures**. In EarSketch, measures always have four beats.
		* `setEffect()`: add an effect to a track. Takes parameters: track number, effect name, effect parameter, effect value
		* `makeBeat()`: instead of composing at the measure-level, we can work at the note-level. Takes parameters: clip name, track number, measure number, beat string
3. **Lab**
	* Follow the EarSketch instructions below to use the `makeBeat()` function
	* Create a simple song with 2 uses of fitMedia, 2 uses of makeBeat and 1 use of effect. 
	* Students can use looping and if statements if they would like 
4. **Debrief**
	* Talk about new functions, questions about data types and using strings.



[Do Now]: do_now.md
[Lab]: lab.md