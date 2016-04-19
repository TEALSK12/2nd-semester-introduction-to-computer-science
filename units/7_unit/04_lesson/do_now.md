# Do Now 

Type and run the following code: 

```python
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

1. What is output when you run this code?
2. Rewrite the code to resolve the error and make this work properly
3. What happens when you call method `make_noise`?