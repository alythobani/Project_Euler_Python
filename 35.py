"""
Solution to Problem 35 of Project Euler.

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""


def is_prime(n):
    """
    Return True if n is prime, else return False.

    Assumed: n >= 2
    """
    factor = 2
    while factor <= n / factor:  # No point checking past the square root
        if n % factor == 0:
            return False
        factor += 1
    return True


def find_all_rotations(number_string):
    """Return an array of all rotations of digits in number_string."""
    if len(number_string) == 1:
        return [number_string]
    rotation_array = [number_string]
    for i in range(len(number_string) - 1):
        first_digit = number_string[0]
        other_digits = number_string[1:]
        number_string = other_digits + first_digit
        rotation_array.append(number_string)
    return rotation_array


def get_number_of_circular_primes_below_1000000():
    """Return the number of circular primes below one million."""
    # There are 13 circular primes below 100
    non_circular_primes = set(range(100)) - set(
        [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97])
    number_of_non_circular_primes = 99 - 13

    for i in range(100, 1000000):
        if i in non_circular_primes:
            # Covered already
            continue
        elif not is_prime(i):
            non_circular_primes.add(i)
            number_of_non_circular_primes += 1
            for rotation in find_all_rotations(str(i))[1:]:
                if len(str(int(rotation))) != len(str(i)):
                    # If there is a 0 in i, a lower-digit number will be caught
                    continue
                if int(rotation) == i:
                    # In case rotating i does not change it (e.g. i == 3333)
                    break
                non_circular_primes.add(int(rotation))
                number_of_non_circular_primes += 1
    return 999999 - number_of_non_circular_primes

number_of_circular_primes = get_number_of_circular_primes_below_1000000()
print(number_of_circular_primes)
