"""
Solution to Problem 47 of Project Euler.

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""


def get_prime_factors(n):
    """Return a set of prime factors of n."""
    factor = 2
    while factor <= n / factor:
        if n % factor == 0:
            return set([factor]).union(get_prime_factors(n / factor))
        if factor > 2:
            factor += 2
        else:
            factor += 1
    return set([n])


def num_distinct_prime_factors(n):
    """Return the number of distinct prime factors of n."""
    return len(get_prime_factors(n))


def get_answer(n=2):
    """Return the 1st of the 1st 4 consecutive numbers with 4 prime factors."""
    while True:
        if num_distinct_prime_factors(n + 3) != 4:
            n += 4
        elif num_distinct_prime_factors(n + 2) != 4:
            n += 3
        elif num_distinct_prime_factors(n + 1) != 4:
            n += 2
        elif num_distinct_prime_factors(n) != 4:
            n += 1
        else:
            return n


print('Answer: %d' % get_answer())
