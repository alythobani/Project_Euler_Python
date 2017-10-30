"""
Solution to Problem 26 of Project Euler.

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""


def get_length_of_recurring_cycle_in_reciprocal(d):
    """
    Return the length of the decimal representation's recurring cycle for 1/d.

    If the remainder on a step is ever 0, then 1/d has a finite decimal
    representation and there is no recurring cycle (so we return 0).

    If there is a recurring cycle, we will know its length based on when a
    step's remainder is the same as a previous remainder we have encountered.

    >>> get_length_of_recurring_cycle_in_reciprocal(3)
    1
    >>> get_length_of_recurring_cycle_in_reciprocal(2)
    0
    >>> get_length_of_recurring_cycle_in_reciprocal(7)
    6
    """
    def get_dividend(n, r):
        """
        Return the dividend for a long division step.

        It should be the first r * 10^p greater than or equal to n.

        Inputs:
        n: the divisor
        r: the remainder from the last step

        Assumptions:
        n and r are positive integers
        r < n

        >>> get_dividend(1, 1)
        1
        >>> get_dividend(8, 1)
        10
        >>> get_dividend(10, 1)
        10
        >>> get_dividend(38, 3)
        300
        >>> get_dividend(100, 28)
        280
        >>> get_dividend(129, 13)
        130
        """
        p = 0
        dividend = r
        while dividend < n:
            p += 1
            dividend = r * (10**p)
        return dividend

    # Find what initial number to divide into
    dividend = get_dividend(d, 1)
    remainder = dividend % d
    remainder_set = set()
    cycle_length = 0
    while remainder != 0 and remainder not in remainder_set:
        remainder_set.add(remainder)
        dividend = get_dividend(d, remainder)
        remainder = dividend % d
        cycle_length += 1
    return cycle_length


def get_longest_recurring_cycle_reciprocal_denominator_below_x(x):
    """Return d < x such that 1/d has the longest recurring cycle length."""
    longest_cycle_length = 0
    longest_cycle_length_denominator = None
    for i in range(1, x):
        cycle_length = get_length_of_recurring_cycle_in_reciprocal(i)
        if cycle_length >= longest_cycle_length:
            longest_cycle_length = cycle_length
            longest_cycle_length_denominator = i
    return longest_cycle_length_denominator


d = get_longest_recurring_cycle_reciprocal_denominator_below_x(1000)
print('Answer: %d' % d)
print('Cycle length in 1/%d\'s decimal representation: %d' %
      (d, get_length_of_recurring_cycle_in_reciprocal(d)))
