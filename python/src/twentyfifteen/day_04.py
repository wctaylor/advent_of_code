"""
Advent of Code 2015 Day 4

The input contains a string representing a secret key for MD5 hashing.

Part 1
------
What is the smallest positive number that produces an MD5 hash with
five leading zeros?

Part 2
------
What is the smallest positive number that produces an MD5 hash with
six leading zeros?
"""

import hashlib


def _generate_hash(key: str, num_zeros: int) -> int:
    """
    Generate an MD5 hash of the input key with a number of leading zeros

    :param key: The input to hash
    :param num_zeros: The number of zeros the hash must start with
    :returns: The first positive integer that generates the required hash
    """

    hash_start = "0" * num_zeros
    integer = 0
    solution = None
    while solution is None:
        integer = integer + 1
        md5 = hashlib.md5()
        md5.update(f"{key}{integer}".encode("utf-8"))
        if md5.hexdigest().startswith(hash_start):
            solution = integer

    return solution


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2015 Day 4 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    if len(puzzle) > 1:
        raise ValueError(
            f"Unexpected puzzle length: expected a length of 1, "
            f"but found {len(puzzle)}."
        )
    key = puzzle[0]

    if part == 1 or part is None:
        print(
            f"Part 1: The integer which produces five leading zeroes is "
            f"{_generate_hash(key, 5)}"
        )
    if part == 2 or part is None:
        print(
            f"Part 2: The integer which produces six leading zeroes is "
            f"{_generate_hash(key, 6)}"
        )
