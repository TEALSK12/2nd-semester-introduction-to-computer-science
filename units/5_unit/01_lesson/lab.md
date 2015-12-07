# Lab 5.01
Let's make our own script using the structure above.

1. To begin, open the Code Editor, and click Options. Select New Script. This will give you a template to fill in with music. Make sure you are signed in, then save your script. Add a script name, your name, and a description in the comments section. Label your sections with comments, as in the image above. Empty lines don't effect how the program runs, so add as many as you need to make space for each section. The music section will be empty for now.

2. The function setTempo() comes with a default argument of 120, but let's change it to 100. This sets the tempo of our project to 100 beats per minute. As you can see, the name of a function tells you what it does.

3. In our music section, let's call a function named fitMedia() to add sound to the DAW. fitMedia() requires four arguments: clip name; track number; starting measure; ending measure. In other words, you tell it the name of the audio clip you want to add to the DAW, which track to put it on, and which measures to put it between. For now, just type in fitMedia() without any arguments.

4. Let's pick some audio clips to add with fitMedia(). Open up the sound browser, and select the Sounds tab. We're going to do some instrumentation:  choosing the combination of instruments for a composition. Let's go with a typical rock instrumentation: drums, bass, and guitar. Search in the sound browser for clips with 'drum' in the name, and find one you like by pressing the play button next to them. Click your text cursor in the parentheses of  fitMedia(), and use the copy button (next to the clip you want to add to your song) in the sound browser to add your chosen clip as an argument. You can also just type it, if you like, but make sure it is in all-caps! Audio clip names MUST BE IN CAPS.

5. We want the drum clip added to track 1, so the 2nd argument in  fitMedia() should be the number 1. Our clip should start on the first measure, so the 3rd argument is 1. If we want our clip to play for one measure, the end measure should be 2 (meaning we stop at the beginning of measure 2). So our 4th argument should be 2. Your function should look something like this: fitMedia(Y01_DRUMS_1, 1, 1, 2). 

6. Now we'll add some bass. We will basically repeat steps 3-5, by adding a new  fitMedia() call on the line below our previous one. In this new  fitMedia() , find a bass clip to add as an argument, just like you found the drums. Clips that are in the same folder in the sound browser are designed to sound good together, so try to choose clips from the same folder. We can only have one clip at a time on a given track, so tell  fitMedia() that this goes on track 2. Finally, choose a range of measures to fit the clip into, probably between measures 1 and 2 like before.

7. Repeat step 6, but add a guitar clip instead of a drum clip. With any luck, your code looks something like ours below, but with different clips. Press 'Run', and then play the music you made!


