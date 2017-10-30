"""
Solution to Problem 32 of Project Euler.

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""


def is_1_to_9_pandigital(multiplicand, multiplier, product):
    """
    Return True if each digit 1 to 9 is found once in the inputs, else False.

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
    identity_str = str(multiplicand) + str(multiplier) + str(product)
    if len(identity_str) != 9:  # We need exactly 9 digits
        return False
    else:
        digits_needed = range(1, 10)
        for digit in identity_str:
            try:
                digits_needed.remove(int(digit))
            except ValueError:
                # There is a duplicate digit
                return False
        return True


def contains_duplicate_digits(number):
    """
    Return True if a digit is found more than once in number, else False.

    >>> contains_duplicate_digits(999)
    True
    >>> contains_duplicate_digits(319)
    False
    >>> contains_duplicate_digits(2093)
    False
    >>> contains_duplicate_digits(1831)
    True
    """
    digit_array = range(1, 10)
    for digit in str(number):
        try:
            digit_array.remove(int(digit))
        except ValueError:
            return True
    return False


def get_all_possible_multipliers(remaining_digits):
    """Return all permutations up to 4 digits long from remaining_digits."""
    all_one_digit_multipliers = []
    all_two_digit_multipliers = []
    all_three_digit_multipliers = []
    all_four_digit_multipliers = []
    for digit1 in remaining_digits:
        all_one_digit_multipliers.append(digit1)
        remaining_digits_copy = remaining_digits[:]
        remaining_digits_copy.remove(digit1)
        for digit2 in remaining_digits_copy:
            all_two_digit_multipliers.append(digit1 * 10 + digit2)
            remaining_digits_copy_2 = remaining_digits_copy[:]
            remaining_digits_copy_2.remove(digit2)
            for digit3 in remaining_digits_copy_2:
                all_three_digit_multipliers.append(
                    digit1 * 100 + digit2 * 10 + digit3)
                remaining_digits_copy_3 = remaining_digits_copy_2[:]
                remaining_digits_copy_3.remove(digit3)
                for digit4 in remaining_digits_copy_3:
                    all_four_digit_multipliers.append(
                        digit1 * 1000 + digit2 * 100 + digit3 * 10 + digit4)
    return (all_one_digit_multipliers + all_two_digit_multipliers +
            all_three_digit_multipliers + all_four_digit_multipliers)


def get_all_1_to_9_pandigital_products():
    """Return a set of all products whose identity can be 1 to 9 pandigital."""
    set_of_pandigital_products = set()

    # Note: since the product is at least as many digits as the multiplier, and
    #  same for the multiplicand, neither can exceed 4 digits.
    for multiplicand in [n for n in range(1, 10000)
                         if not contains_duplicate_digits(n)]:
        remaining_digits = range(1, 10)
        for digit in str(multiplicand):
            remaining_digits.remove(int(digit))
        for multiplier in get_all_possible_multipliers(remaining_digits):
            product = multiplicand * multiplier
            if is_1_to_9_pandigital(multiplicand, multiplier, product):
                print('Found one! %d x %d = %d' %
                      (multiplicand, multiplier, product))
                set_of_pandigital_products.add(product)
    return set_of_pandigital_products

all_1_to_9_pandigital_products = get_all_1_to_9_pandigital_products()
print(all_1_to_9_pandigital_products)
print('Answer: %d' % sum(all_1_to_9_pandigital_products))
