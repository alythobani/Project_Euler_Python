"""
Solution to Problem 36 of Project Euler.

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""


def decimal_to_binary(n):
    """Return n represented as a binary string."""
    binary_result = ''

    # Find the largest p such that 2^p <= n
    p = 0
    while 2**p <= n:
        p += 1
    p -= 1

    while p >= 0:
        binary_power = 2**p
        if binary_power <= n:
            n -= binary_power
            binary_result += '1'
        else:
            binary_result += '0'
        p -= 1
    return binary_result


def is_palindrome(number_string):
    """Return True if number_string is a palindrome, else return False."""
    for i in range(1, len(number_string) / 2 + 1):
        if number_string[i - 1] != number_string[-i]:
            return False
    return True


def print_answer():
    """Print the answer."""
    palindrome_sum = 0
    for i in range(1, 1000000):
        if is_palindrome(str(i)) and is_palindrome(decimal_to_binary(i)):
            palindrome_sum += i
    print(palindrome_sum)


print_answer()
