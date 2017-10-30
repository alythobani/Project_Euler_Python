"""
Solution to Problem 30 of Project Euler.

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""


def sum_pth_powers_of_digits(n, p):
    """
    Return the sum of the pth power of each digit in n.

    >>> sum_pth_powers_of_digits(1634, 4)
    1634
    >>> sum_pth_powers_of_digits(8208, 4)
    8208
    >>> sum_pth_powers_of_digits(9474, 4)
    9474
    """
    digit_power_sum = 0
    for d in str(n):
        digit_power_sum += (int(d)**p)
    return digit_power_sum


def get_sum_of_numbers_that_are_the_sum_of_the_5th_power_of_their_digits():
    """
    Return every number that is the sum of each 5th power of its digits.

    Note: No number that is more than 6 digits long can be written as the sum
    of each 5th power of its digits. Even with the highest digits possible
    (e.g. 99999999), 8 * (9^5) is still only 6 digits long.
    """
    number_sum = 0
    for i in range(10, 999999):
        if i == sum_pth_powers_of_digits(i, 5):
            number_sum += i
    return number_sum


print(get_sum_of_numbers_that_are_the_sum_of_the_5th_power_of_their_digits())
