#Do Now: 3.03

Open up the terminal. Type the following code into the editor. 

```
import random
# inputs:  x, int
           y, int
# outputs: int 
# 50% returns sum of x and y, 50% returns product of x and y
def mystery_functions(x, y):
	random_number = random.randint(0,2)
	if random_number > 0: 
		z = x + y 
	else: 
		z = x * y
	return z
mystery_function(1, 2)
```

What happens in this code? How do you know what the result was? 
<br>
<br>
<br>

Keeping the function the same, rewrite the code to print out the value to the function? 
<br>
<br>
<br>