# Lesson 2.07: Project 2 - Text Monster

## Learning Objectives

Students will be able to...

* Use knowledge of lists, booleans, conditionals, and while loops to create a text-based adventure game.

## Materials/Preparation

* [Project Spec - Text Monster] ([printable project Spec]) ([editable project spec])
* [Text Monster Starter Code](https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/07_lesson/text_Monster_Starter_Code.py)
)
* Solution (access protected resources by clicking on "Additional Curriculum Materials" on the [TEALS Dashboard])
* Update the Project Spec as needed to meet your grading requirements
* Try creating your own variation on the Text Monster code so you are familiar with the potential challenges and bugs your students will hit.
* Review [4 Steps to Solve Any CS Problem]
* [Associated Readings 2.7](https://tealsk12.gitbook.io/intro-cs-2/readings#2-7)
* [Editable Grading Rubric](https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/07_lesson/rubric.docx)

### Day 1 Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 10 Minutes | Project Overview/Demo|
| 40 Minutes | Design      |
| 5 Minutes | Debrief  |

### Days 2 - 9 Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 10 Minutes | Review      |
| 40 Minutes | Project Work|
| 5 Minutes | Debrief  |

## Instructor's Notes

### 1. 4 Steps to Solve Any CS Problem

* Review [4 Steps to Solve Any CS Problem]

### 2. Project Overview/Demo

* Distribute the project spec to all students and walk them through the goals and requirements of the project.
* Show a demo of a completed project.
* Go over specific design considerations from the project spec:
* Introduce the concept of global variables and how they will be useful here.
* Identify the importance of the "User Pocket" and how to use a list along with `append` and `remove` for this information.

### 3. Design

* Have students stay at their desks and write down what lists they'll need.
* They should break up the project into parts: parsing user input, keeping track of players position, returning what is at the player's position .

### 4. Debrief/Review

* During discussion and warp up at the end of class, get a feeling for where students are in the project.
* During the review the next morning cover the topics/areas that students are struggling on and present tips, suggestions, and goals for that day.

## Accommodation/Differentiation

* Make sure to do status checks with all students throughout the project.
* Identify students that are struggling on the project after the first few days and provide additional scaffolding & support as needed.
* For any students that are advancing rapidly through the project, give them extension ideas such as adding a new feature or floor to the game.
* Advanced students can also be paired as tutors/helpers with struggling students.

## Grading

| Functional Correctness (Behavior)                               |     |
| --------------------------------------------------------------- |-----|
| Game has three floors                                           | 5   |
| User can move `left` or `right`, but not beyond the rooms       | 10  |
| User can only move `up` or `down` at an appropriate staircase   | 5   |
| `Grab` adds an item to the users collected items                | 5   |
| User can only collect 3 items                                   | 2   |
| `Help` lists all possible commands                              | 2   |
| Monsters either disappear if user has a sword or defeat the user| 5   |
| A sword can only be used once and then it disappears            | 6   |
| Boss monster needs sword and magic stones to be defeated        | 5   |
| Prize is blocked by boss monster                                | 5   |
| **Sub total**                                                   | 50  |
| **Technical Correctness**                                       |     |
| Correctly use of lists                                          | 15  |
| Correctly appends items to list of users collected items        | 15  |
| Correctly uses if statements to check items in user's possession | 15  |
| Correctly using `or` statements and `and` statements            | 15  |
| **Sub total**                                                   | 60  |
| **Total**                                                       | 110 |

## Forum discussion

[Lesson 2.07: Text Game (TEALS Discourse Account Required)](https://forums.tealsk12.org/c/2nd-semester-unit-2/lesson-2-07-text-game)

[Project Spec - Text Monster]: project.md
[Text Monster Game - Example Code]: project_file.py
[TEALS Dashboard]:http:/www.tealsk12.org/dashboard
[4 Steps to Solve Any CS Problem]:https://github.com/TEALS-IntroCS/2nd-semester-introduction-to-computer-science-principles/raw/master/units/4%20Steps%20to%20Solve%20Any%20CS%20Problem.pdf
[printable project Spec]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/07_lesson/project.pdf
[editable project spec]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/07_lesson/project.docx
