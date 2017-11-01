"""
Solution to Problem 42 of Project Euler.

The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""


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


def get_word_value(word):
    """
    Return the word value for word.

    Assumption: word consists of capital letters from A-Z

    >>> get_word_value_for_word('COLIN')
    53
    """
    word_value = 0
    for letter in word:
        word_value += get_alphabetical_value_for_letter(letter)
    return word_value


def is_triangle_word(word):
    """
    Return True if word's word value is a triangle number, else False.

    Return False otherwise.
    """
    word_value = get_word_value(word)
    i = 1
    while word_value > 0:
        word_value -= i
        i += 1
    return word_value == 0


def print_answer():
    """Print the answer."""
    words_file = open('data/p042_words.txt', 'r')
    words_string = words_file.read(50000)
    words_file.close()
    words_array = words_string.split(',')
    number_of_triangle_words = 0
    for word in words_array:
        if is_triangle_word(word):
            number_of_triangle_words += 1
    print('Answer: %d' % number_of_triangle_words)


print_answer()
