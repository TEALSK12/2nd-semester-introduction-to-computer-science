# Do Now 5.01 

##Introduction to EarSketch
EarSketch, created by Georgia Tech, is an online tool that allows you to learn Python and music technology side by side. By applying concepts already covered in this curriculum such as functions, loops, and conditionals, you will be able to use the EarSketch IDE to create unique and entertaining beats and songs!


1. Skim the EarSketch documentation in [Unit 1](http://earsketch.gatech.edu/category/unit-1)
3. Copy the following code from the reading above into the [EarSketch Editor]: 

```python
# python code
#
# script_name: Intro_Script
#
# author: The EarSketch Team
#
# description: This code adds one audio clip to the DAW
#
#
#

#Setup Section
from earsketch import *
init()
setTempo(120)

#Music Section
fitMedia(TECHNO_SYNTHPLUCK_001, 1, 1, 9)

#Finish Section
finish()
```

What inputs does `fitMedia` take? Press the run button and describe what happened. 

[EarSketch Editor]: http://earsketch.gatech.edu/earsketch2/