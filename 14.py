"""
Solution to problem 14 of Project Euler.

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def number_of_steps(n):
    """Return the sequence chain length from n to 1."""
    def number_of_steps_helper(n, acc):
        if n == 1:
            return acc + 1

        if n % 2 == 0:
            return number_of_steps_helper(n / 2, 1)

        else:
            return 1 + number_of_steps_helper(3 * n + 1, 1)

    return number_of_steps_helper(n, 0)


def longest_chain_under_n_starting_number(n):
    """Return the starting number under n that produces the longest chain."""
    longest_chain = 0
    longest_chain_starting_number = None

    x = 1

    while x < n:
        num_steps = number_of_steps(x)
        if num_steps > longest_chain:
            longest_chain = num_steps
            longest_chain_starting_number = x
        x += 1

    return longest_chain_starting_number


print(longest_chain_under_n_starting_number(1000000))
