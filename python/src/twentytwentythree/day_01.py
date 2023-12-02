"""
Advent of Code 2023 Day 1

The input is a list of strings.

Part 1
------
Each string creates a calibration value, which is a two digit number
comprised of the first and last digit in the string.

Part 2
------
The strings might spell out digits in addition to containing decimal digits,
and the spelled digits should count as valid digits.

In both cases, what is the sum of all the calibration values?
"""


def _get_calibration_value(line: str, digits: dict[str, int]) -> int:
    """
    Find the calibration value of the input line,
    which consists of the first and last digits in the line.

    :param line: The string to search
    :param digits:
        A dict mapping a string definition of a digit to an integer value
    """

    index_first = len(line)
    index_last = 0
    digit_first = "0"
    digit_last = "0"
    for digit in digits:
        if digit not in line:
            continue
        index = line.find(digit)
        if index <= index_first:
            index_first = index
            digit_first = digit
        index = line.rfind(digit)
        if index >= index_last:
            index_last = index
            digit_last = digit

    return 10 * digits[digit_first] + digits[digit_last]


def solve(puzzle: list[str], part: int | None = None) -> None:
    """
    Solve the 2023 Day 1 puzzle.

    :param puzzle: the contents of the puzzle file
    :param part: the part of the puzzle to solve. If None, solve both parts.
    """

    DIGITS_1 = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    DIGITS_2 = DIGITS_1.copy()
    DIGITS_2.update(
        {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }
    )

    total_1 = 0
    total_2 = 0
    for line in puzzle:
        if part == 1 or part is None:
            total_1 = total_1 + _get_calibration_value(line, digits=DIGITS_1)

        if part == 2 or part is None:
            total_2 = total_2 + _get_calibration_value(line, digits=DIGITS_2)

    if part == 1 or part is None:
        print(f"The sum of the calibration values is {total_1}.")
    if part == 2 or part is None:
        print(f"The sum of the calibration values is now {total_2}.")
