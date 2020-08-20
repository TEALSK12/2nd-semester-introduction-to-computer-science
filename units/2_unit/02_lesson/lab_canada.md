# Lab 2.02 - Can I or Can't I

## In your Notebook

Predict if each of the following examples will produce a `True` or `False` output. Check your answers in interactive mode.

### Example 1

```python
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b == "science"
```

### Example 2

```python
    >>> a = 100
    >>> b = "science"
    >>> a > 75 and b != "science"
```

### Example 3

```python
    >>> a = 100
    >>> b = "science"
    >>> a > 75 or b != "science"
```

### Example 4

```python
    >>> a = 100
    >>> b = "science"
    >>> c = True
    >>> not c and a > 75 and b == "science"
```

## In your Console

### Complete the following coding challenge

1. Create a "Can I be Prime Minister?" program, which determines if the user meets the minimum requirements for becoming the Prime Minister of Canada. Have the user input the information needed.
   In Canada, the PM is not directly elected.  Political parties try to win a majority of seats in a general election to form a government. 
   
    **The minimum requirements to be Prime Minister of Canada are:**

    * You must be a Canadian Citizen.
    * You must be at least 18 years old on election day.
    * You have been elected as the leader of a Political Party.
    * If you are not a member of a Party, then you must run as an Independent.
    * You cannot be a member of more than one Party.
    * Print `True` if the person could be Prime Minister and `False` if they can't be Prime Minister

2. Create a "I can't be Prime Minister?" program. Print `True` if the user cannot be Prime Minister and `False` if they can be Prime Minister.

---

#### Emphasize with students...

#### BC Mathematics Computer Science 11 and ADST Computer Programming 11 - Connecting and Reflecting
#### BC Core Competencies - Social Responsibility

Adapt this program to connect with other levels of leadership or influence in your community:  Civic level (Mayor);  Provincial level (Premier);  
First People's Elders or Band leaders.  How are these positions elected or chosen?  What is the reason for the logic behind some of these requirements?  While the path to becoming Prime Minister may seem complicated, we can use boolean logic and democratic reasoning to better understand the process and its merits. 

Extension: Many of your students may have career paths in mind, and post-secondary goals.  Ask students to consider the path to becoming a .... [insert a post-secondary/position/career/job here] (Examples: Engineering students at UBC, optometrist, a professional hockey player).   There are many requirements, or "ducks to align" along the way.   What pre-requisite courses do you need?  Do you need highschool graduation?  What language or science courses do you need?  What is the university's admissions requirement, and the faculty's admission requirement?   What is the tuition or savings required?  Are you staying in residence or at home?   Life is full of boolean logic!  

---

3. Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated).

    * Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print `True` if the person can ride and `False` if they can't.

## Bonus

### Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same

`not(x or y) == not x and not y`

`not(x and y) == not x or not y`
