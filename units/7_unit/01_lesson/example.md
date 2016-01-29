# Example 
1. Read the following code: 

```python
class Pet(object): 
 """Represents a pet"""

my_pet_1 = Pet() 
my_pet_1.type = 'cat'
my_pet_1.noise = 'meow'
my_pet_1.full_name = 'Snuffles McGruff'

my_pet_2 = Pet()
my_pet_2.type = 'cat'
my_pet_2.noise = 'meow'
my_pet_2.full_name = 'Snowpounce Flury'

my_pet_3 = Pet()
my_pet_3.type = 'cat'
my_pet_3.noise = 'meow'
my_pet_3.full_name = 'Snickers Snorkel'

my_pets = [my_pet_1, my_pet_2, my_pet_3]
print(type(my_pets))
for pet in my_pets: 
    print(pet.full_name)
```
