"""
Solution to Problem 34 of Project Euler.

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


FACTORIAL_DIGIT_DICT = {}


def factorial(n):
    """
    Return the factorial of n.

    Assumption: n is a digit from 0-9
    """
    def factorial_helper(n, acc):
        if n in [0, 1]:
            return acc
        else:
            return factorial_helper(n - 1, n * acc)
    if n not in FACTORIAL_DIGIT_DICT:
        FACTORIAL_DIGIT_DICT[n] = factorial_helper(n, 1)
    return FACTORIAL_DIGIT_DICT[n]


def get_digit_factorial_sum(n):
    """Return the sum of n's digit factorials."""
    digit_factorial_sum = 0
    for digit in str(n):
        digit_factorial_sum += factorial(int(digit))
    return digit_factorial_sum


def get_numbers_that_are_sums_of_their_digit_factorials():
    """
    Return every number that is a sum of its digits' factorials.

    Note: Since 9! == 362880, and get_digit_factorial_sum(9999999) == 2540160,
    no such number will exceed 2540160.

    Note: one digit numbers do not count as sums. They must be at least 2
    digits long.
    """
    number_list = []
    for i in range(10, 2540161):
        if i % 100000 == 0:
            print(i)
        if i == get_digit_factorial_sum(i):
            print('Found one: %d' % i)
            number_list.append(i)
    return number_list


print('Answer: %d' %
      sum(get_numbers_that_are_sums_of_their_digit_factorials()))
