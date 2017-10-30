"""
Solution to Problem 28 of Project Euler.

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""


def get_square_corner_sum(level):
    """
    Return the sum of the corners of the levelth square in the spiral.

    get_square_corner_sum(0)
         = 1
    get_square_corner_sum(1)
         = (1 + 2) + (1 + 2 + 2) + (1 + 2 + 2 + 2) + (1 + 2 + 2 + 2 + 2)
         = 4*1 + 2(1 + 2 + 3 + 4)
    get_square_corner_sum(2)
         = (9 + 4) + (9 + 4 + 4) + (9 + 4 + 4 + 4) + (9 + 4 + 4 + 4 + 4)
         = 4*9 + 4(1 + 2 + 3 + 4) = 4* (9 + 1 + 2 + 3 + 4)
    get_square_corner_sum(3)
         = (25 + 6) + (25 + 6 + 6) + (25 + 6 + 6 + 6) + (25 + 6 + 6 + 6 + 6)
         = 4*25 + 6(1 + 2 + 3 + 4)
    get_square_corner_sum(4)
         = (49 + 8) + (49 + 8 + 8) + (49 + 8 + 8 + 8) + (49 + 8 + 8 + 8 + 8)
         = 4*49 + 8(1 + 2 + 3 + 4)
    get_square_corner_sum(n) = 4 * ?(n) + (2 * n)(1 + 2 + 3 + 4)

    ?(1) = 1 = 1 + 8(0) = 1 + 4(1*0)
    ?(2) = 9 = 1 + 8(1) = 1 + 4(2*1)
    ?(3) = 25 = 1 + 8(3) = 1 + 4(3*2)
    ?(4) = 49 = 1 + 8(6) = 1 + 4(4*3)
    ?(5) = 81 = 1 + 8(10) = 1 + 4(5*4)
    ?(n) = 1 + 4(n * (n - 1))

    Thus:
    get_square_corner_sum(n) = 4 * (1 + 4 * n * (n - 1)) + (20 * n)
                             = 4 * (1 + 4n^2 - 4n) + 20 * n
                             = 4 + 16n^2 - 16n + 20n
                             = 16n^2 + 4n + 4
                             = 4(4n^2 + n + 1)
                             for n > 0

    >>> S(0)
    1
    >>> S(1)
    24
    >>> S(2)
    76
    >>> S(3)
    160
    """
    if level == 0:
        return 1
    else:
        return 16 * (level**2) + (4 * level) + 4


def get_diagonal_sum_in_n_by_n_spiral(n):
    """
    Return the sum of the diagonals in an n x n spiral starting at 1.

    D(1) = S(0)
    D(3) = S(0) + S(1)
    D(5) = S(0) + S(1) + S(2)
    D(n) = S(0) + S(1) + ... + S((n-1) / 2)

    >>> get_diagonal_sum_in_n_by_n_spiral(1)
    1
    >>> get_diagonal_sum_in_n_by_n_spiral(3)
    25
    >>> get_diagonal_sum_in_n_by_n_spiral(5)
    101
    """
    diagonal_sum = 0
    for i in range(0, (n + 1) / 2):
        diagonal_sum += get_square_corner_sum(i)
    return diagonal_sum


print(get_diagonal_sum_in_n_by_n_spiral(1))
print(get_diagonal_sum_in_n_by_n_spiral(3))
print(get_diagonal_sum_in_n_by_n_spiral(5))
print(get_diagonal_sum_in_n_by_n_spiral(1001))
