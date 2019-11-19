# Lab 2.03 - Can I or Can't I?

1) In your notebook, predict if each of the following will produce a `True` or `False` output. Check your answers in interactive mode. 

    ### Example 1

    ```
        >>> a = 100
        >>> b = "science"
        >>> a > 75 and b == "science" 
    ```

    | **Predicted Output** | **Actual Output** |
    | --- | --- |
    |<br> |<br> | 

    ### Example 2

    ```
        >>> a = 100
        >>> b = "science"
        >>> a > 75 and b != "science" 
    ```
    | **Predicted Output** | **Actual Output** |
    | --- | --- |
    |<br> |<br> | 

    ### Example 3

    ```
        >>> a = 100
        >>> b = "science"
        >>> a > 75 or b != "science" 
    ```
    | **Predicted Output** | **Actual Output** |
    | --- | --- |
    |<br> |<br> | 

    ### Example 4

    ```
        >>> a = 100
        >>> b = "science"
        >>> c = True
        >>> not c and a > 75 and b == "science" 
    ```
    | **Predicted Output** | **Actual Output** |
    | --- | --- |
    |<br> |<br> | 

## In your Console
### Complete the following:

2) Create a "Can I be President?" program, which determines if the user meets the minimum requirements for becoming the President of the United States. Use user input. The rules for being president of the U.S. are: 
    * Older than 35
    * Resident of US for 14 Years
    * Natural born citizen
    * Print `True` if the person could be president and `False` if they can't be president. 

3) Alter one line of that program to be a "I can't be President?" game. Print `True` if the user cannot be President and `False` if they can be President.

4) Create a "Can I ride the roller coaster?" program. A roller coaster has the rule that a rider has to be over the height of 50 inches. Because of a legal loophole, if you are over the age of 18 you can ride regardless of your height. If you are allowed to ride, the coaster costs 4 quarters (although the operator accepts tips so more money is appreciated). 

    * Also, the theme park sells frequent rider passes: with a frequent rider pass the roller coaster costs only 2 quarters. Ask the user how tall they are in inches, their age, how many quarters they have, and if they have a frequent rider pass. Print `True` if the person can ride and `False` if they can't. 


# Bonus!
### Are the following expressions equivalent? Research DeMorgan's Laws and write why you think they are the same or why they are not the same. 

`not(x or y) == not x and not y`

`not(x and y) == not x or not y`
