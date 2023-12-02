"""
Advent of Code 2015 Day 5

The input contains a list of strings.
Each string in the list is a sequence of characters that must meet
certain criteria in order to be considered a nice string.
How many strings in the list are nice, given the conditions for being nice?

Part 1
-------
A nice string is one with all of the following properties:
 * It contains at least three vowels (aeiou only),
   like aei, xazegov, or aeiouaeiouaeiou.
 * It contains at least one letter that appears twice in a row,
   like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
 * It does not contain the strings ab, cd, pq, or xy,
   even if they are part of one of the other requirements.

Part 2
------
A nice string is one with all of the following properties:
 * It contains a pair of any two letters that appears at least twice
   in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
   but not like aaa (aa, but it overlaps).
 * It contains at least one letter which repeats
   with exactly one letter between them,
   like xyx, abcdefeghi (efe), or even aaa.
"""


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2015 Day 5 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    BAD_STRINGS = {"ab", "cd", "pq", "xy"}
    VOWELS = {"a", "e", "i", "o", "u"}

    # We can solve both parts in a single loop over the input,
    # and with a single pass over each string
    num_nice_strings_1 = 0
    num_nice_strings_2 = 0
    for string in puzzle:
        # Part 1 parameters
        bad_string_found = False
        double_found = False
        num_vowels = 0
        # Part 2 parameters
        pair_found = False
        pairs_seen = set()
        previous_pair = None
        split_repeat_found = False

        previous_char = None
        for char in string:
            if char in VOWELS:
                num_vowels = num_vowels + 1

            if previous_char is not None:
                if previous_char == char:
                    double_found = True
                if previous_char + char in BAD_STRINGS:
                    bad_string_found = True

                current_pair = previous_char + char
                if previous_pair is not None:
                    if (
                        current_pair != previous_pair
                        and current_pair in pairs_seen
                    ):
                        pair_found = True
                    if char == previous_pair[0]:
                        split_repeat_found = True
                previous_pair = previous_char + char
                pairs_seen.add(current_pair)
            previous_char = char

        if not bad_string_found and num_vowels >= 3 and double_found:
            num_nice_strings_1 = num_nice_strings_1 + 1
        if pair_found and split_repeat_found:
            num_nice_strings_2 = num_nice_strings_2 + 1

    if part == 1 or part is None:
        print(f"Part 1: The number of nice strings is {num_nice_strings_1}.")
    if part == 2 or part is None:
        print(f"Part 2: The number of nice strings is {num_nice_strings_2}.")
