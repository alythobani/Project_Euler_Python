"""
Solution to Problem 39 of Project Euler.

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""


def get_all_triangles(p):
    """Return a set of all 90 degree triangles with perimeter p."""
    solution_set = set()
    for a in range(1, p / 3):
        for b in range(a, (p - a) / 2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solution_set.add((a, b, c))
    return solution_set


def get_number_of_traingles(p):
    """Return the number of 90 degree triangles with perimeter p."""
    return len(get_all_triangles(p))


def get_p_with_max_triangles():
    """Return p <= 1000 that maximizes get_number_of_traingles(p)."""
    max_p = 0
    max_triangles = 0
    for p in range(3, 1001):
        number_of_triangles = get_number_of_traingles(p)
        if number_of_triangles > max_triangles:
            print('New max: %d has %d solutions' % (p, number_of_triangles))
            max_triangles = number_of_triangles
            max_p = p
    return max_p


print(get_p_with_max_triangles())
