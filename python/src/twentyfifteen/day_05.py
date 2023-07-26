"""
Advent of Code 2015 Day 5
"""


def is_nice_1(string: str) -> bool:
    """
    Determine if a string is nice according to the rules of part 1.
    A string is nice if:
        It has at least three vowels
        It contains at least one letter that appears twice in a row
        It does not contain the strings "ab", "cd", "pq", or "xy"

    :param string: The string to test
    :returns: Whether the string is nice
    """

    BAD_STRINGS = {"ab", "cd", "pq", "xy"}
    VOWELS = {"a", "e", "i", "o", "u"}

    bad_string_found = False
    double_found = False
    is_nice = False
    num_vowels = 0
    previous_char = None

    for char in string:
        if char in VOWELS:
            num_vowels = num_vowels + 1

        if previous_char is not None:
            if previous_char == char:
                double_found = True
            if previous_char + char in BAD_STRINGS:
                bad_string_found = True
                break

        previous_char = char

    if not bad_string_found and num_vowels >= 3 and double_found:
        is_nice = True

    return is_nice


def is_nice_2(string: str) -> bool:
    """
    Determine if a string is nice according to the rules of part 1.
    A string is nice if:
        It contains a pair of any two letters that appears at least twice
        in the string without overlapping
        It contains at least one letter which repeats
        with exactly one letter between them

    :param string: The string to test
    :returns: Whether the string is nice
    """

    is_nice = False
    pair_found = False
    pairs_seen = set()
    previous_char = None
    previous_pair = None
    split_repeat_found = False

    for char in string:
        if previous_char is not None:
            current_pair = previous_char + char
            if previous_pair is not None:
                if (
                    current_pair != previous_pair
                    and current_pair in pairs_seen
                ):
                    pair_found = True
                if char == previous_pair[0]:
                    split_repeat_found = True
            pairs_seen.add(current_pair)
            previous_pair = previous_char + char
        previous_char = char

    if pair_found and split_repeat_found:
        is_nice = True

    return is_nice


def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 5 puzzle.
    Each string in puzzle is a sequence of characters that must meet
    certain criteria in order to be considered a nice string.

    :param puzzle: the contents of the puzzle file
    """

    num_nice_strings_1 = 0
    num_nice_strings_2 = 0
    for string in puzzle:
        if is_nice_1(string):
            num_nice_strings_1 = num_nice_strings_1 + 1
        if is_nice_2(string):
            num_nice_strings_2 = num_nice_strings_2 + 1

    print(f"Part 1: The number of nice strings is {num_nice_strings_1}.")
    print(f"Part 2: The number of nice strings is {num_nice_strings_2}.")
