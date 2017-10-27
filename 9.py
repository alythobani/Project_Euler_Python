"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def find_pythagorean_triplet_adding_to_n(n):
    """
    Finds a pythagorean triplet a < b < c such that a + b + c = n. Returns it
    in dict form.

    If no such pythagorean triplet is found, returns False.

    Notes:
    c = n - a - b
    b < c = n - a - b
    2b < n - a
    b < (n - a)/2

    Returns a dict
    """

    for a in range(1, n - 1):

        for b in range(a + 1, (n - a) / 2 + 1):

            c = n - a - b

            if a >= b or b >= c:
                continue

            if a**2 + b**2 == c**2:
                return {'a': a, 'b': b, 'c': c}

    return False

triplet = find_pythagorean_triplet_adding_to_n(1000)
print('triplet: %s' % triplet)
product = triplet['a'] * triplet['b'] * triplet['c']
print('product: %d' % product)
