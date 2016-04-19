# Lab 7.04 - Pokemon Classes 
Given the following [example], practice using inheritance to create specific child classes for different types of Pokemon. Create the three child classes below:

1. Water Type
	* When attacking a fire type, the attack is more effective
	* When getting healed the effect is doubled
	* When attacking an Grass type the effect is less effective
	* has a method splash which will print out "Splish Splosh"
2. Fire Type
	* When attacking a water type, the attack is less effective
	* When attacking an earth type the effect is more effective
	* When growl is called should print out "Fire Fire"
3. Grass Type
	* When attacking a water type, the attack is more effective
	* When attacking a fire type the effect is less effective
	* When growl is called should print out "Cheep Cheep"

Note: To check what type a class is you can use `isinstance` which takes in an object, a class and returns a boolean if the object is the type of the inputted class. 

###Example
```python
my_pet = Pet()
isinstance(my_pet, Pet) # returns true
isinstance(my_pet, Dog) # returns false
```


	
[example]: example.py