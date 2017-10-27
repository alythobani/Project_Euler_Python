"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def is_prime(n):
    """
    Returns True if n is a prime number, else returns False.
    Assumed: n >= 2
    """
    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        factor += 1
    return True


def get_prime_factorization_dict(n):
    """
    Returns a dict of the prime factors that multiply to n
    Assumed: n >= 2

    >>> get_prime_factorization_dict(2)
    {2: 1}
    >>> get_prime_factorization_dict(6)
    {2: 1, 3: 1}
    >>> get_prime_factorization_dict(24)
    {2: 3, 3: 1}
    """

    def add_prime_factor_dicts(dict1, dict2):
        """
        Returns a dict of the sum of prime factor frequencies in two dicts

        >>> add_prime_factor_dicts({3: 1, 5: 2, 11:7}, {3: 3, 5: 1, 7: 1})
        {3: 4, 5: 3, 7: 1, 11: 7}
        """
        for k in dict2:
            dict1[k] = dict1.get(k, 0) + dict2[k]
        return dict1

    factor = 2

    if is_prime(n):
        return {n: 1}

    while factor <= n / factor:

        if n % factor == 0:
            return add_prime_factor_dicts(
                get_prime_factorization_dict(factor),
                get_prime_factorization_dict(n / factor))

        factor += 1

    return [n]


for i in range(2, 20):
    print('Prime factorization of %d: %s' %
          (i, get_prime_factorization_dict(i)))


def lowest_common_multiple_for_all_numbers_below_n(n):
    """
    Returns the smallest positive number that is evenly divisible by all the
    numbers from 1 to n
    """

    def max_prime_factor_frequency_dict(dict1, dict2):
        """
        Takes in two dictionaries dict1 and dict2 of frequencies of prime
        numbers.
        Returns a dictionary of the max frequencies across each dict.

        >>> max_prime_factor_frequency_dict({3: 2, 5: 6}, {3: 3, 5: 1, 7: 1})
        {3: 3, 5: 6, 7: 1}
        """
        for k in dict2:
            dict1[k] = max(dict1.get(k, 0), dict2[k])
        return dict1

    prime_factor_frequency_dict = {}
    for i in range(2, n):
        prime_factor_frequency_dict = max_prime_factor_frequency_dict(
            prime_factor_frequency_dict,
            get_prime_factorization_dict(i))

    lcm = 1
    for k in prime_factor_frequency_dict:
        lcm *= (k**prime_factor_frequency_dict[k])

    return lcm

print(lowest_common_multiple_for_all_numbers_below_n(10))
print(lowest_common_multiple_for_all_numbers_below_n(20))
