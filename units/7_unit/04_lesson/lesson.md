# Lesson 7.04: Inheritance

## Learning Objectives

Students will be able to...

* Define and identify: **inheritance**,  **parent class**, **child class**.
* Create a class that inherits from anther class.
* Override methods of parent class in a child class.

## Materials/Preparation

* [7.04 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/7_unit/slidedecks/Intro%20Python%207.04%20TEALS.pptx)
* [Do Now][]
* [Lab - Pokemon Child Classes][] ([docx][]) ([pdf][])
* [Associated Reading](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/7.4)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 30 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes

### 1. Do Now

* Display the Do Now on the board.
* Students will explore an example of a new `Dog` class inheriting the methods of the `Pet` class.

### 2. Lesson

#### Instruction - Inheritance

* when you create a new class that is a subclass of the original (ex. the `Dog` class "inherits" the properties/methods of the `Pet` class.)

#### Discussion

* Ask students: what is the difference between the `Dog` declaration and the `Pet` declaration?
* Discuss the error and what was missing in the original code.

#### Instruction - Parent and Child Class

* When a class inherits from another class, the class it inherits from is called the **parent class** and the class that inherits is called the **child class**.
* Ask: in the example from the do now, which is the child and which is the parent?
* Child classes gain access to all the methods of the parent class.
* What does `dog1.make_nosie()` print out?
* Child classes can also override their parent classes. Have the students practice overriding `make_noise` in the `Dog` class so that the dog will print out `bark bark`.
  * A child can override any method, including `__init__`, and can add methods and attributes that are not in the parent class.
  * Overriding a method in one child class does not affect instances of the parent class and another child class could override the method in its own unique way.

### 3. Lab

* Given a generic Pokemon class, create three child classes that represent different types of Pokemon.
* Consider demonstrating the creation of one of the child classes before having students start the lab independently.

### 4. Debrief

* Go over students' questions. Ask what questions the students have and review instance, class, methods, `init`, `str`, etc.

## Accommodation/Differentiation

In the Pokemon lab, students may need clarification regarding how to use `isinstance` and how to manipulate the `defend` method to meet the requirements of each child class. Consider demonstrating the creation of one child class for all students before having students work on the lab.

[Do Now]:do_now.md
[Lab - Pokemon Child Classes]:lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/7_unit/04_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/7_unit/04_lesson/lab.docx
