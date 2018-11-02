# Do Now 5.01 

##Introduction to EarSketch
EarSketch, created by Georgia Tech, is an online tool that allows you to learn Python and music technology side by side. By applying concepts already covered in this curriculum such as functions, loops, and conditionals, you will be able to use the EarSketch IDE to create unique and entertaining beats and songs!


1. Skim the following lessons in the EarSketch documentation in [Unit 1], located in the right panel of the [EarSketch Editor].

* 1.1.2 [Tools of the Trade: DAWs and APIs](https://earsketch.gatech.edu/earsketch2/?curriculum=1-1-1)
* 1.1.3 [The EarSketch Workspace](https://earsketch.gatech.edu/earsketch2/?curriculum=1-1-2)
* 1.1.6 [The DAW in Details](https://earsketch.gatech.edu/earsketch2/?curriculum=1-1-5)
* 1.1.9 [Creating a New Script](https://earsketch.gatech.edu/earsketch2/?curriculum=1-1-8)
* 1.1.10 [Compising in EarSketch - fitMedia()](https://earsketch.gatech.edu/earsketch2/?curriculum=1-1-9)

2. Copy the following code from the reading above into the [EarSketch Editor]: 

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
