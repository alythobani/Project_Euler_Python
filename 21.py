"""
Solution to Problem 21 of Project Euler.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def get_sum_of_divisors(n):
    """Return the sum of all proper divisors of n."""
    divisor_sum = 0
    divisor = 1
    other_divisor = n
    while divisor <= other_divisor:
        if n % divisor == 0:
            divisor_sum += divisor
            if other_divisor != divisor:
                divisor_sum += other_divisor
        divisor += 1
        other_divisor = n / divisor
    return divisor_sum - n  # n doesn't count as a proper divisor


def has_amicable_number(n):
    """Return True if n is part of an amicable pair, else return False."""
    divisor_sum = get_sum_of_divisors(n)
    if divisor_sum == n:
        return False
    else:
        return get_sum_of_divisors(divisor_sum) == n


amicable_number_sum = 0
for x in range(1, 10000):
    if has_amicable_number(x):
        amicable_number_sum += x
print(amicable_number_sum)
