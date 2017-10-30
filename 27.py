"""
Solution to Problem 27 of Project Euler.

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 <= n <= 39.

However, when n=40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and
certainly when n=41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80
primes for the consecutive values 0 <= n <= 79. The product of the
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| <= 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
"""


def is_prime(q):
    """
    Return True iff q is a prime number.

    Assumed: q >= 2 or q <= -2
    """
    if q < 0:
        q = -q
    factor = 2
    while factor <= q / factor:  # No point checking past the square root
        if q % factor == 0:
            return False
        factor += 1
    return True


def get_quadratic_result(a, b, n):
    """Return n^2 + an + b."""
    return n**2 + a * n + b


def get_number_of_consecutive_quadratic_primes(a, b):
    """
    Return the number of consecutive prime quadratic results starting at n = 0.

    The quadratic result of a and b is given by n^2 + an + b, for n >= 0.
    """
    consecutive_prime_count = 0
    n = 0
    q = get_quadratic_result(a, b, n)
    while is_prime(q):
        consecutive_prime_count += 1
        n += 1
        q = get_quadratic_result(a, b, n)
    return consecutive_prime_count


def get_coefficients_with_most_consecutive_prime_quadratic_results():
    """
    Return a and b with the most consecutive prime quadratic results.

    Outputs:
    a: integer with |a| < 1000
    b: integer with |b| <= 1000
    """
    best_a = None
    best_b = None
    highest_consecutive_prime_count = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            consecutive_prime_count = \
                get_number_of_consecutive_quadratic_primes(a, b)
            if consecutive_prime_count > highest_consecutive_prime_count:
                print('New best count: %d' % consecutive_prime_count)
                print('a=%d, b=%d' % (a, b))
                highest_consecutive_prime_count = consecutive_prime_count
                best_a = a
                best_b = b
    return (best_a, best_b)


print(get_number_of_consecutive_quadratic_primes(1, 41))
print(get_number_of_consecutive_quadratic_primes(-79, 1601))
(a, b) = get_coefficients_with_most_consecutive_prime_quadratic_results()
print('a: %d\nb: %d' % (a, b))
print('Answer: %d' % (a * b))
