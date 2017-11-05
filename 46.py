"""
Solution to Problem 46 of Project Euler.

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from math import sqrt


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


def generate_next_prime():
    """Generate the next prime, starting from 3."""
    p = 3
    while True:
        yield p
        p += 2
        while not is_prime(p):
            p += 2


def is_sum_of_a_prime_and_twice_a_square(n):
    """Return whether n can be written as <some prime> + 2 * <some square>."""
    prime_generator = generate_next_prime()
    p = prime_generator.next()
    while p <= n - 2:
        square = (n - p) / 2
        root = sqrt(square)
        if int(root) == root:
            return True
        p = prime_generator.next()
    return False


def solve():
    """Solve the problem."""
    composite = 33
    while True:
        if not is_sum_of_a_prime_and_twice_a_square(composite):
            return composite
        composite += 2
        while is_prime(composite):
            composite += 2


print('Answer: %d' % solve())
