"""
Solution to Problem 40 of Project Euler.

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""


def print_answer():
    """Print the answer."""
    number_string = ''
    i = 1
    while len(number_string) < 1000000:
        number_string += str(i)
        i += 1
    digit_product = 1
    for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        digit_product *= int(number_string[i - 1])
    print(digit_product)


print_answer()
