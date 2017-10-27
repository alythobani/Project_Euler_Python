"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    """
    Determine if n is a palindromic number
    """

    string_n = str(n)

    i = 0
    while i < len(string_n) / 2:
        if string_n[i] != string_n[-i - 1]:
            return False
        i += 1

    return True


palindrome_list = set()


for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            palindrome_list.add(product)

print("largest palindrome: %d" % max(palindrome_list))
