"""
Solution to Problem 33 of Project Euler.

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""


ALL_DIGIT_STRINGS = [str(i) for i in range(1, 10)]


def are_fractions_equivalent(n1, d1, n2, d2):
    """
    Return True if n1/d1 == n2/d2 non-trivially, else return False.

    n1/d1 == n2/d2 trivially if n1 = 10 * n2 and d1 = 10 * d2.
    """
    return n1 * d2 == n2 * d1 and n1 != (10 * n2)


def get_cancelled_fractions():
    """Return a set of non-trivial examples of equivalent fractions."""
    def check_fractions(n1, d1, n2, d2):
        """If n1/d1 and n2/d2 are non-trivial examples, add them to our set."""
        if are_fractions_equivalent(n1, d1, n2, d2):
            print('%s/%s = %s/%s' % (n1, d1, n2, d2))
            cancelled_fractions_set.add((n2, d2))

    cancelled_fractions_set = set()
    for numerator in range(10, 99):
        first_digit = str(numerator)[0]
        possible_denominators_1 = [first_digit + d for d in ALL_DIGIT_STRINGS
                                   if int(first_digit + d) > numerator]
        new_numerator_1 = str(numerator)[1]
        for denominator_1 in possible_denominators_1:
            new_denominator_1 = denominator_1[1]
            check_fractions(int(numerator), int(denominator_1),
                            int(new_numerator_1), int(new_denominator_1))

        possible_denominators_2 = [d + first_digit for d in ALL_DIGIT_STRINGS
                                   if int(d + first_digit) > numerator]
        for denominator_2 in possible_denominators_2:
            new_denominator_2 = denominator_2[0]
            check_fractions(int(numerator), int(denominator_2),
                            int(new_numerator_1), int(new_denominator_2))

        second_digit = str(numerator)[1]
        possible_denominators_3 = [d + second_digit for d in ALL_DIGIT_STRINGS
                                   if int(d + second_digit) > numerator]
        new_numerator_2 = str(numerator)[0]
        for denominator_3 in possible_denominators_3:
            new_denominator_3 = denominator_3[0]
            check_fractions(int(numerator), int(denominator_3),
                            int(new_numerator_2), int(new_denominator_3))
        possible_denominators_4 = [second_digit + d for d in ALL_DIGIT_STRINGS
                                   if int(second_digit + d) > numerator]
        for denominator_4 in possible_denominators_4:
            new_denominator_4 = denominator_4[1]
            check_fractions(int(numerator), int(denominator_4),
                            int(new_numerator_2), int(new_denominator_4))

    return cancelled_fractions_set


def reduce_fraction(n, d):
    """
    Return n and d such that n/d is in lowest terms.

    Assumption: n < d
    """
    factor = 2
    while factor <= n:
        if n % factor == 0 and d % factor == 0:
            n /= factor
            d /= factor
        if n % factor != 0 or d % factor != 0:
            factor += 1
    return (n, d)


def print_answer():
    """Print the product of all non-trivial examples in lowest terms."""
    fractions_set = get_cancelled_fractions()
    product_numerator = 1
    product_denominator = 1
    for (n, d) in fractions_set:
        product_numerator *= int(n)
        product_denominator *= int(d)
    (n, d) = reduce_fraction(product_numerator, product_denominator)
    print('Product of fractions in lowest terms: %d/%d' % (n, d))


print_answer()
