"""
Solution to Problem 50 of Project Euler.

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""


def is_prime(n):
    """
    Return True if n is prime, else return False.

    Assumption: n >= 2
    """
    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        if factor == 2:
            factor += 1
        else:
            factor += 2
    return True


def solve(m):
    """
    Return the prime below m that is the sum of the most consecutive primes.

    >>> solve(100)
    41
    >>> solve(1000)
    953
    """
    longest_chain = 0
    longest_chain_prime = None
    all_primes_under_m = [p for p in range(2, m) if is_prime(p)]
    for starting_index in range(0, len(all_primes_under_m)):
        # Check chains longer than longest_chain that start at starting_index
        for ending_index in range(starting_index + longest_chain,
                                  len(all_primes_under_m)):
            primesum = sum(all_primes_under_m[starting_index:ending_index + 1])
            if primesum >= m:
                # This chain's sum is too big
                if ending_index == starting_index + longest_chain:
                    # This was our first try for starting_index and it already
                    #  is too big. No chains starting at an index higher than
                    #  starting_index will work, so we can end now!
                    return longest_chain_prime
                else:
                    # Move onto the next starting index
                    break
            if primesum in all_primes_under_m:
                chainlength = ending_index - starting_index + 1
                # print('New longest: %d from index %d creating %d' %
                #       (chainlength, starting_index, primesum))
                longest_chain = chainlength
                longest_chain_prime = primesum
    return longest_chain_prime


print(solve(100))
print(solve(1000))
print('Answer: %d' % solve(1000000))
