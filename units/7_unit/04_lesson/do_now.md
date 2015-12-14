# Do Now 

Type and run the following code: 

```
class Pet(object): 
	def __init__(self, name): 
		self.name = name
	
	def make_noise(self): 
		print("Noise!")
		return 
		
class Dog(Pet): 
	"""
	A specific type of Pet! 
	"""
	
dog1 = Dog()
dog1.make_noise()
```

1. Write down what happens when you run this code is run? 
2. Try re-writing the code to make this work properly
3. Write down what happens when you call method make_noise. 