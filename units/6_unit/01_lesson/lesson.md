# Lesson 6.01: Introduction to Dictionaries

## Learning Objectives

Students will be able to...

* Define and identify: **dictionary**, **key**, **value**.
* Create dictionaries of key-value pairs.
* Access items from dictionaries.

## Materials/Preparation

* [6.01 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/slidedecks/Intro%20Python%206.01%20TEALS.pptx)
* [Do Now][]
* [Lab - Dictionary of Internet Abbreviations][] ([docx][]) ([pdf][])
* [Associated Reading](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/6.1)
* Read through the do now, lesson, and lab so that you are familiar with the requirements and can assist students.

## Pacing Guide

| **Duration**   | **Description** |
| ---------- | ----------- |
| 5 Minutes  | Do Now      |
| 10 Minutes | Lesson      |
| 35 Minutes | Lab         |
| 5 Minutes | Debrief     |

## Instructor's Notes

### 1. Do Now

* Display the [Do Now][] on the board.
* Students will copy and edit code involving creating a dictionary and accessing items from that dictionary.

### 2. Lesson

#### Instruction - Dictionaries

* Ask the students what *type* they think `my_dictionary` is.
* `my_dictionary` is a **dictionary** or a collection of **key-value** pairs.
* You use the key to look up the value in the dictionary.
* Keys and values can be of any type. The syntax is: `{key : value, key : value, ...}`

#### Discussion

* Did anyone run the `type()` function to find out what type 'my_dictionary' is?
* Ask: what are the keys in the example from the Do Now? What are the associated values?
* Ask the students what `my_dictionary['dog']` did, and if this syntax reminds them of anything (lists!).

#### Instruction - Square Brackets

* To get the value associated with a key in a dictionary you use square brackets.
* You can also use `my_dictionary.get()`, which will return `None` if the key isn't there.
* *Note*: You can pass in a second argument to `get` which takes the place of the `None` default.

#### More Discussion

* Ask how students would get the value for `chair` or `car`.
* Discuss what happened when students ran `my_dictionary['kittens']`.

#### 'in' keyword

* Explain that this error is common and means that there is no value in the dictionary.
To avoid this error, use the `in` keyword with an `if` statement. If a certain key
is `in` a specified dictionary, it will return `True`. Otherwise it will return `False`.

#### Example

 ```python
 my_dictionary = {'a': 1, 'b': 2, 'c': 3}
 if 'a' in my_dictionary:
     print("It's there!")
 else:
     print("It's missing!")
 ```

### 3. Lab

* Students will create a dictionary translating common phrases into their meanings.

### 4. Debrief

* Review what was covered in today's lesson and check for understanding of the three concepts covered: **dictionaries**, **keys,** and **values**.

## Accommodation/Differentiation

* If any students are struggling with today's lesson, be prepared to offer additional examples of the usefulness of having key-value pairs.
* Students that are moving quickly through the lab should work on the bonus and research how to add new key/value pairs to a dictionary.

[Do Now]: do_now.md
[Lab - Dictionary of Internet Abbreviations]: lab.md
[pdf]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/01_lesson/lab.pdf
[docx]: https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/6_unit/01_lesson/lab.docx
