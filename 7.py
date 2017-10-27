"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
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


def nth_prime_number(n):
    """
    Returns the nth prime number

    Assumption: n >= 2
    """

    prime_number_count = 0

    x = last_prime_number = 2

    while prime_number_count < n:
        if is_prime(x):
            last_prime_number = x
            prime_number_count += 1
        x += 1

    return last_prime_number

print(nth_prime_number(6))
print(nth_prime_number(10001))
