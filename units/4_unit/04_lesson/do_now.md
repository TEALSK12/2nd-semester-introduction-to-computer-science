# Do Now 4.04

## Part 1
1. Type and run the following code: 

    ```python
    # my_building is a representation of the apartments on each floor of my 3 story building
    my_building = [
    ['apt1a', 'apt1b', 'apt1c'],
    ['apt2a', 'apt2b', 'apt2c'],
    ['apt3a', 'apt3b', 'apt3c']
    ]
    print("first floor" + str(my_building[0]))
    print("first floor, 3rd apartment" + str(my_building[0][2]))
    ```

    Write down what was printed. How you would access the 2nd apartment of the 3rd floor (`apt3b`)?
<br>
<br>
<br>

2. Write a for loop that iterates over `my_building` and prints out each value (apartment number). Describe what happened. 
<br>
<br>
<br>

##Part 2

1. Copy the following code into editor:

    ```python
    my_floor = ['apt1a', 'apt1b', 'apt1c']
    ```

    Write a function `apartments_on_floor`.  When given a list of apartments, `my_floor`, `apartments_on_floor` prints out each apartment. 

    <br>
    <br>
    <br>

2. Copy the following code into the editor:

    ```python
    my_building = [
    ['apt1a', 'apt1b', 'apt1c'],
    ['apt2a', 'apt2b', 'apt2c'],
    ['apt3a', 'apt3b', 'apt3c']
    ]
    ```
    Write a function  `apartments_in_building`. `apartments_in_building` prints out every apartment in the building. Use your function `apartments_on_floor`. 
<br>
<br>
<br>