"""
Solution to Problem 23 of Project Euler.

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""


def sum_proper_divisors(n):
    """
    Return the sum of the proper divisors of n.

    Assumption: n >= 2

    >>> sum_proper_divisors(12)
    16
    >>> sum_proper_divisors(28)
    28
    """
    divisor_sum = 1  # 1 is the first proper divisor
    divisor = 2
    other_divisor = n / 2
    while divisor <= n / divisor:
        if n % divisor == 0:
            # We found a proper divisor
            divisor_sum += divisor
            if other_divisor != divisor:
                divisor_sum += other_divisor
        divisor += 1
        other_divisor = n / divisor
    return divisor_sum


def get_all_abundant_numbers_below_28123():
    """Return an array of all abundant numbers <= 28123."""
    abundant_array = []
    for i in range(1, 28124):
        if sum_proper_divisors(i) > i:
            abundant_array.append(i)
    return abundant_array


def sum_1_to_n(n):
    """Return 1 + 2 + ... + n."""
    return (n * (n + 1)) / 2


def sum_the_sums_of_abundant_numbers_below_28123():
    """Return the total of all sums <= 28123 of two abundant numbers."""
    abundant_number_array = get_all_abundant_numbers_below_28123()

    # Set of every number below 28123 that is the sum of two abundant numbers
    abundant_pair_sum_set = set()
    for i in abundant_number_array:
        for j in abundant_number_array:
            if i + j <= 28123:
                abundant_pair_sum_set.add(i + j)
    return sum(abundant_pair_sum_set)


def get_sum_of_non_abundant_sum_numbers():
    """
    Return the sum of every number that is not the sum of two abundant numbers.

    Note: The sum of all positive integers that cannot be written as the sum of
    two abundant numbers is the same as the sum of 1 + 2 + ... + 28123 minus
    the sum of all numbers <= 28123 that are the sum of two abundant numbers.
    (Since every number > 28123 is the sum of two abundant numbers.)
    """
    return sum_1_to_n(28123) - sum_the_sums_of_abundant_numbers_below_28123()


print(get_sum_of_non_abundant_sum_numbers())
