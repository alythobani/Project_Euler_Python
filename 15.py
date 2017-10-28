"""
Solution to problem 15 of Project Euler.

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""


number_of_routes_dict = {}


def number_of_routes(remaining_right, remaining_down):
    """
    Return the number of routes we can take to the bottom right corner.

    remaining_right: How far horizontally we are from the far right
    remaining_down: How far vertically we are from the bottom
    """
    if (remaining_right, remaining_down) in number_of_routes_dict:
        # We've already encountered this one
        return number_of_routes_dict[(remaining_right, remaining_down)]

    elif remaining_right == 0 and remaining_down == 0:
        # We are at the end
        number_of_routes_dict[(remaining_right, remaining_down)] = 0

    elif remaining_right == 0 or remaining_down == 0:
        # Either we can only go right, or we can only go down
        number_of_routes_dict[(remaining_right, remaining_down)] = 1

    # At this point, we can move either right or down

    elif remaining_right == remaining_down:
        # We are in a symmetrical grid position
        number_of_routes_dict[(remaining_right, remaining_down)] = \
            2 * number_of_routes(remaining_right - 1, remaining_down)

    else:
        number_of_routes_dict[(remaining_right, remaining_down)] = \
            (number_of_routes(remaining_right - 1, remaining_down) +
             number_of_routes(remaining_right, remaining_down - 1))

    return number_of_routes_dict[(remaining_right, remaining_down)]


print(number_of_routes(2, 2))
print(number_of_routes(20, 20))
