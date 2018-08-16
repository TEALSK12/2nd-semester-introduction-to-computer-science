# Lesson Plan 1.05: Quiz & Debugging

## Learning Objectives
Students will be able to...
* Demonstrate their understanding of key concepts covered up to this point
* Define and identify: **debugging, syntax errors**
* Analyze and respond to error messages

## Materials/Preparation
* Quiz (access protected resources by clicking on "Additional Curriculum Materials" on the
  [TEALS Dashboard])
* Associated Reading - section 1.3 of Book
* Take the quiz and create a scoring rubric
* Look through [http://tinyurl.com/TEALS-Python-Errors] web tutorial and [example code] below to
  prepare students for analyzing and responding to errors

## Pacing Guide
| **Duration** | **Description**    |
|-------------:|:-------------------|
|    5 Minutes | Welcome and Review |
|   25 Minutes | Quiz               |
|   25 Minutes | Debugging Activity |

## Instructor's Notes
1. **Welcome and Review**
    * Ask students for any final questions before passing out the quiz.

2. **Quiz**

3. **Debugging Activity**

   * Explain to students that you will now be exploring how to read analyze and respond to errors in
     code.
     * Present students with a longer piece of code that will produce an error (e.g. [code]). Ask
       them to read through it and predict what will be printed out.
     * Remind students that when reading through code we go line by line, as if we are the
       interpreter.
     * Run the code, display the stack trace, and have students analyze the error message reported.
     * Explain that, much like in Snap, **debugging** is the process of tracking and fixing errors
       in your code.

   * Indentation Errors:
     * Errors the students are most likely to have seen
       * "IndentationError: unindent does not match any outer indentation level"
     * Ask student why these errors are caused and how they find/fix this type of error? Suggest
       using the tab key to indent and the shift-tab to remove an indent as ways to avoid the error.
     * Direct students to work through and complete this web tutorial on [debugging]

### Accomodation/Differentiation
Make sure to provide extended time on the quiz for any students that have that requirement in an IEP
or 504 plan.


## Code Example
```Python
favorite_number_str = input("What is your favorite number: ")
birth_month_str = input("What month where you born in: ")

lucky_number = int(favorite_number_str) + int(birth_month_str)
print("Your lucky number is " + lucky_number)
```




## Forum discussion
[Lesson 1.05: Quiz and Debugging (TEALS Forums Account Required)](https://forums.tealsk12.org/c/2nd-semester-unit-1/1-05-quiz-debugging)


[TEALS Dashboard]: http://www.tealsk12.org/dashboard

[http://tinyurl.com/TEALS-Python-Errors]: http://interactivepython.org/runestone/static/thinkcspy/Debugging/KnowyourerrorMessages.html
[debugging]: http://interactivepython.org/runestone/static/thinkcspy/Debugging/toctree.html
[example code]: #code-example
