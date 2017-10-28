"""
Solution to Problem 18 of Project Euler.

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)
"""


# Note: from index i on row j, you can move to index i or i+1 on row j+1.


triangle_string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
triangle_rows = triangle_string.split('\n')
triangle_array = [row.split(' ') for row in triangle_rows]
for i in range(0, len(triangle_array)):
    triangle_array[i] = [int(e) for e in triangle_array[i]]


max_sum_dict = {}


def max_sum_from_row_i_col_j(i, j):
    """
    Return the maximum path sum from row i, column j of triangle_array.

    Assumptions:
    0 <= i < len(triangle_array)
    0 <= j < len(triangle_array[i])
    """
    if (i, j) in max_sum_dict:
        # We have already encountered this position
        return max_sum_dict[(i, j)]

    elif i == len(triangle_array) - 1:
        # We are on the last row
        max_sum_dict[(i, j)] = triangle_array[i][j]

    else:
        max_sum_dict[(i, j)] = triangle_array[i][j] + max(
            max_sum_from_row_i_col_j(i + 1, j),
            max_sum_from_row_i_col_j(i + 1, j + 1))

    return max_sum_dict[(i, j)]


print(max_sum_from_row_i_col_j(0, 0))
