# Project- Final Project Alternative or Supplement (True North Edition)
# The Financial Calculator Project

* [printable project spec][]
* [editable project spec][]

Students will design, plan, and implement a medium- to large-scale 
final project involving financial literacy.  Students can work individually, or with a partner. 

## Overview

During this course, you have learned a huge amount about 
computer science and programming in general, and Python in particular.  
In this project, you will put all of that knowledge, 
along with some new skills you will develop around design, 
planning, and project management, to build a relatively large and 
complex financial application that _you_ choose.  
You should 
ultimately produce a project that is interesting, useful, and challenging.
To enhance the efficacy of the financial application, you will learn how to read user input data from a CSV file, 
and possible provide output via a file as well. 

---

### Emphasize with students ...

#### BC ADST Mathematics Computer Science 11 Content - Use of Computing for Financial Analysis

Use this opportunity to apply software to do financial calculations.
Afterall, what's tedious for a human, may be easy for a computer.
It's up to the software developer to design a product that takes advance of the computer's powers,
to give the user a smooth experience and helpful product. 

Think about the most recent times when you used a calcuator. 
These are possible candidates.  When and why did you need to use calculator?
The computer is also great to processing lots of data with accuracy and speed.
What are some financial scenarios where we need to record and analyze lots of data?

Here are some examples:
- Student loan calculator and tracker
- Holiday budget planner, currency convertor, and expense tracker
- Personal budget and expense/income tracker
- Post-secondary "Dream School" financial cost calculator and analyzer and planner 

---


## Details

### 1. Project Phases

This project will be significantly larger in scope than any of your previous assignments, so there will be more design and planning than before.  More importantly, though, rather than be given a well-defined specification, _YOU_ will be setting the requirements for your project by coming up with an idea, fleshing out the details, and defining the steps necessary to complete your program.

To help you through this process, there will be several steps to this project.  You must complete **all** of the steps **in order** for your project to be successful.  In fact, _half_ of your grade will be based not on how well your program works, but on how well you completed the design and planning process.

The project includes these applied design phases: 

1. _Understanding Context_ - Conduct user centred research to understand design opportunities and barriers
2. _Ideating_ - Establish point of view, generate and prioritize ideas, analyze competing social, ethical, and sustainability considerations; list out user stories and features
3. _Prototyping_ - Choose an appropriate form, scale, and level of detail for prototyping multiple ideas; analyse the design for the life cycle, and construct prototype, making changes to tools, materials, and procesures as needed; record iterations of prototyping
4. _Testing_ - Identify feedback, develop an appropriate way to test prototype, collect feedback and critically evaluate design and makes changes; iterate or abandon design idea
5. _Making_ - Task project management processes (task management schedule) to work collaboratively to coordinate production, ensuring that your software goals are met
6. _Sharing_ - Share progress; design an how to promote product with end-users; critically reflect on design thinking and processes, identify new design goals and future work

---

### Emphasize with students ...

#### BC ADST Computer Programming 11 Big Ideas - The Design Cycle 
#### Curricular Competencies for Applied Design 

Software development process is iterative and agile process.
The actual "coding" is done during Phase 5 "Making".  
Before the designer dives into coding, it is crucial to spend enough time flushing through the idea, and doing some sketches of what using the program will look like.  

The Prototype phase is meant to be quick and efficient, using materials that are easily available.   This can be a pencil and paper sketch of a flowchart, and sketch of the software interface, what things will look like when the client uses the software.   What does input (and data format) does it prompt from the user?  What output will it generate?  

The Testing phase here refers to testing the prototype design, and not seeing if your code works.   It means getting others (possibly potential users) to look at your prototype, and see if its usage makes sense.  Give the tester a scenario, and ask them what they would do, and then tell them what result or action would happen next.  The tester's response and feedback should be observed and used to make a new iteration of the design. 

Note: Generally, using the console to type/read input/output is not user-friendly.  Therefore, in this project, we can solve this problem by learning how to read/write data from a file.  (See note about parsing CSV files below).   It may not be as pretty as a graphical interface, but as least it's efficient.  In fact, when a scientist or financial analyst is focussed on crunching numbers and analyzing results, they prefer skipping the graphical interface, and working with data that is create/provided in a simple text format.   It is also common practice in business applications to interface data with a program like Excel, which is why the CSV format is convenient. 

---

### 2. Progress Tracking

In phase 3, you will complete a Final Project Spec and in phase 4 you will complete a Final Project Schedule.  These documents will be your guides in the development Making phase and will help you stay on track and aware of your progress.  Throughout the development phase of the project, you will be expected to keep your spec and plan up-to-date and make adjustments as you get ahead or behind, as requirements change, or as tasks or features get re-prioritized.  At the end of each coding day, your spec and plan documents should be updated to reflect the current state of your project, and you will check in with an instructor at least once a week to make sure things are on track.  

### 3. Implementation Requirements

#### Complexity and Creativity

Your final project should be sufficiently complex and large-scale to push your limits as a programmer, but not so sophisticated that you are not able to complete it in the time allotted.  The complexity in your project should come from the _design_ and the _algorithms_ and not from the _code_.  (That is, you cannot meet the complexity requirement simply by writing a lot of code.  Your code must be challenging or interesting in some meaningful way.)  In addition, you should not add complexity by introducing peripheral elements, such as graphics or sound effects.  (Your program can certainly have these, but they will not be considered in determining the projects complexity.)

In addition, one of the main goals of this project is to allow you to unleash your creativity and allow you to create something of interest to you.  To achieve this, your project must show some level of creativity or personalization that makes it your own.  Simply creating your own version of some existing application will not fully meet this requirement.

For both the complexity and creativity requirements, you should talk to the instructors early and often to ensure your project is in line with our expectations.

---

### Emphasize with students ...

#### BC ADST Mathematics Computer Science 11 Curricular Competencies - Understanding and solving; Apply flexible and strategic appoaches to solving problems.

In our course so far, students know how to use the console to get input from a user, and to display output. 
In an actual financial application, a GUI (graphical user interface) is needed to make it easy for a client to use the software,
especially when more than one piece of input information is required from the user. 
Another possible approach is to read the information (input data) from a file that the user prepares ahead of time.

One popular input data format is the CSV (comma separated file) that can be created by a spreadsheet program like excel.
Python has a built in CSV parser library that we can use.  
Students should first try these exercises as practice:  https://realpython.com/python-csv/

---

#### Documentation and Style

As with all previous projects, your program must be well-written, well-documented, and readable.  Writing code with good style is always a good idea, but in a project of this size and scope, following style guidelines will help you keep your thoughts organized and make it easier to keep track of your progress, pick up where you left off each day, and find and fix bugs.  In particular, though this is certainly not a comprehensive list, pay attention to the following:

* organizing your functions/code so that they can be read and comprehended easily
* giving your functions, variables, lists, and dictionaries descriptive and meaningful names
* using the right data type (`string`, `int`, `bool`, `float`, `dictionary`, `class`) for each situation
* include comments to describe the structure of your program and track your progress
* avoiding redundancy with good use of loops, functions, and/or lists, and/or dictionaries, and/or classes
* practicing good procedural decomposition and abstraction

#### Required Python Elements

In order to show that you have fully mastered all the skills from the course, you project must include at least the following:

1. A clear way to start the program, and clear prompts or instructions for any user interaction
2. At least one loop, variable, function, and list, and more as necessary or appropriate
3. Each of these must be used correctly and meaningfully

    * creating a list that contains  
    * a single element just to meet this requirement will not earn points

4. at least one user interaction
5. this can be prompting for information using ask, responding to key presses or mouse movements, or any other action that keeps the user involved

#### Required Checkpoints

At least three times during the project period, and at least once each week, you should check in with an instructor to ensure that your project is on track, that you are meeting the project requirements, and that you have the answers to any questions that might have arisen during your work.  The course staff will work with you to set up a schedule for these checkpoints, but it is **your responsibility** to ensure that the meetings take place.

#### Suggested Pacing Plan

- Day 1 - project introduction, team formation (if working with partner), brainstorm, prepare some survey or interview questions to help validate your caluclator idea. 
- Day 2 - prototype and testing, sketch out solution and input/outputs, do a small example of what the input CSV would look like, and what the output would look like;  get feedback from peers
- Day 3 - start of learning how to read and write data with CSV files, re-visit your design to see that it still make sense, ie
   * is it easy and convenient for the user?
   * does the sequence of events make sense?
   * is the output meaningful and useful?
- Day 4-6 - provide detailed breakdown of tasks to focus on getting one feature at a time working; as the students are coding, they should test small amounts of code at a time, and revisit the initial design plan to see if everything still makes sense for the user
- Day 7 - sharing and presentation day to external clients and friends

[printable project spec]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/8_unit/project.pdf
[editable project spec]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/8_unit/project.docx
