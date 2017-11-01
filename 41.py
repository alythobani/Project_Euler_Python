"""
Solution to Problem 41 of Project Euler.

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""


def is_prime(n):
    """
    Return True if n is prime, else return False.

    Assumed: n >= 2
    """
    if n == 1:
        return False

    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        factor += 1
    return True


def find_all_permutations(number_string):
    """Return an array of all permutations of digits in number_string."""
    if len(number_string) == 1:
        return [number_string]
    permutation_array = []
    for index, digit in list(enumerate(number_string)):
        other_digits = number_string[0:index] + number_string[index + 1:]
        permutation_array_starting_at_digit = []
        remaining_permutations = find_all_permutations(other_digits)
        for permutation in remaining_permutations:
            new_permutation = digit + permutation
            permutation_array_starting_at_digit.append(new_permutation)
        permutation_array.extend(permutation_array_starting_at_digit)
    return permutation_array


def get_largest_pandigital_prime():
    """Return the largest pandigital prime, or None."""
    i = 9
    while i > 3:
        digits_string = ''
        for j in range(1, i):
            digits_string += str(j)
        for number in reversed(find_all_permutations(digits_string)):
            if is_prime(int(number)):
                return number
        i -= 1
    return None


print(get_largest_pandigital_prime())
