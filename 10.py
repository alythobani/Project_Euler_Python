"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(n):
    """
    Returns True if n is prime, else returns False

    Assumption: n >= 2
    """

    factor = 2

    while factor <= n / factor:  # No need to check past square root of n
        if n % factor == 0:
            return False
        factor += 1

    return True


def sum_primes_below_n(n):
    """
    Returns the sum of all prime numbers below n

    Assumption: n >= 3
    """

    sum_of_primes_below_n = 2

    x = 3

    while x < n:
        if is_prime(x):
            print('Found one: %d' % x)
            sum_of_primes_below_n += x
        x += 2  # All primes greater than 2 are odd so we can skip evens

    return sum_of_primes_below_n


print(sum_primes_below_n(10))
print(sum_primes_below_n(2000000))
