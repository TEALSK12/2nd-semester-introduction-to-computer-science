# Lab 3.04 - Aliasing & Scope

##Aliasing 
* Will updating b affect a? Explain why or why not? 
    
    ```python
        a = [1, 2, 4]
        b = a 
      ```
    <br>
    
* Predict what `my_list` list will print out when this code is run. If you are not sure check the code by copying and running it. 
    
     ```python
     # input: a list of ints
     # output: an int
     def update_list(a_list): 
     	if len(a_list) > 5: 
     		a_list[3] = "yo"
     		b = a_list[4]
     		c = a 
     	return c
     my_list = [1, 2, 3, 4, 5]
     update_list(my_list)
     ```
    <br>
    
##Scope
* Draw a stack diagram for the following:
    
    ```python
	var_1 = "kittens"
	var_2 = "cookies"
	
	# input: a string
	# output: a string
	def my_function(my_favorite_things): 
		song_lyrics = "rain drops on roses,"
		combined_song = song_lyrics + my_favorite_things
		return combined_song
		
	# input: a string
	# output: a string	
	def my_function_2(item, item2): 
		full_lyrics = item + "on " + item2
		full_song = my_function(full_lyrics)
		return full_song
		
	my_song = my_function_2(var_1, var_2)
     ```
    <br>
     
* Describe what is wrong with the following code. Then write out how to fix it. If you are unsure copy and run the code and fix it. 

```python
var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet): 
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2: 
        print("My favorite pet is the dog.")

print_out_my_favorite(var_1)
```

* Write a program that has a global variable, my_num. Create three functions that update my_num: 
    1. add2: this function adds 2 to my_num
    2. multiply_num: this function takes in a parameter, multiplier, and multiplies my_num by that parameter
    3. add2_and_multiply: this function takes in a parameter, multiplier, and calls both add2 and multiply_num. 


