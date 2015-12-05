def boxes_to_buy(num_needed, sizes):
    result = {}
    remaining = num_needed

    for size in sizes:
        result[size] = remaining // size
        remaining = remaining % size

    if remaining > 0:
        result[min(sizes)] += 1  # add one of the smallest pack-size if there are any left :)

boxes_to_buy(96, [3, 5, 7])