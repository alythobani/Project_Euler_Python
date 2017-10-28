"""
Solution to Problem 22 of Project Euler.

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


names_file = open('data/p022_names.txt', 'r')
names_string = names_file.read(47000)
names_file.close()
names_array = names_string.split(',')
sorted_names_array = sorted(names_array)


def get_alphabetical_value_for_letter(l):
    """
    Return the alphabetical value for l.

    Assumption: l is a capital letter from A-Z, or a double quote

    >>> get_alphabetical_value_for_letter('A')
    1
    >>> get_alphabetical_value_for_letter('C')
    3
    >>> get_alphabetical_value_for_letter('Z')
    26
    """
    return 0 if l == '"' else ord(l) - 64


def get_alphabetical_value_for_name(name):
    """
    Return the alphabetical value for name.

    Assumption: name consists of capital letters from A-Z

    >>> get_alphabetical_value_for_name('COLIN')
    53
    """
    alphabetical_value = 0
    for letter in name:
        alphabetical_value += get_alphabetical_value_for_letter(letter)
    return alphabetical_value


def get_name_score(name, location):
    """Return the name score for <name> at spot <location> in the names."""
    return get_alphabetical_value_for_name(name) * location


def print_total_score():
    """Return the total name score across all names."""
    total_score = 0

    for index, name in list(enumerate(sorted_names_array)):
        total_score += get_name_score(name, index + 1)

    print(total_score)


print_total_score()
