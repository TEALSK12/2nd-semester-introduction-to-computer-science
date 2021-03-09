# Lesson 2.01: Data Types & Casting

## Learning Objectives

Students will be able to...

* Define and identify: **type, string, casting, floating point number (float), integer**
* Describe different representations of data in Python
* Convert from one data type to another data type

## Materials/Preparation

* [2.01 Slide Deck](https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/slidedecks/Intro%20Python%202.01%20TEALS.pptx)
* [Do Now][]
* [Lab - Casting][] ([docx][]) ([pdf][])
* [Associated Readings 2.1](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/2.1)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students
* Video Resources
  * [String Concepts](https://youtu.be/tSebLz1hNpA)
  * [Strings Demo](https://youtu.be/zv3cVJHCqXA)

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief  |

## Instructor's Notes

### 1. Do Now

* Project the Do Now on the board, circulate around the class to check that students are working and understand the instructions.

### 2. Lesson

#### Discussion

* Ask students to define **type**. Talk about types as a way to represent data (give examples of `strings`, `int`, and `float`).
* Ask students what they thought typing the command `str(123)` does.

#### Instruction

* Define this process of changing data types as **casting**.
* Define the `int` function if the students were unable to guess it from the Do Now.
* Demonstrate casting `string` to `int` by typing in the following:

```python
    n = int(input())
    9
    type(n)
```

Output from Python:
```
    <class 'int'>
```

* Because Python 3 is strongly typed, concatenating strings and numbers requires casting.  Demonstrate by typing the following:

```python
    n = int(input())
    9
    print ("You entered " + n)
```

Output from Python:
```
    TypeError: Can't convert 'int' object to str implicitly
```

* Cast the integer to a string. Demonstrate by typing the following:

```python
    n = int(input())
    9
    print ("You entered " + str(n))
```

Output from Python:
```
    You entered 9
```

* Take a few minutes to have students write down how they would produce the following output:

```
    Give me a number you want to multiply by 2: 4
    8
```

* Explain to students that in Python
  * when asking for input from the user, the input is automatically stored as a string
  * if the input will be used for calculations or numeric comparisons, it will be necessary to cast it to another data type.

#### Swapping Variables Discussion

* Go over the method of swapping two variables using Python syntax covered so far, with a third temporary variable.
  * Python includes a way to swap two variables directly. The syntax for this will be covered in a later unit.

#### Student Sharing

* Call on 2-3 students to write their answers on the board.
* Discuss what would happen if the user types in 1.5 instead of 4.
* If input is a float, can cast with `float(num)`
* `type`: ask students what they think `type('a')` would output.  
* Why might you want to use `type`?

### 3. Lab

* Practice predicting what casting will do to inputs.
* Create a halving program, and a variant of the same program that converts any fractional output values to whole numbers.
* 

### 4. Debrief

* Check student progress and completion of the lab, wrap up by taking any final questions.

## Accommodation/Differentiation

If students are moving quickly, it is possible to introduce the concepts of Booleans here. Discuss how students would represent binary (0's and 1's). In practice these translate to True and False. Convert numbers to Boolean, and Booleans to numbers.

## Forum discussion

[Lesson 2.01: Data Types and Casting (TEALS Forums Account Required)](https://forums.tealsk12.org/c/2nd-semester-unit-2/lesson-2-01-data-types-casting)
  
[Do Now]:do_now.md
[Lab - Casting]:lab.md

[pdf]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/01_lesson/lab.pdf
[docx]: https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/raw/master/units/2_unit/01_lesson/lab.docx
