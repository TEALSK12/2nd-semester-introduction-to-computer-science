# Lab 2.05

1. Predict what will be printed. Then run the program and confirm. 
    *  
    *  ```
        a = ['a', 'b', 'c', 'd', 'e']
        print(a[0])
        print(a[3])```
    <br>
    *  
    *  ```
        a = ['a', 'b', 'c', 'd', 'e']
        print(a[len(a) - 3])```
    <br>
    
    *  
    *  ```
        a = ['a', 'b', 'c', 'd', 'e']
        print(a[len(a) - 6])```
    <br>
    
    *  
    *  ```
        a = ['a', 'b', 'c', 'd', 'e']
        a[3] = 'haha'
        print(a)```
    <br> 
    

2. Remember the game show program from last lab? Create this game again using lists, and indexes. Updated Rules Below: 
    * Declare 10 prizes (prize0, prize1, prize2 at the top of your file)
    * User picks a number.
    * Print prize associated with the door user picked 

3. Create a quiz to help you choose which college/pet/tv-show you should got to/get/watch! The style of this quiz game is that each answer from index-0 adds 1 point to School0, each answer from index-1 adds 1 point to School0. At the end print out the schools and the scores for each school. 
    * Create a list of 5 options of colleges/pets/tv-shows
    * Create a list of 5 0s, representing the user's votes so far
    * Create 4 questions. Each question should have five different answers. Each answer corresponds to the specific option.
    * At the end print off the 5 different schools and the score the user got for each of those schools. 

Extra Credit: Research nested lists and work through the following: 
* 
*  ```
    a = ['a', 'b', 'c', ['d', 'e']]
    print(len(a))```
<br>
*
*  ```
    a = ['a', 'b', 'c', ['d', 'e']]
    b = a[3]
    print(b)```
<br>

How would you access 'd' from the list `a`? 