"""
Solution to Problem 25 of Project Euler.

The Fibonacci sequence is defined by the recurrence relation:

F(n) = F(n - 1) + F(n - 2), where F(1) = 1 and F(2) = 1.
Hence the first 12 terms will be:

F(1) = 1
F(2) = 1
F(3) = 2
F(4) = 3
F(5) = 5
F(6) = 8
F(7) = 13
F(8) = 21
F(9) = 34
F(10) = 55
F(11) = 89
F(12) = 144
The 12th term, F(12), is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""


def number_of_digits(n):
    """
    Return the number of digits in n.

    Assumptions:
    n > 0
    type(n) == <type 'int'>
    """
    return len(str(n))


def find_first_fib_term_with_x_digits(x):
    """
    Return the index of the first Fibonacci term with x digits.

    Assumption: x >= 2
    """
    fib_n_minus_1 = 1  # F(2) = 1
    fib_n = 2  # F(3) = 2
    n = 3  # Starting on n == 3
    while number_of_digits(fib_n) < x:
        old_fib_n = fib_n
        fib_n += fib_n_minus_1
        fib_n_minus_1 = old_fib_n
        n += 1
    return n


print(find_first_fib_term_with_x_digits(3))
print(find_first_fib_term_with_x_digits(1000))
