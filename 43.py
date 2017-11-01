"""
Solution to Problem 43 of Project Euler.

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


def find_all_permutations(number_string):
    """
    Generate all permutations of digits in number_string.

    Assumption: The initial call will ask to permute 9 digits.
    """
    if len(number_string) == 1:
        yield number_string
    for index, digit in list(enumerate(number_string)):
        other_digits = number_string[0:index] + number_string[index + 1:]
        for permutation in find_all_permutations(other_digits):
            yield digit + permutation


def is_specially_divisible(number):
    """Return True if number has the substring divisibilty property above."""
    for i, prime in list(enumerate([2, 3, 5, 7, 11, 13, 17])):
        if int(number[i + 1:i + 4]) % prime != 0:
            return False
    return True


def get_sum_of_specially_divisible_0_to_9_pandigitals():
    """
    Return the sum of specially divisible 0 to 9 pandigitals.

    By "specially divisble" we mean its substrings are divisible in the ways
    described above in this module's docstring.
    """
    digits_string = '1234567890'
    special_sum = 0
    for number in find_all_permutations(digits_string):
        # Avoid numbers that start with the digit 0, since their integer form
        #  is not pandigital
        if len(str(int(number))) != 10:
            continue
        if number[3] in ['1', '3', '5', '7', '9']:
            continue
        if number[5] not in ['5', '0']:
            continue
        if is_specially_divisible(number):
            print('Found one: %s' % number)
            special_sum += int(number)
    return special_sum


print(is_specially_divisible('1406357289'))
print(get_sum_of_specially_divisible_0_to_9_pandigitals())
