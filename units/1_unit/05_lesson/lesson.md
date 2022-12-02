# Lesson Plan 1.05: Quiz & Debugging

## Learning Objectives

Students will be able to...

* Demonstrate their understanding of key concepts covered up to this point.
* Define and identify: **debugging, syntax errors**.
* Analyze and respond to error messages.

## Materials/Preparation

* [1.05 Slide Deck](https://github.com/Areson/2nd-semester-introduction-to-computer-science/raw/master/units/1_unit/slidedecks/Intro%20Python%201.05%20TEALS.pptx)
* Download quiz and Answer key(access protected resources by clicking on "Additional Curriculum Materials" on the [TEALS Dashboard][])
* [Associated Readings 1.3](https://tealsk12.github.io/2nd-semester-introduction-to-computer-science/readings.md#associatedreadings/1.3)
* Take the quiz.
* After taking the quiz yourself, take a look at the answer key provided in the additional curriculum materials.
* Create a scoring rubric
* Look through [debugging][] web tutorial to dig deeper yourself into analyzing and responding to errors.

## Pacing Guide

| **Duration** | **Description**    |
|-------------:|:-------------------|
|    5 Minutes | Welcome and Review |
|   25 Minutes | Quiz               |
|   25 Minutes | Debugging Activity |

## Instructor's Notes

### 1. Welcome and Review

* Ask students for any final questions before passing out the quiz.

### 2. Quiz

### 3. Debugging Activity

* Explain to students that you will now be exploring how to read analyze and respond to errors in code.

* Ask students to read through it and predict what will be printed out.

  ```Python
  favorite_number_str = input("What is your favorite number: ")
  birth_month_str = input("What month where you born in: ")
  lucky_number = int(favorite_number_str) + int(birth_month_str)
  print("Your lucky number is " + lucky_number)
  ```

* Remind students that when reading through code we go line by line, as if we are the interpreter.

#### Demonstration

* Run the code, display the stack trace, and have students analyze the error message reported.
* Explain that **debugging** is the process of tracking. and fixing errors in your code.
* Indentation Errors: Errors the students are most likely to have seen
  * `IndentationError: unindent does not match any outer indentation level`
* Ask student why these errors are caused and how they find/fix this type of error? Suggest using the tab key to indent and the shift-tab to remove an indent as ways to avoid the error.
* Direct students to work through and complete this web tutorial on [debugging][].

### Accommodation/Differentiation

Make sure to provide extended time on the quiz for any students who need extra time.

[TEALS Dashboard]: http://www.tealsk12.org/dashboard

[debugging]: https://runestone.academy/ns/books/published/fopp/Debugging/toctree.html
[example code]: #code-example
