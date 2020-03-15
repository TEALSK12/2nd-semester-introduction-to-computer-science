import random

#print(random.randint(1, 6))

def roll6():
    for i in range(6):
        print(square(random.randint(1,6)))
    return
    
    
def square(x):
    return x * x

    
def main():
    roll6()
    
    print(square(100))
    
    return

main()

