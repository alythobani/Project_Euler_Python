"""
Project Euler 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples_of_3_below_1000 = [n * 3 for n in range(1, int(1000 / 3))]
multiples_of_5_below_1000 = [n * 5 for n in range(1, int(1000 / 5))]

if multiples_of_3_below_1000[-1] + 3 < 1000:
    multiples_of_3_below_1000.append(multiples_of_3_below_1000[-1] + 3)

if multiples_of_5_below_1000[-1] + 5 < 1000:
    multiples_of_5_below_1000.append(multiples_of_5_below_1000[-1] + 5)

final_sum = (sum(multiples_of_3_below_1000) +
             sum(multiples_of_5_below_1000) -
             sum(set(multiples_of_3_below_1000) &
                 set(multiples_of_5_below_1000)))

print(final_sum)
