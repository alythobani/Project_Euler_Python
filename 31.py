"""
Solution to Problem 31 of Project Euler.

In England the currency is made up of pound, L, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1L (100p) and 2L (200p).
It is possible to make 2L in the following way:

1x1L + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2L be made using any number of coins?
"""


COINS_ARRAY = [1, 2, 5, 10, 20, 50, 100, 200]


def number_of_ways_to_make_x_pence(x, coins_array):
    """
    Return the number of ways to make x pence with values from coins_array.

    Assumption: coins_array is not empty

    >>> number_of_ways_to_make_x_pence(1, COINS_ARRAY)
    1
    >>> number_of_ways_to_make_x_pence(2, COINS_ARRAY)
    2
    >>> number_of_ways_to_make_x_pence(2, [1])
    1
    >>> number_of_ways_to_make_x_pence(2, [1, 2])
    2
    >>> number_of_ways_to_make_x_pence(2, [5])
    0
    >>> number_of_ways_to_make_x_pence(2, [2])
    1
    >>> number_of_ways_to_make_x_pence(5, [1, 2])
    3
    """
    if len(coins_array) == 1:
        return 1 if (x % coins_array[0] == 0) else 0
    else:
        number_of_ways = 0
        coin = coins_array[0]
        for number_of_coins in range(0, x / coin + 1):
            new_x = x - (coin * number_of_coins)
            if new_x == 0:
                number_of_ways += 1
                continue
            elif new_x < 0:
                continue
            else:
                coins_array_copy = coins_array[:]
                coins_array_copy.remove(coin)
                number_of_ways += number_of_ways_to_make_x_pence(
                    new_x, coins_array_copy)
        return number_of_ways


print(number_of_ways_to_make_x_pence(1, COINS_ARRAY))
print(number_of_ways_to_make_x_pence(2, COINS_ARRAY))
print(number_of_ways_to_make_x_pence(2, [1]))
print(number_of_ways_to_make_x_pence(2, [1, 2]))
print(number_of_ways_to_make_x_pence(2, [5]))
print(number_of_ways_to_make_x_pence(2, [2]))
print(number_of_ways_to_make_x_pence(5, [1, 2]))
print('Answer: %d' % number_of_ways_to_make_x_pence(200, COINS_ARRAY))
