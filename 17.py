"""
Solution to Problem 17 of Project Euler.

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""


class InvalidNumberException(Exception):
    """Raised when an invalid number is inputted into a function from 17.py."""

    pass


def unit_digit_word(n):
    """
    Return a string of unit digit n written out in words.

    Assumption: 0 <= n <= 9
    """
    return {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        0: ''
    }[n]


def tens_word(n):
    """
    Return a string of n written out in words.

    Assumption: 10 <= n <= 99
    """
    if n >= 10 and n <= 19:
        return {
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen'
        }[n]

    else:
        return {
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety',
            0: ''
        }[n / 10] + unit_digit_word(n % 10)


def hundreds_word(n):
    """
    Return a string of n written out in words.

    Assumption: 100 <= n <= 999
    """
    return_string = unit_digit_word(n / 100) + 'hundred'
    if int(str(n)[-2:]):
        return_string += ('and' + tens_word(int(str(n)[-2:])))
    return return_string


def num_to_words(n):
    """
    Return a string of n written out in words, without spaces or hyphens.

    Assumption: 1 <= n <= 1000

    >>> num_to_words(1)
    'one'
    >>> num_to_words(20)
    'twenty'
    >>> num_to_words(309)
    'threehundredandnine'
    >>> num_to_words(115)
    'onehundredandfifteen'
    >>> num_to_words(342)
    'threehundredandfortytwo'
    >>> num_to_words(1000)
    'onethousand'
    >>> num_to_words(999)
    'ninehundredandninetynine'
    """
    num_string = str(n)

    if len(num_string) == 1:
        return unit_digit_word(n)

    elif len(num_string) == 2:
        return tens_word(n)

    elif len(num_string) == 3:
        return hundreds_word(n)

    elif len(num_string) == 4:
        if n == 1000:
            return 'onethousand'

    else:
        return InvalidNumberException(
            'invalid input %s into function num_to_words' % n)


number_of_letters = 0

for i in range(1, 1001):
    number_of_letters += len(num_to_words(i))

print(number_of_letters)
