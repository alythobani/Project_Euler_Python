"""
Solution to Problem 37 of Project Euler.

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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


def is_truncatable(p):
    """
    Return True if p is truncatable, else return False.

    Assumption: p > 10 and p is odd

    >>> is_truncatable(3797)
    True
    >>> is_truncatable(94)
    False
    """
    if p > 99:
        # Every digit can be a unit digit for a truncation of p, so must be odd
        #  and not equal to 5
        for digit in reversed(str(p)):
            if digit not in ['1', '3', '7', '9']:
                return False
    for i in range(len(str(p))):
        if not is_prime(int(str(p)[i:])) or not is_prime(int(str(p)[:i + 1])):
            return False
    return True


def print_answer():
    """Print the answer."""
    truncatable_count = 0
    truncatable_set = set()
    i = 11
    while truncatable_count < 11:
        if is_truncatable(i):
            print('Found one: %d' % i)
            truncatable_set.add(i)
            truncatable_count += 1
        if i % 10 == 7:
            # Skip unit digits 9 and 1 since they are not prime
            i += 6
        elif i % 10 in [3, 9]:
            # Skip unit digits 5 and 1 since they are not prime
            i += 4
        else:
            i += 2
    print('Set: %s' % truncatable_set)
    print('Count: %d' % truncatable_count)
    print('Sum: %d' % sum(truncatable_set))


print_answer()
