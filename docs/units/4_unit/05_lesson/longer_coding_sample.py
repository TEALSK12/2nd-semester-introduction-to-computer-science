## Lesson 4.05 Debugging - Sample Code 
## Packs of 20, 5 and 3. The user needs 96.
## Expected output: [4, 3, 1]

def boxes_to_buy(num_needed, sizes):
    result = []
    index = 0
    remaining = num_needed

    for size in sizes:
        result.append(remaining // size)
        remaining = remaining % size
        index += 1

boxes_to_buy(96, [20, 5, 3])
