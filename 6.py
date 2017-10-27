"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def sum_of_first_n_squares(n):
    """
    Returns 1^2 + 2^2 + ... + n^2
    """

    return n * (n + 1) * (2 * n + 1) / 6


def sum_of_first_n_numbers(n):
    """
    Returns 1 + 2 + ... + n
    """

    return n * (n + 1) / 2


print(sum_of_first_n_numbers(10)**2 - sum_of_first_n_squares(10))

print(sum_of_first_n_numbers(100)**2 - sum_of_first_n_squares(100))
