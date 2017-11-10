"""
Solution to Problem 49 of Project Euler.

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways:
(i) each of the three terms are prime, and
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""


def is_prime(n):
    """
    Return True if n is prime, else return False.

    Assumed: n >= 2
    """
    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        factor += 1
    return True


def find_all_permutations(number_string):
    """Return a list of all permutations of digits in number_string."""
    if len(number_string) == 1:
        return [number_string]
    all_permutations = []
    for index, digit in list(enumerate(number_string)):
        other_digits = number_string[0:index] + number_string[index + 1:]
        for permutation in find_all_permutations(other_digits):
            all_permutations.append(digit + permutation)
    return all_permutations


def solve():
    """Return a set of appropriate 12-digit numbers as described above."""
    numbers_that_work = set([])
    for n in [i for i in range(1000, 10000) if is_prime(i)]:
        permutations_of_n = find_all_permutations(str(n))[1:]
        for perm in permutations_of_n:
            if int(perm) <= n or not is_prime(int(perm)):
                continue
            delta = int(perm) - n
            perm_plus_delta = int(perm) + delta
            if str(perm_plus_delta) in permutations_of_n:
                if is_prime(perm_plus_delta):
                    print('Found one!!! %s + %s = %s, %s + %s = %s' %
                          (n, delta, perm, perm, delta, perm_plus_delta))
                    numbers_that_work.add(str(n) + perm + str(perm_plus_delta))
    return numbers_that_work


print(solve())
