# Functional Prompt Solution
from functools import reduce

def flatten_and_sort(array):
    # Flattening the array using reduce and lambda
    flattened = reduce(lambda acc, sublist: acc + sublist, array, [])
    # Sorting the flattened array
    sorted_array = sorted(flattened)
    return sorted_array

# Example usage
array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
result = flatten_and_sort(array)
print(result)  # Output should be [1, 2, 3, 4, 5, 6, 7, 8, 9]
