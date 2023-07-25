"""
Advent of Code 2015 Day 4
"""

import hashlib


def find_leading_zeros(key: str, num_zeroes: int) -> int:
    """
    Find the integer which combines with key to create an MD5 hash that
    starts with num_zeroes

    :param key: The key used by the MD5 hash
    :param num_zeroes:
        The number of zeroes the resulting digest must start with
    :returns: The integer that results in the desired hash digest
    """

    number = 1
    hash_found = False
    while not hash_found:
        md5 = hashlib.md5()
        md5.update(f"{key}{number}".encode("utf-8"))
        if md5.hexdigest().startswith("0" * num_zeroes):
            hash_found = True
        else:
            number = number + 1

    return number


def solve(puzzle: list[str]) -> None:
    """
    Solve the 2015 Day 4 puzzle.
    The input contains a string representing a secret key for MD5 hashing.

    Part 1
    ------
    What is the smallest positive number that produces an MD5 hash with
    five leading zeros?

    Part 2
    ------
    What is the smallest positive number that produces an MD5 hash with
    six leading zeros?

    :param puzzle: the contents of the puzzle file
    """

    if len(puzzle) > 1:
        raise ValueError(
            f"Unexpected puzzle length: expected a length of 1, "
            f"but found {len(puzzle)}."
        )

    key = puzzle[0]
    five_zero_int = find_leading_zeros(key, 5)
    six_zero_int = find_leading_zeros(key, 6)

    print(
        f"Part 1: The integer which produces five leading zeroes is "
        f"{five_zero_int}"
    )
    print(
        f"Part 2: The integer which produces six leading zeroes is "
        f"{six_zero_int}"
    )
