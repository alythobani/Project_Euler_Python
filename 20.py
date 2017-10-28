"""
Solution.

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n):
    """Return the factorial of n."""
    def factorial_helper(n, acc):
        if n == 1:
            return acc
        else:
            return factorial_helper(n - 1, acc * n)

    return factorial_helper(n, 1)


def sum_digits_of_n_factorial(n):
    """Return the sum of the digits of the factorial of n."""
    n_factorial = factorial(n)
    factorial_digit_sum = 0
    for digit in str(n_factorial):
        factorial_digit_sum += int(digit)
    return factorial_digit_sum


print(sum_digits_of_n_factorial(10))
print(sum_digits_of_n_factorial(100))
