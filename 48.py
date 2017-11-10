"""
Solution to Problem 48 of Project Euler.

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def solve():
    """Return the answer."""
    power_sum = 0
    for i in range(1, 1001):
        power_sum += i**i
    return power_sum


total_sum = solve()
print('Answer: %d' % (total_sum % 10000000000))
