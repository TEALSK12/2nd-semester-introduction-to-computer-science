## Lesson 4.05 Debugging 
## The n-th triangular number is the sum of numbers from 1 to n. 
## Expected output: 1, 3, 6, 10
## Credit: David Miller 

def triangular_num(a_list): 
  for i in range(0, len(a_list)):
    sum = 0   
    for j in range(0, a_list[i]):
        sum += j
    print(sum)

num_list = [1, 2, 3, 4]
triangular_num(num_list)

