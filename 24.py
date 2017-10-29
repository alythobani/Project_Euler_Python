"""
Solution to Problem 24 of Project Euler.

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""


def find_all_permutations(digit_array):
    """Return an array of all permutations of digits in digit_array."""
    if len(digit_array) == 1:
        return [[digit_array[0]]]
    permutation_array = []
    for e in digit_array:
        digit_array_copy = digit_array[:]
        digit_array_copy.remove(e)
        permutation_array_starting_at_e = []
        remaining_permutations = find_all_permutations(digit_array_copy)
        for permutation in remaining_permutations:
            new_permutation = [e] + permutation
            permutation_array_starting_at_e.append(new_permutation)
        permutation_array.extend(permutation_array_starting_at_e)
    return permutation_array


print(find_all_permutations([0, 1, 2]))
print(find_all_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999])
