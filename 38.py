"""
Solution to Problem 38 of Project Euler.

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


def is_1_to_9_pandigital(number_str):
    """
    Return True if each digit 1 to 9 is found once in number_str, else False.

    >>> is_1_to_9_pandigital(99, 34, 3366)
    False
    >>> is_1_to_9_pandigital(12, 34, 408)
    False
    >>> is_1_to_9_pandigital(12, 34, 5678)
    False
    >>> is_1_to_9_pandigital(12, 345, 67899)
    False
    >>> is_1_to_9_pandigital(39, 186, 7254)
    True
    >>> is_1_to_9_pandigital(12, 345, 6789)
    True
    """
    if len(number_str) != 9:  # We need exactly 9 digits
        return False
    else:
        digits_needed = range(1, 10)
        for digit in number_str:
            try:
                digits_needed.remove(int(digit))
            except ValueError:
                # There is a duplicate digit
                return False
        return True


def find_largest_pandigital_concatenated_product():
    """
    Return the largest 1-to-9 pandigital number that satisfies the condition.

    Condition: the number can be formed as the concatenated product of an
    integer with (1, 2, ..., n) with n > 1.

    Note: the digits in the concatenated product will be at least twice the
    digits in the integer, so the integer can be at most 4 digits long.
    """
    largest_pandigital = 0
    for i in range(1, 10000):
        n = 1
        concatenated_product = ''
        while len(concatenated_product) < 9:
            concatenated_product += str(i * n)
            n += 1
        if is_1_to_9_pandigital(concatenated_product):
            if int(concatenated_product) >= largest_pandigital:
                largest_pandigital = int(concatenated_product)
                print('New largest: %d' % largest_pandigital)
    return largest_pandigital


print(find_largest_pandigital_concatenated_product())
