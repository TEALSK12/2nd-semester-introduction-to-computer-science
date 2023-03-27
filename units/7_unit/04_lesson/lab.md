# Lab 7.04 - `Pokemon` Child Classes

## Overview

Given the following [Sample Code](https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/blob/master/units/7_unit/04_lesson/example.py), practice using inheritance to create specific child classes for different types of `Pokemon`.

### Create the three child classes below

#### 1. Water Type

* When attacking a fire type, the attack is more effective
* When attacking a grass type the effect is less effective
* When `growl` is called print out `Splish Splash`

#### 2. Fire Type

* When attacking a water type, the attack is less effective
* When attacking a grass type the effect is more effective
* When `growl` is called print out "Fire Fire"

#### 3. Grass Type

* When attacking a water type, the attack is more effective
* When attacking a fire type the effect is less effective
* When `growl` is called print out "Cheep Cheep"

**Note**: In order to check what type an object is you can use `isinstance` which takes in an object, a class and returns a Boolean if the object is the type of the inputted class.

### Example Code

```python
my_pet = Pet()
isinstance(my_pet, Pet) # returns true
isinstance(my_pet, Dog) # returns false
```
