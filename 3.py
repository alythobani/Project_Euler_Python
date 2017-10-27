"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    """
    Determines if n is a prime number.
    Assumed: n >= 2
    """
    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        factor += 1
    return True


def get_prime_factors(n):
    """
    Retrieves a set of prime factors of n
    Assumed: n >= 2
    """

    prime_factor_list = set()

    factor = 2

    while factor <= n / factor:

        if n % factor == 0:

            if is_prime(factor):
                prime_factor_list.add(factor)
            else:
                prime_factor_list = prime_factor_list | get_prime_factors(
                    factor)

            prime_factor_list = prime_factor_list | get_prime_factors(
                n / factor)

        factor += 1

    return prime_factor_list if prime_factor_list else set([n])

for i in range(2, 20):
    print('Prime factors of %d: %s' % (i, get_prime_factors(i)))

print('Prime factors of 13195: %s' % get_prime_factors(13195))

print('Prime factors of 600851475143: %s' % get_prime_factors(600851475143))
